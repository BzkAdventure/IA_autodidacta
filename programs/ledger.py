"""Append-only ledger. A refused amount never changes the file."""

from datetime import date
from pathlib import Path


def add(path, amount, note: str) -> None:
    path = Path(path)
    text = "" if amount is None else str(amount).strip()
    if text == "":
        raise ValueError("empty input")
    try:
        value = float(text)
    except ValueError:
        raise ValueError("bad amount") from None
    if value != value or value in (float("inf"), float("-inf")):
        raise ValueError("bad amount")
    line = f"{date.today().isoformat()}\t{value}\t{note}\n"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(line)


def report(path):
    path = Path(path)
    raw = path.read_text(encoding="utf-8")
    lines = []
    total = 0.0
    for line in raw.splitlines():
        if line.strip() == "":
            continue
        day, value_text, note = line.split("\t")
        value = float(value_text)
        lines.append((day, value, note))
        total += value
    return lines, total
