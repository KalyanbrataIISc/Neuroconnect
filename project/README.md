# Comparative Topological Analysis of Biological Neural Networks Using Canonical Complex Network Models

## Research question
Which canonical network model best approximates the topology of a real biological neural network (C. elegans): random, lattice, small-world, or scale-free?

## Dataset used
- **Dataset**: OpenWorm ConnectomeToolbox `aconnectome_white_1986_whole.csv`
- **URL**: https://raw.githubusercontent.com/openworm/ConnectomeToolbox/main/cect/data/aconnectome_white_1986_whole.csv
- **Raw rows**: 2961 synaptic records
- **Directed graph**: 309 nodes, 2812 edges, weighted (`synapses`) and typed (`chemical`/`electrical`)
- **Analysis graph**: undirected, unweighted topology over largest connected component (309 nodes, 2511 edges)

## Project structure
- `data/raw/`: downloaded raw connectome
- `data/processed/`: cleaned edge list for analysis
- `results/figures/`: all plots
- `results/tables/`: metric and experiment tables
- `src/`: end-to-end code
- `report/final_report.md`: course-report narrative

## Install
```bash
python -m pip install -r requirements.txt
```

If using the local conda environment from this machine:

```bash
conda run -n coglab python -m pip install -r requirements.txt
```

## Run the full pipeline
```bash
python src/main.py
```

Local conda command used for this rerun:

```bash
conda run -n coglab python src/main.py
```

## Main finding (short summary)
Using normalized multi-metric distance, the **Barabási-Albert (scale-free)** model was the closest overall to the C. elegans topology in this run, followed by **Watts-Strogatz (small-world)**. This supports a **hybrid interpretation**: biological connectomes combine hub structure, clustering, and short path lengths rather than matching one pure canonical model.

## Output files generated
### Figures
- `real_network_visualization.png`
- `model_network_visualizations.png`
- `degree_distribution_comparison.png`
- `clustering_vs_pathlength_ws_sweep.png`
- `metric_comparison_barplot.png`
- `centrality_distribution_comparison.png`
- `robustness_random_removal.png`
- `robustness_targeted_removal.png`
- `model_distance_ranking.png`

### Tables
- `real_network_summary.csv`
- `all_metrics_comparison.csv`
- `model_distance_ranking.csv`
- `ws_sweep_results.csv`
- `robustness_random.csv`
- `robustness_targeted.csv`
