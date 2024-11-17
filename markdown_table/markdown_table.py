import logging
from typing import Any, Iterable, List, Union, Dict


class MarkdownTable:
    def __init__(self, headers: Iterable[Union[str, int]], rows: Iterable[Iterable[Any]] = None, alignment: str = "left", column_padding: int = 1):
        self.headers = self._validate_headers(headers)
        self.rows = self._validate_rows(rows) if rows else []
        self.alignment = self._validate_alignment(alignment)
        self.column_padding = self._validate_column_padding(column_padding)

    @staticmethod
    def _validate_headers(headers: Iterable[Union[str, int]]) -> List[str]:
        if not headers or not isinstance(headers, Iterable):
            raise ValueError("Headers must be a non-empty iterable.")
        return [str(header) for header in headers]

    @staticmethod
    def _validate_rows(rows: Iterable[Iterable[Any]]) -> List[List[str]]:
        if not isinstance(rows, Iterable):
            raise ValueError("Rows must be an iterable of iterables.")
        return [list(map(str, row)) for row in rows]

    @staticmethod
    def _validate_alignment(alignment: str) -> str:
        if alignment not in {"left", "center", "right"}:
            raise ValueError("Alignment must be one of 'left', 'center', or 'right'.")
        return alignment

    @staticmethod
    def _validate_column_padding(padding: int) -> int:
        if not isinstance(padding, int) or padding < 0:
            raise ValueError("Column padding must be a non-negative integer.")
        return padding

    def _get_alignment_format(self) -> List[str]:
        alignment_map = {"left": ":---", "center": ":---:", "right": "---:"}
        return [alignment_map[self.alignment]] * len(self.headers)

    def add_row(self, row: Iterable[Any]) -> None:
        if len(row) != len(self.headers):
            raise ValueError("Row must have the same number of elements as headers.")
        self.rows.append(list(map(str, row)))
        logging.info("Row added: %s", row)

    def add_rows(self, rows: Iterable[Iterable[Any]]) -> None:
        for row in rows:
            self.add_row(row)

    @classmethod
    def from_dict(cls, data: Dict[Any, List[Any]], **kwargs) -> "MarkdownTable":
        if not data:
            raise ValueError("Data dictionary cannot be empty.")
        headers = list(data.keys())
        rows = zip(*data.values())
        return cls(headers=headers, rows=rows, **kwargs)

    def to_string(self) -> str:
        padding = " " * self.column_padding
        header_line = " | ".join(f"{padding}{header}{padding}" for header in self.headers)
        separator_line = " | ".join(self._get_alignment_format())
        rows_lines = [" | ".join(f"{padding}{cell}{padding}" for cell in row) for row in self.rows]
        result = f"| {header_line} |\n| {separator_line} |\n" + "\n".join(f"| {line} |" for line in rows_lines)
        logging.info("Table generated:\n%s", result)
        return result

    def save_to_file(self, file_path: str) -> None:
        table_string = self.to_string()
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(table_string)
        logging.info("Table saved to file: %s", file_path)

    def sort_rows(self, column_index: int, reverse: bool = False) -> None:
        if column_index < 0 or column_index >= len(self.headers):
            raise IndexError("Column index out of range.")
        self.rows.sort(key=lambda row: row[column_index], reverse=reverse)

    def filter_rows(self, condition: callable) -> None:
        self.rows = [row for row in self.rows if condition(row)]

    def add_column(self, column_name: str, values: Iterable[Any]) -> None:
        if len(values) != len(self.rows):
            raise ValueError("Number of values must match the number of rows.")
        self.headers.append(column_name)
        for i, value in enumerate(values):
            self.rows[i].append(str(value))

    def to_csv(self, file_path: str) -> None:
        import csv
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)
            writer.writerows(self.rows)

    def to_html(self) -> str:
        rows = "".join(f"<tr>{''.join(f'<td>{cell}</td>' for cell in row)}</tr>" for row in self.rows)
        headers = "".join(f"<th>{header}</th>" for header in self.headers)
        return f"<table><thead><tr>{headers}</tr></thead><tbody>{rows}</tbody></table>"

    def validate(self) -> None:
        row_lengths = [len(row) for row in self.rows]
        if len(set(row_lengths)) > 1:
            raise ValueError("All rows must have the same number of columns.")
        logging.info("Table is valid.")
