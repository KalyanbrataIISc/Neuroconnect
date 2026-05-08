# Comparative Topological Analysis of Biological Neural Networks Using Canonical Complex Network Models

## 1. Introduction
This project evaluates which canonical complex network model best approximates a real biological neural graph topology.

## 2. Background
Complex systems show emergence from many interacting units. In neural systems, topology influences integration, segregation, robustness, and communication efficiency. Canonical references are random, lattice, small-world, and scale-free models.

## 3. Dataset
We used the OpenWorm ConnectomeToolbox C. elegans dataset (`aconnectome_white_1986_whole.csv`). It includes directed weighted edges with connection type labels. For topology comparison we used an undirected unweighted projection and its largest connected component.

## 4. Methods
- Download and clean dataset
- Remove self-loops
- Build analysis graph (undirected), extract LCC for path metrics
- Generate ER, lattice, WS, BA models matched by node count and approx. degree/edge count
- WS sweep over p in [0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.1, 0.3, 0.5, 1.0]
- Compute graph metrics and robustness
- Rank model similarity by normalized mean metric distance over: clustering, path length, density, degree variance, modularity, assortativity, global efficiency

## 5. Experiments
- Metric extraction for each graph
- Random node removal (20 repeats, mean±std)
- Targeted hub removal (descending degree)

## 6. Results
- Dataset summary: 309 nodes, 2511 undirected edges in analysis graph
- Best WS p selected by clustering/path match
- Distance ranking: **Barabási-Albert first**, **Watts-Strogatz second**, then ER, then lattice
- Robustness: biological graph is more resilient to random removal than targeted hub removal, indicating hub dependence

## 7. Discussion
The C. elegans topology appears hybrid. It does not map perfectly to one canonical class. The best overall fit is scale-free-like under the chosen distance objective, while small-world characteristics remain evident via clustering/path behavior.

## 8. Limitations
- Single species/single dataset scope
- Projection to undirected unweighted graph loses direction and synapse-strength detail
- Rankings depend on selected metrics and normalization
- Stochastic model generation introduces seed sensitivity

## 9. Conclusion
For this dataset and metric set, **Barabási-Albert (scale-free) provides the closest overall approximation**, with **Watts-Strogatz close behind**, supporting a biologically plausible hybrid topology interpretation.

## 10. Future Work
- Add directed and weighted analyses
- Compare multiple connectomes (e.g., male/hermaphrodite variants or other species)
- Use motif-level and multiscale community comparisons

## 11. References
1. OpenWorm ConnectomeToolbox data repository.
2. Watts & Strogatz (1998), small-world networks.
3. Barabási & Albert (1999), scale-free networks.
