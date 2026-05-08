# Comparative Topological Analysis of Biological Neural Networks Using Canonical Complex Network Models

## 1. Introduction
This project asks which canonical complex network model best approximates the topology of a real biological neural network. The biological network analyzed here is the C. elegans connectome from the OpenWorm ConnectomeToolbox. Four canonical model families are compared against it: Erdos-Renyi random graphs, regular ring lattices, Watts-Strogatz small-world graphs, and Barabasi-Albert scale-free graphs.

The question is not whether a nervous system is exactly one simple mathematical graph model. Biological neural systems are shaped by development, spatial constraints, function, and evolution. The goal is narrower and more appropriate for a complex systems course: measure major topological properties of one empirical neural graph, generate matched synthetic baselines, and identify which model gives the closest approximation under a transparent metric-distance criterion.

## 2. Background
Complex systems contain many interacting units whose collective behavior is not obvious from isolated components. Neural systems are a natural example: neurons and muscles interact through synaptic and electrical connections, producing global behavior through network topology. In this setting, graph structure matters because topology affects communication efficiency, clustering, modularity, hub formation, and robustness to damage.

Random networks, represented here by the Erdos-Renyi model, provide a baseline in which edges are placed without strong local structure. These graphs often have short path lengths but low clustering and weak hub structure.

Lattice networks represent the opposite extreme: nodes connect mostly to local neighbors. They usually have high clustering but long path lengths, which limits global integration.

Small-world networks, represented by the Watts-Strogatz model, interpolate between lattices and random graphs. They retain clustering while adding shortcuts that reduce path length. This is biologically relevant because nervous systems often require both local specialization and fast global communication.

Scale-free networks, represented by the Barabasi-Albert model, grow through preferential attachment and produce hubs. Hubs can support efficient routing and integration, but they also make networks more vulnerable to targeted removal of high-degree nodes.

Biological neural networks may combine several of these traits. They can show emergence through many local interactions, modular organization, high clustering, short paths, hubs, and non-random robustness patterns.

## 3. Dataset
The dataset used is:

- Dataset: OpenWorm ConnectomeToolbox `aconnectome_white_1986_whole.csv`
- Source URL: `https://raw.githubusercontent.com/openworm/ConnectomeToolbox/main/cect/data/aconnectome_white_1986_whole.csv`
- Local raw file: `data/raw/celegans_aconnectome_white_1986_whole.csv`
- Raw records: 2,961 synaptic connection rows
- Directed graph: 309 nodes and 2,812 directed edges
- Undirected graph: 309 nodes and 2,511 undirected edges
- Edge attributes: connection type (`chemical` or `electrical`) and synapse count (`synapses`)

The raw dataset is directed and weighted. For the core comparison, the project uses an undirected topology projection so that all canonical synthetic models can be compared consistently. Edge weights and connection types are preserved in the processed edge list, but the reported topological metrics are computed on the unweighted graph unless otherwise stated. Self-loops are removed. The largest connected component contains all 309 nodes in this run, so no nodes were excluded for shortest-path calculations.

## 4. Methods
The pipeline performs the following steps:

1. Download the C. elegans connectome CSV into `data/raw/`.
2. Load the raw table with columns for presynaptic node, postsynaptic node, connection type, and synapse count.
3. Build both a directed weighted graph and an undirected projection.
4. Remove self-loops.
5. Save the processed edge list to `data/processed/celegans_processed_edges.csv`.
6. Generate matched synthetic graphs with the same node count as the empirical graph and approximately matched edge count or average degree.
7. Compute graph metrics for the empirical graph and all synthetic models.
8. Run robustness experiments under random node removal and targeted high-degree node removal.
9. Rank synthetic models by normalized metric distance from the empirical graph.

The synthetic graphs are:

- Erdos-Renyi random graph using `G(n, m)` to match the empirical edge count exactly.
- Regular lattice graph using a ring lattice with approximately the same average degree.
- Watts-Strogatz small-world graph using the same node count and approximate average degree.
- Barabasi-Albert scale-free graph using an attachment parameter chosen from the empirical average degree.

For the Watts-Strogatz model, the rewiring probability sweep used:

`[0, 0.001, 0.005, 0.01, 0.03, 0.05, 0.1, 0.3, 0.5, 1.0]`

The best Watts-Strogatz probability is selected by comparing average clustering coefficient and average shortest path length against the biological graph.

The selected metrics for final model-distance ranking are average clustering coefficient, average shortest path length, density, degree variance, modularity, assortativity, and global efficiency. For each metric, the normalized absolute difference from the empirical value is computed, and the model score is the mean of those normalized differences. Lower distance means closer similarity under this specific objective.

## 5. Experiments
The main metric experiment computed:

- Number of nodes and edges
- Density
- Average degree and degree variance
- Average clustering coefficient
- Transitivity
- Average shortest path length on the largest connected component
- Diameter
- Global efficiency
- Maximum degree and top hubs
- Mean degree, betweenness, and closeness centralities
- Greedy modularity communities and modularity
- Degree assortativity

