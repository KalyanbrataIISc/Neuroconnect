"""Visualization placeholders for network and metric comparison outputs."""

from __future__ import annotations

from pathlib import Path

import networkx as nx
import pandas as pd


def plot_network(G: nx.Graph, output_path: str | Path, title: str) -> Path:
    """Plot a single network graph.

    Args:
        G: Graph to visualize.
        output_path: Destination figure path.
        title: Figure title.

    Returns:
        Destination path as a ``Path`` object.
    """
    _ = G, title
    return Path(output_path)


def plot_model_networks(graph_dict: dict[str, nx.Graph], output_path: str | Path) -> Path:
    """Plot empirical and synthetic model networks side by side.

    Args:
        graph_dict: Mapping of graph labels to NetworkX graph objects.
        output_path: Destination figure path.

    Returns:
        Destination path as a ``Path`` object.
    """
    _ = graph_dict
    return Path(output_path)


def plot_degree_distributions(
    graph_dict: dict[str, nx.Graph],
    output_path: str | Path,
) -> Path:
    """Plot degree distributions for empirical and synthetic graphs.

    Args:
        graph_dict: Mapping of graph labels to NetworkX graph objects.
        output_path: Destination figure path.

    Returns:
        Destination path as a ``Path`` object.
    """
    _ = graph_dict
    return Path(output_path)


def plot_metric_comparison(metrics_df: pd.DataFrame, output_path: str | Path) -> Path:
    """Plot a comparison of selected network metrics.

    Args:
        metrics_df: Table of metrics for all graphs.
        output_path: Destination figure path.

    Returns:
        Destination path as a ``Path`` object.
    """
    _ = metrics_df
    return Path(output_path)


def plot_model_distance_ranking(
    distance_df: pd.DataFrame,
    output_path: str | Path,
) -> Path:
    """Plot model-distance rankings.

    Args:
        distance_df: Table containing model distances and ranks.
        output_path: Destination figure path.

    Returns:
        Destination path as a ``Path`` object.
    """
    _ = distance_df
    return Path(output_path)

