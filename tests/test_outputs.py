import json
from pathlib import Path


def load_report():
    path = Path("/app/report.json")
    assert path.exists(), "no report.json found"
    report = json.loads(path.read_text())
    assert isinstance(report, dict), "report.json must contain a JSON object"
    return report


def test_report_exists():
    """The agent produced a report file and saved findings for review."""
    report = load_report()
    assert "total_requests" in report, "report.json missing total_requests"
    assert report["total_requests"] == 6


def test_report_nonempty():
    """The report contains the expected client and page summary values."""
    report = load_report()
    assert report["unique_ips"] == 3
    assert report["top_path"] == "/index.html"