The robustness experiment removed fractions of nodes equal to 0%, 5%, 10%, 20%, 30%, 40%, and 50%. Random node removal was repeated 20 times per fraction, reporting mean and standard deviation of the largest connected component fraction. Targeted attack removed nodes in descending order of degree and measured the remaining largest connected component fraction.

## 6. Results
The empirical C. elegans analysis graph has 309 nodes and 2,511 undirected edges. Its density is 0.0528 and its average degree is 16.25. The graph has average clustering 0.3511, average shortest path length 2.6649, global efficiency 0.4308, modularity 0.3689, and degree variance 180.04.

The most connected node in the processed graph is `LegacyBodyWallMuscles` with degree 114. Major neuronal hubs include `AVAR`, `AVAL`, `AVBL`, `AVBR`, `AVER`, `AVDR`, `AVEL`, `PVCL`, and `PVCR`. This hub structure is one reason the scale-free model scores well on the final distance metric.

The final model-distance ranking is:

| Rank | Model | Distance |
|---:|---|---:|
| 1 | Barabasi-Albert | 0.2999 |
| 2 | Watts-Strogatz | 0.3464 |
| 3 | Erdos-Renyi | 0.4536 |
| 4 | Regular lattice | 0.9819 |

The Erdos-Renyi graph matches the edge count and density but has much lower clustering and much smaller degree variance than the biological network. The regular lattice has high clustering but much longer paths and no hub variation. The Watts-Strogatz graph captures short paths and moderate clustering, but it does not reproduce the empirical hub structure as strongly. The Barabasi-Albert graph gives the best overall score because it better approximates the empirical degree heterogeneity while still producing short paths.

The robustness results support the same hybrid interpretation. The biological graph remains relatively robust under random node removal, but targeted removal of high-degree nodes damages connectivity more strongly. This is consistent with networks that contain important hubs, a scale-free-like property, while still retaining clustering and modular organization that are common in biological systems.

## 7. Discussion
The closest canonical approximation in this run is the Barabasi-Albert scale-free model. However, this result should not be interpreted as proving that the C. elegans nervous system is a pure scale-free network. The biological graph also has substantial clustering and modularity, and its average shortest path length is short. Those properties are closely associated with small-world organization and biological modularity.

The evidence therefore supports a hybrid complex-network interpretation. The empirical network has hubs, which improve integration but create vulnerability to targeted attacks. It also has clustering and communities, which support local specialization. Its short average path length supports efficient communication across the whole network. These features together fit the broader complex systems idea that biological organization emerges from many constrained local interactions rather than from one idealized graph-generation rule.

The regular lattice model is least similar because local connectivity alone creates path lengths that are too long and degree variation that is too small. The random model is useful as a density-matched baseline, but it misses the empirical clustering and hub structure. The Watts-Strogatz model is scientifically important here because it explains the coexistence of clustering and short paths, even though the final normalized score ranks it behind the scale-free model.

## 8. Limitations
This analysis is based on one biological connectome dataset. It does not prove that the human brain, all brains, or all neural systems have the same topology. Network properties depend on species, developmental stage, scale, measurement method, and preprocessing choices.

The core comparison uses an undirected unweighted projection. That makes the canonical model comparison simpler and cleaner, but it loses directionality, synapse multiplicity, and chemical/electrical distinction. A weighted or directed analysis could change some conclusions.

The normalized distance ranking depends on the chosen metrics. Emphasizing clustering more heavily might favor Watts-Strogatz; emphasizing degree heterogeneity or hubs might favor Barabasi-Albert. Synthetic models are also stochastic, so exact values can vary by random seed.

Finally, canonical network models are simplified baselines. Biological networks are shaped by anatomical constraints, cell identities, functional pressures, and developmental mechanisms not represented in these models.

## 9. Conclusion
For this dataset and metric set, the Barabasi-Albert scale-free model provides the closest overall approximation to the C. elegans connectome topology, followed by the Watts-Strogatz small-world model. The answer to the research question is therefore: among the four tested canonical models, scale-free is the closest by normalized multi-metric distance, but the biological network is better understood as a hybrid complex network with hub structure, clustering, modularity, short paths, and non-random robustness behavior.

## 10. Future Work
Future extensions could:

- Analyze directed and weighted versions of the same connectome.
- Compare chemical and electrical subnetworks separately.
- Add additional biological connectome datasets from other organisms or modalities.
- Compare motif frequencies and rich-club organization.
- Run model ensembles over many seeds instead of one representative graph per model.
- Test additional generative models with spatial constraints or modular growth.

## 11. References
1. OpenWorm ConnectomeToolbox data repository.
2. White, J. G., Southgate, E., Thomson, J. N., and Brenner, S. (1986). The structure of the nervous system of the nematode Caenorhabditis elegans.
3. Erdos, P., and Renyi, A. (1959). On random graphs.
4. Watts, D. J., and Strogatz, S. H. (1998). Collective dynamics of small-world networks.
5. Barabasi, A. L., and Albert, R. (1999). Emergence of scaling in random networks.
6. Newman, M. E. J. (2010). Networks: An Introduction.
