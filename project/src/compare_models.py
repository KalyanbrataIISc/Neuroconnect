from __future__ import annotations

from typing import Any
import pandas as pd

SELECTED = ["average_clustering", "average_shortest_path_length", "density", "degree_variance", "modularity", "assortativity", "global_efficiency"]


def normalized_metric_distance(real_metrics: dict[str, Any], model_metrics: dict[str, Any], selected_metrics=SELECTED) -> float:
    vals = []
    for k in selected_metrics:
        r = float(real_metrics[k]); m = float(model_metrics[k])
        denom = abs(r) if abs(r) > 1e-9 else 1.0
        vals.append(abs(m - r) / denom)
    return float(sum(vals) / len(vals))


def rank_models(real_metrics: dict[str, Any], model_metrics_dict: dict[str, dict[str, Any]]) -> pd.DataFrame:
    rows=[]
    for name, mm in model_metrics_dict.items():
        if name=="real":
            continue
        rows.append({"model": name, "distance": normalized_metric_distance(real_metrics, mm)})
    df = pd.DataFrame(rows).sort_values("distance").reset_index(drop=True)
    df["rank"] = df.index + 1
    return df
