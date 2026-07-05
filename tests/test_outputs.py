from pathlib import Path
import json


def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_nonempty():
    """The report file is not empty."""
    assert Path("/app/report.json").stat().st_size > 0, "report.json is empty"

def test_total_requests_property():
    """how many requests there were."""

    assert "total_requests" in json.load(Path("/app/report.json").open())


def test_clients_involved_property():
    """the clients involved."""

    assert "unique_ips" in json.load(Path("/app/report.json").open())


def test_popular_pages_property():
    """which pages are popular."""

    assert "top_path" in json.load(Path("/app/report.json").open())

