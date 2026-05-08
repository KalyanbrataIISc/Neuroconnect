"""Robustness experiment placeholders for connectome graph analysis."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import networkx as nx


def random_node_removal_experiment(
    G: nx.Graph,
    fractions: Iterable[float],
    repeats: int = 20,
    seed: int = 42,
) -> list[dict[str, float]]:
    """Run a random node-removal robustness experiment.

    Args:
        G: Graph to test.
        fractions: Fractions of nodes to remove.
        repeats: Number of repeated trials per fraction.
        seed: Random seed for reproducibility.

    Returns:
        Empty list placeholder for future experiment results.
    """
    _ = G, list(fractions), repeats, seed
    return []


def targeted_node_removal_experiment(
    G: nx.Graph,
    fractions: Iterable[float],
) -> list[dict[str, float]]:
    """Run a targeted node-removal robustness experiment.

    Args:
        G: Graph to test.
        fractions: Fractions of high-importance nodes to remove.

    Returns:
        Empty list placeholder for future experiment results.
    """
    _ = G, list(fractions)
    return []


def plot_robustness_results(results: list[dict[str, float]], output_path: str | Path) -> Path:
    """Plot robustness experiment results.

    Args:
        results: Robustness experiment output records.
        output_path: Destination figure path.

    Returns:
        Destination path as a ``Path`` object.
    """
    _ = results
    return Path(output_path)

