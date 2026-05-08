from __future__ import annotations
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

import compare_models, generate_networks, load_data, metrics, robustness, visualize

PROJECT_ROOT = Path(__file__).resolve().parents[1]
FRACTIONS=[0,0.05,0.1,0.2,0.3,0.4,0.5]
WS_P=[0,0.001,0.005,0.01,0.03,0.05,0.1,0.3,0.5,1.0]

def ensure_dirs():
    for p in ["data/raw","data/processed","results/figures","results/tables","report","notebooks"]:
        (PROJECT_ROOT/p).mkdir(parents=True, exist_ok=True)

def main():
    ensure_dirs()
    raw_path=load_data.download_dataset(PROJECT_ROOT/"data/raw")
    raw_df=load_data.load_raw_connectome(raw_path)
    directed, undirected=load_data.build_graphs(raw_df)
    clean, lcc=load_data.preprocess_graph(undirected)
    load_data.save_processed_graph(clean, PROJECT_ROOT/"data/processed/celegans_processed_edges.csv")
    load_data.save_real_network_summary(raw_df,directed,clean,lcc,PROJECT_ROOT/"results/tables/real_network_summary.csv")

    real_metrics=metrics.compute_all_metrics(lcc)
    avg_degree=int(round(real_metrics['average_degree']))
    ws_rows=[]
    for p in WS_P:
        G=generate_networks.generate_ws_graph(lcc.number_of_nodes(),avg_degree,p,seed=42)
        m=metrics.compute_all_metrics(G)
        ws_rows.append({"rewiring_p":p,"average_clustering":m['average_clustering'],"average_shortest_path_length":m['average_shortest_path_length'],"match_score":abs(m['average_clustering']-real_metrics['average_clustering'])+abs(m['average_shortest_path_length']-real_metrics['average_shortest_path_length'])})
    ws_df=pd.DataFrame(ws_rows).sort_values('rewiring_p')
    ws_df.to_csv(PROJECT_ROOT/"results/tables/ws_sweep_results.csv", index=False)
    best_p=float(ws_df.sort_values('match_score').iloc[0]['rewiring_p'])

    graphs=generate_networks.generate_all_models(lcc,best_ws_p=best_p,seed=42)
    metrics_rows=[]; model_metrics={}
    for name,G in graphs.items():
        mm=metrics.compute_all_metrics(G); model_metrics[name]=mm; metrics_rows.append({"network":name,**mm})
    metrics_df=pd.DataFrame(metrics_rows)
    metrics_df.to_csv(PROJECT_ROOT/"results/tables/all_metrics_comparison.csv", index=False)
    ranking=compare_models.rank_models(model_metrics['real'],model_metrics)
    ranking.to_csv(PROJECT_ROOT/"results/tables/model_distance_ranking.csv", index=False)

    rand_rows=[]; targ_rows=[]
    for name,G in graphs.items():
        for r in robustness.random_node_removal_experiment(G,FRACTIONS,repeats=20,seed=42): r['network']=name; rand_rows.append(r)
        for t in robustness.targeted_node_removal_experiment(G,FRACTIONS): t['network']=name; targ_rows.append(t)
    pd.DataFrame(rand_rows).to_csv(PROJECT_ROOT/"results/tables/robustness_random.csv", index=False)
    pd.DataFrame(targ_rows).to_csv(PROJECT_ROOT/"results/tables/robustness_targeted.csv", index=False)

    figs=PROJECT_ROOT/"results/figures"
    visualize.plot_network(graphs['real'], figs/"real_network_visualization.png", "C. elegans LCC")
    visualize.plot_model_networks(graphs, figs/"model_network_visualizations.png")
    visualize.plot_degree_distributions(graphs, figs/"degree_distribution_comparison.png")
    visualize.plot_metric_comparison(metrics_df, figs/"metric_comparison_barplot.png")
    visualize.plot_model_distance_ranking(ranking, figs/"model_distance_ranking.png")

    plt.figure(figsize=(8,5)); plt.plot(ws_df['rewiring_p'],ws_df['average_clustering'],marker='o',label='clustering'); plt.plot(ws_df['rewiring_p'],ws_df['average_shortest_path_length'],marker='s',label='path length'); plt.xscale('symlog', linthresh=0.001); plt.legend(); plt.tight_layout(); plt.savefig(figs/"clustering_vs_pathlength_ws_sweep.png",dpi=200); plt.close()

    plt.figure(figsize=(8,5))
    for name,G in graphs.items():
        dc=list(nx.degree_centrality(G).values()); bc=list(nx.betweenness_centrality(G).values())
        plt.scatter(dc,bc,s=10,alpha=0.4,label=name)
    plt.xlabel('Degree centrality'); plt.ylabel('Betweenness centrality'); plt.legend(fontsize=7); plt.tight_layout(); plt.savefig(figs/"centrality_distribution_comparison.png",dpi=200); plt.close()

    rr=pd.read_csv(PROJECT_ROOT/"results/tables/robustness_random.csv"); plt.figure(figsize=(8,5))
    for name,g in rr.groupby('network'): plt.errorbar(g['fraction_removed'],g['lcc_mean'],yerr=g['lcc_std'],label=name,marker='o')
    plt.legend(fontsize=7); plt.xlabel('Fraction removed'); plt.ylabel('Largest CC fraction'); plt.tight_layout(); plt.savefig(figs/"robustness_random_removal.png",dpi=200); plt.close()

    tr=pd.read_csv(PROJECT_ROOT/"results/tables/robustness_targeted.csv"); plt.figure(figsize=(8,5))
    for name,g in tr.groupby('network'): plt.plot(g['fraction_removed'],g['lcc_mean'],label=name,marker='o')
    plt.legend(fontsize=7); plt.xlabel('Fraction removed'); plt.ylabel('Largest CC fraction'); plt.tight_layout(); plt.savefig(figs/"robustness_targeted_removal.png",dpi=200); plt.close()

    print('Pipeline complete')

if __name__=='__main__':
    main()
