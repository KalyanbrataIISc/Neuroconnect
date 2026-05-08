from __future__ import annotations

from pathlib import Path
import urllib.request

import networkx as nx
import pandas as pd

DATASET_URL = "https://raw.githubusercontent.com/openworm/ConnectomeToolbox/main/cect/data/aconnectome_white_1986_whole.csv"
DATASET_NAME = "OpenWorm ConnectomeToolbox - aconnectome_white_1986_whole.csv"


def download_dataset(raw_dir: Path) -> Path:
    raw_dir.mkdir(parents=True, exist_ok=True)
    out = raw_dir / "celegans_aconnectome_white_1986_whole.csv"
    if not out.exists():
        urllib.request.urlretrieve(DATASET_URL, out)
    return out


def load_raw_connectome(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path, sep="\t")


def build_graphs(df: pd.DataFrame) -> tuple[nx.DiGraph, nx.Graph]:
    dfg = df.rename(columns={"pre": "source", "post": "target", "synapses": "weight", "type": "connection_type"})
    directed = nx.DiGraph()
    for _, r in dfg.iterrows():
        directed.add_edge(str(r["source"]), str(r["target"]), weight=float(r["weight"]), connection_type=str(r["connection_type"]))

    undirected = nx.Graph()
    for u, v, data in directed.edges(data=True):
        w = data.get("weight", 1.0)
        ctype = data.get("connection_type", "unknown")
        if undirected.has_edge(u, v):
            undirected[u][v]["weight"] += w
            undirected[u][v]["connection_type"] = "mixed" if undirected[u][v]["connection_type"] != ctype else ctype
        else:
            undirected.add_edge(u, v, weight=w, connection_type=ctype)

    undirected.remove_edges_from(nx.selfloop_edges(undirected))
    directed.remove_edges_from(nx.selfloop_edges(directed))
    return directed, undirected


def preprocess_graph(G: nx.Graph) -> tuple[nx.Graph, nx.Graph]:
    largest_nodes = max(nx.connected_components(G), key=len)
    lcc = G.subgraph(largest_nodes).copy()
    return G, lcc


def save_processed_graph(G: nx.Graph, output_path: str | Path) -> Path:
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    rows = [{"source": u, "target": v, "weight": d.get("weight", 1.0), "connection_type": d.get("connection_type", "unknown")} for u, v, d in G.edges(data=True)]
    pd.DataFrame(rows).to_csv(out, index=False)
    return out


def save_real_network_summary(raw_df: pd.DataFrame, directed: nx.DiGraph, undirected: nx.Graph, lcc: nx.Graph, out_path: Path) -> Path:
    summary = pd.DataFrame([
        {
            "dataset_name": DATASET_NAME,
            "source_url": DATASET_URL,
            "raw_rows": len(raw_df),
            "directed_nodes": directed.number_of_nodes(),
            "directed_edges": directed.number_of_edges(),
            "directed_weighted": True,
            "undirected_nodes": undirected.number_of_nodes(),
            "undirected_edges": undirected.number_of_edges(),
            "undirected_weighted": True,
            "analysis_graph": "undirected_unweighted_lcc_metrics",
            "lcc_nodes": lcc.number_of_nodes(),
            "lcc_edges": lcc.number_of_edges(),
        }
    ])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(out_path, index=False)
    return out_path
