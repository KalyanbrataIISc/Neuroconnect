from __future__ import annotations

from typing import Any

import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities, modularity


def compute_all_metrics(G: nx.Graph) -> dict[str, Any]:
    n = G.number_of_nodes()
    m = G.number_of_edges()
    deg = [d for _, d in G.degree()]
    avg_degree = (sum(deg) / n) if n else 0
    lcc = G.subgraph(max(nx.connected_components(G), key=len)).copy() if n else G

    degree_c = nx.degree_centrality(G)
    between_c = nx.betweenness_centrality(G)
    close_c = nx.closeness_centrality(G)
    hubs = sorted(G.degree, key=lambda x: x[1], reverse=True)[:10]
    comms = list(greedy_modularity_communities(G)) if n > 0 and m > 0 else []
    mod = modularity(G, comms) if comms else 0.0

    assort = nx.degree_assortativity_coefficient(G) if n > 1 and m > 0 else 0
    if assort != assort:
        assort = 0.0

    return {
        "num_nodes": n,
        "num_edges": m,
        "density": nx.density(G) if n > 1 else 0,
        "average_degree": avg_degree,
        "degree_variance": float(__import__('numpy').var(deg)) if deg else 0,
        "average_clustering": nx.average_clustering(G) if n > 0 else 0,
        "transitivity": nx.transitivity(G) if n > 2 else 0,
        "average_shortest_path_length": nx.average_shortest_path_length(lcc) if lcc.number_of_nodes() > 1 else 0,
        "diameter": nx.diameter(lcc) if lcc.number_of_nodes() > 1 else 0,
        "global_efficiency": nx.global_efficiency(G) if n > 1 else 0,
        "max_degree": max(deg) if deg else 0,
        "top_10_hub_nodes": str(hubs),
        "degree_distribution": str(deg),
        "degree_centrality_mean": sum(degree_c.values()) / len(degree_c) if degree_c else 0,
        "betweenness_centrality_mean": sum(between_c.values()) / len(between_c) if between_c else 0,
        "closeness_centrality_mean": sum(close_c.values()) / len(close_c) if close_c else 0,
        "modularity": mod,
        "num_communities": len(comms),
        "assortativity": float(assort),
    }
