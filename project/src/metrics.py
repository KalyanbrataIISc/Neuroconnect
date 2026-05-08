"""Metric calculation placeholders for empirical and synthetic networks."""

from __future__ import annotations

from typing import Any

import networkx as nx


def compute_basic_metrics(G: nx.Graph) -> dict[str, Any]:
    """Compute basic graph summary metrics.

    Args:
        G: Graph to summarize.

    Returns:
        Placeholder dictionary containing node and edge counts.
    """
    return {
        "num_nodes": G.number_of_nodes(),
        "num_edges": G.number_of_edges(),
    }


def compute_small_world_metrics(G: nx.Graph) -> dict[str, Any]:
    """Compute small-world-related network metrics.

    Args:
        G: Graph to analyze.

    Returns:
        Empty placeholder dictionary.
    """
    _ = G
    return {}


def compute_centrality_metrics(G: nx.Graph) -> dict[str, Any]:
    """Compute centrality metrics for important nodes.

    Args:
        G: Graph to analyze.

    Returns:
        Empty placeholder dictionary.
    """
    _ = G
    return {}


def compute_community_metrics(G: nx.Graph) -> dict[str, Any]:
    """Compute community-structure metrics.

    Args:
        G: Graph to analyze.

    Returns:
        Empty placeholder dictionary.
    """
    _ = G
    return {}


def compute_all_metrics(G: nx.Graph) -> dict[str, Any]:
    """Compute all planned graph metrics.

    Args:
        G: Graph to analyze.

    Returns:
        Combined placeholder metrics dictionary.
    """
    metrics: dict[str, Any] = {}
    metrics.update(compute_basic_metrics(G))
    metrics.update(compute_small_world_metrics(G))
    metrics.update(compute_centrality_metrics(G))
    metrics.update(compute_community_metrics(G))
    return metrics

