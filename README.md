# MarkdownTable

A Python library for generating Markdown tables easily.

## Installation

To install from GitHub:
```bash
pip install git+https://github.com/username/markdown_table.git
```

## To build locally
pip install .


## Usage
```python
from markdown_table import MarkdownTable

headers = ["Name", "Age"]
rows = [["Alice", 30], ["Bob", 25]]
table = MarkdownTable(headers, rows)
print(table.to_string())

```