"""Synthetic complex-network model generation placeholders."""

from __future__ import annotations

import networkx as nx


def generate_er_graph(n: int, m: int, seed: int = 42) -> nx.Graph:
    """Prepare an Erdos-Renyi random graph placeholder.

    Args:
        n: Number of nodes.
        m: Number of edges.
        seed: Random seed for reproducibility.

    Returns:
        An empty NetworkX graph placeholder with ``n`` nodes.
    """
    _ = m, seed
    G = nx.Graph()
    G.add_nodes_from(range(n))
    return G


def generate_lattice_graph(n: int, avg_degree: int, seed: int = 42) -> nx.Graph:
    """Generate a regular lattice-style graph placeholder.

    Args:
        n: Number of nodes.
        avg_degree: Intended average degree.
        seed: Random seed reserved for future use.

    Returns:
        An empty NetworkX graph placeholder with ``n`` nodes.
    """
    _ = avg_degree, seed
    G = nx.Graph()
    G.add_nodes_from(range(n))
    return G


def generate_ws_graph(
    n: int,
    avg_degree: int,
    rewiring_p: float,
    seed: int = 42,
) -> nx.Graph:
    """Generate a Watts-Strogatz small-world graph placeholder.

    Args:
        n: Number of nodes.
        avg_degree: Target neighborhood degree parameter.
        rewiring_p: Rewiring probability.
        seed: Random seed for reproducibility.

    Returns:
        An empty NetworkX graph placeholder with ``n`` nodes.
    """
    _ = avg_degree, rewiring_p, seed
    G = nx.Graph()
    G.add_nodes_from(range(n))
    return G


def generate_ba_graph(n: int, avg_degree: int, seed: int = 42) -> nx.Graph:
    """Generate a Barabasi-Albert scale-free graph placeholder.

    Args:
        n: Number of nodes.
        avg_degree: Intended average degree used to derive attachment count.
        seed: Random seed for reproducibility.

    Returns:
        An empty NetworkX graph placeholder with ``n`` nodes.
    """
    _ = avg_degree, seed
    G = nx.Graph()
    G.add_nodes_from(range(n))
    return G


def generate_all_models(real_graph: nx.Graph, seed: int = 42) -> dict[str, nx.Graph]:
    """Generate all planned synthetic graph models for comparison.

    Args:
        real_graph: Empirical graph whose size and density guide model setup.
        seed: Random seed for reproducibility.

    Returns:
        A dictionary of model names to placeholder graph instances.
    """
    n = real_graph.number_of_nodes()
    m = real_graph.number_of_edges()
    avg_degree = round((2 * m / n) if n else 0)
    return {
        "erdos_renyi": generate_er_graph(n, m, seed=seed),
        "regular_lattice": generate_lattice_graph(n, avg_degree, seed=seed),
        "watts_strogatz": generate_ws_graph(n, avg_degree, rewiring_p=0.1, seed=seed),
        "barabasi_albert": generate_ba_graph(n, avg_degree, seed=seed),
    }
