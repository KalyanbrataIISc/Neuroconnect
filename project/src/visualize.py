from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

def plot_network(G, output_path, title):
    output_path=Path(output_path); output_path.parent.mkdir(parents=True,exist_ok=True)
    plt.figure(figsize=(8,6)); pos=nx.spring_layout(G, seed=42)
    nx.draw_networkx(G,pos,node_size=20,with_labels=False,width=0.3)
    plt.title(title); plt.tight_layout(); plt.savefig(output_path,dpi=200); plt.close(); return output_path

def plot_model_networks(graph_dict, output_path):
    output_path=Path(output_path); plt.figure(figsize=(15,8))
    for i,(name,G) in enumerate(graph_dict.items(),1):
        plt.subplot(2,3,i); pos=nx.spring_layout(G,seed=42); nx.draw_networkx(G,pos,node_size=12,with_labels=False,width=0.2); plt.title(name); plt.axis('off')
    plt.tight_layout(); plt.savefig(output_path,dpi=200); plt.close(); return output_path

def plot_degree_distributions(graph_dict, output_path):
    plt.figure(figsize=(8,6))
    for name,G in graph_dict.items():
        deg=sorted([d for _,d in G.degree()], reverse=True)
        plt.plot(range(1,len(deg)+1), deg, marker='o', linestyle='none', markersize=2, alpha=0.6, label=name)
    plt.xscale('log'); plt.yscale('log'); plt.legend(); plt.xlabel('Rank'); plt.ylabel('Degree'); plt.tight_layout(); plt.savefig(output_path,dpi=200); plt.close(); return Path(output_path)

def plot_metric_comparison(metrics_df, output_path):
    cols=["average_clustering","average_shortest_path_length","density","degree_variance","modularity","assortativity","global_efficiency"]
    ax=metrics_df.set_index('network')[cols].plot(kind='bar', figsize=(12,6)); ax.legend(bbox_to_anchor=(1.02,1)); plt.tight_layout(); plt.savefig(output_path,dpi=200); plt.close(); return Path(output_path)

def plot_model_distance_ranking(distance_df, output_path):
    plt.figure(figsize=(8,5)); plt.bar(distance_df['model'], distance_df['distance']); plt.ylabel('Normalized distance'); plt.tight_layout(); plt.savefig(output_path,dpi=200); plt.close(); return Path(output_path)
