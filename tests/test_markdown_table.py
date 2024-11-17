import pytest
from markdown_table import MarkdownTable

def test_creation():
    headers = ["Column1", "Column2"]
    rows = [[1, 2], [3, 4]]
    table = MarkdownTable(headers, rows)
    assert len(table.headers) == 2
    assert len(table.rows) == 2

def test_add_row():
    table = MarkdownTable(["A", "B"])
    table.add_row([1, 2])
    assert len(table.rows) == 1

def test_invalid_row():
    table = MarkdownTable(["A", "B"])
    with pytest.raises(ValueError):
        table.add_row([1])  # Недостаточно столбцов

def test_to_string():
    table = MarkdownTable(["A", "B"], [[1, 2], [3, 4]])
    result = table.to_string()
    assert "| A | B |" in result
