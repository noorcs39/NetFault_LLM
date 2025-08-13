import json
from typing import List, Tuple
import pandas as pd

THRESHOLDS = {
    "latency": 100,          # milliseconds
    "jitter": 30,            # milliseconds
    "packet_loss": 5,        # percent
    "channel_quality": 70,   # percent, lower is worse
    "distant_devices": 20,   # count
}

SEVERITY_LEVELS = ["Normal", "Moderate", "Critical"]

def max_severity(a: str, b: str) -> str:
    return SEVERITY_LEVELS[max(SEVERITY_LEVELS.index(a), SEVERITY_LEVELS.index(b))]

def load_data(path: str) -> pd.DataFrame:
    """Load network metrics from a CSV file."""
    return pd.read_csv(path)

def analyze_row(row: pd.Series) -> Tuple[List[str], str]:
    """Analyze a single row of metrics and return detected issues and severity."""
    issues: List[str] = []
    severity = "Normal"

    if row["latency"] > THRESHOLDS["latency"]:
        issues.append("High latency")
        severity = max_severity(severity, "Moderate")
        if row["latency"] > THRESHOLDS["latency"] * 1.5:
            severity = "Critical"

    if row["jitter"] > THRESHOLDS["jitter"]:
        issues.append("Elevated jitter")
        severity = max_severity(severity, "Moderate")
        if row["jitter"] > THRESHOLDS["jitter"] * 1.5:
            severity = "Critical"

    if row["packet_loss"] > THRESHOLDS["packet_loss"]:
        issues.append("Packet loss")
        severity = max_severity(severity, "Moderate")
        if row["packet_loss"] > THRESHOLDS["packet_loss"] * 1.5:
            severity = "Critical"

    if row["channel_quality"] < THRESHOLDS["channel_quality"]:
        issues.append("Poor channel quality")
        severity = max_severity(severity, "Moderate")
        if row["channel_quality"] < THRESHOLDS["channel_quality"] * 0.8:
            severity = "Critical"

    if row["distant_devices"] > THRESHOLDS["distant_devices"]:
        issues.append("Too many distant devices")
        severity = max_severity(severity, "Moderate")
        if row["distant_devices"] > THRESHOLDS["distant_devices"] * 1.5:
            severity = "Critical"

    return issues, severity

def analyze(df: pd.DataFrame) -> List[dict]:
    """Analyze all rows in a DataFrame."""
    results = []
    for _, row in df.iterrows():
        issues, severity = analyze_row(row)
        results.append({
            "customer_id": row.get("customer_id"),
            "issues": issues,
            "severity": severity,
        })
    return results

def generate_response(results: List[dict]) -> str:
    """Generate a text summary for detected issues."""
    lines = []
    for result in results:
        if result["issues"]:
            lines.append(
                f"Customer {result['customer_id']}: {result['severity']} issues - "
                + ", ".join(result["issues"])
            )
        else:
            lines.append(f"Customer {result['customer_id']}: No issues detected")
    return "\n".join(lines)
