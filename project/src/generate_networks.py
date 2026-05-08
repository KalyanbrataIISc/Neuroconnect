from __future__ import annotations

import networkx as nx


def _safe_k(avg_degree: float, n: int) -> int:
    k = max(2, int(round(avg_degree)))
    if k % 2 == 1:
        k += 1
    if k >= n:
        k = n - 1 if (n - 1) % 2 == 0 else n - 2
    return max(2, k)


def generate_er_graph(n: int, m: int, seed: int = 42) -> nx.Graph:
    return nx.gnm_random_graph(n, m, seed=seed)


def generate_lattice_graph(n: int, avg_degree: int, seed: int = 42) -> nx.Graph:
    _ = seed
    k = _safe_k(avg_degree, n)
    return nx.watts_strogatz_graph(n, k, 0)


def generate_ws_graph(n: int, avg_degree: int, rewiring_p: float, seed: int = 42) -> nx.Graph:
    k = _safe_k(avg_degree, n)
    return nx.watts_strogatz_graph(n, k, rewiring_p, seed=seed)


def generate_ba_graph(n: int, avg_degree: int, seed: int = 42) -> nx.Graph:
    m = max(1, int(round(avg_degree / 2)))
    return nx.barabasi_albert_graph(n, m, seed=seed)


def generate_all_models(real_graph: nx.Graph, best_ws_p: float, seed: int = 42) -> dict[str, nx.Graph]:
    n = real_graph.number_of_nodes()
    m = real_graph.number_of_edges()
    avg_degree = (2 * m / n) if n else 2
    return {
        "real": real_graph.copy(),
        "erdos_renyi": generate_er_graph(n, m, seed=seed),
        "regular_lattice": generate_lattice_graph(n, int(round(avg_degree)), seed=seed),
        "watts_strogatz": generate_ws_graph(n, int(round(avg_degree)), rewiring_p=best_ws_p, seed=seed),
        "barabasi_albert": generate_ba_graph(n, int(round(avg_degree)), seed=seed),
    }
