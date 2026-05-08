from __future__ import annotations

from typing import Iterable
import random
import numpy as np
import networkx as nx


def _lcc_frac(G: nx.Graph, original_n: int) -> float:
    if G.number_of_nodes() == 0:
        return 0.0
    return len(max(nx.connected_components(G), key=len)) / original_n


def random_node_removal_experiment(G: nx.Graph, fractions: Iterable[float], repeats: int = 20, seed: int = 42) -> list[dict[str, float]]:
    rng = random.Random(seed)
    nodes = list(G.nodes())
    n = len(nodes)
    res = []
    for f in fractions:
        vals = []
        k = int(round(f * n))
        for _ in range(repeats):
            rem = set(rng.sample(nodes, k)) if k > 0 else set()
            H = G.copy(); H.remove_nodes_from(rem)
            vals.append(_lcc_frac(H, n))
        res.append({"fraction_removed": f, "lcc_mean": float(np.mean(vals)), "lcc_std": float(np.std(vals)), "mode": "random"})
    return res


def targeted_node_removal_experiment(G: nx.Graph, fractions: Iterable[float]) -> list[dict[str, float]]:
    ordered = [n for n, _ in sorted(G.degree(), key=lambda x: x[1], reverse=True)]
    n = len(ordered)
    out = []
    for f in fractions:
        k = int(round(f * n))
        H = G.copy(); H.remove_nodes_from(ordered[:k])
        out.append({"fraction_removed": f, "lcc_mean": _lcc_frac(H, n), "lcc_std": 0.0, "mode": "targeted"})
    return out
