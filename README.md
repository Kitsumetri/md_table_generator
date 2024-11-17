# MarkdownTable

A Python library for generating Markdown tables easily.

## Installation

To install from GitHub:
```bash
pip install git+https://github.com/Kitsumetri/md_table_generator.git
```

## To build locally
```bash
pip install .
````


## Usage

### Creating table

* From dict:
```python
from markdown_table import MarkdownTable
data = {
    "Language": ["Python", 'C', 'C++', 'Java'],
    "Rating": [0, 5, 1, 3]
}
table = MarkdownTable.from_dict(data=data)
```

* From Iterable rows & columns:
```python
from markdown_table import MarkdownTable

table = MarkdownTable(
    headers=["Language", 'Rating'],
    rows=[('Python', 0), ('C', 5), ('C++', 1), ('Java', 3)],
    alignment='center',  # 'left' (Default), 'right', 'center'
)
```

### Updating table

* Add column:
```python
from markdown_table import MarkdownTable
data = {
    "Language": ["Python", 'C', 'C++', 'Java'],
    "Rating": [0, 5, 1, 3]
}
table = MarkdownTable.from_dict(data=data)
table.add_column(column_name='Marker', values=['✅', '✅', '✅', '🚫'])
```

* Add row/rows:
```python
from markdown_table import MarkdownTable
data = {
    "Language": ["Python", 'C', 'C++', 'Java'],
    "Rating": [0, 5, 1, 3]
}
table = MarkdownTable.from_dict(data=data)
table.add_row(['C#', 2.5])
table.add_rows([('JS', -1), ('Brainfuck', 'infinity')])
```

### Utils methods
* Sort by column:
```python
from markdown_table import MarkdownTable
data = {
    "Language": ["Python", 'C', 'C++', 'Java'],
    "Rating": [0, 5, 1, 3]
}
table = MarkdownTable.from_dict(data=data)
table.sort_rows(column_index=1, reverse=False)
```

* Filter rows by callable condition
```python
from markdown_table import MarkdownTable
data = {
    "Language": ["Python", 'C', 'C++', 'Java'],
    "Rating": [0, 5, 1, 3]
}
table = MarkdownTable.from_dict(data=data)
table.filter_rows(condition=lambda x: x[0] != 'C')
```

### Export:
```python
from markdown_table import MarkdownTable
table = MarkdownTable(<init_params>)
print(table.to_string())  # md repr
print(table.to_html())  # html repr
table.to_csv('table.csv')  # csv file
table.save_to_file('table.md')  # md file
```