"""Append-only ledger. A refused amount never changes the file."""

from datetime import date
from pathlib import Path #Path is a class that represents a file or directory path.


def add(path, amount, note: str) -> None:
    #we could also initialize amount as a float, but we would need to check if the input is a valid float.
    #A ledger command usually reads what someone typed, and that text may be empty or not a number
    path = Path(path)
    text = "" if amount is None else str(amount).strip()
    if text == "":
        raise ValueError("empty input")
    try:
        value = float(text)
    except ValueError:
        raise ValueError("bad amount") from None
    if value != value or value in (float("inf"), float("-inf")): 
    #if the value is not a number, or is infinity,
    #or is negative infinity, raise an error. We could also use the built-in function math.isnan(value) to check if the value is a number.
        raise ValueError("bad amount")
    line = f"{date.today().isoformat()}\t{value}\t{note}\n"
    #date.today().isoformat() returns the current date in the format YYYY-MM-DD
    #\t is a tab character
    #value is the amount of the transaction
    #note is the note of the transaction
    #Example: 2026-10-20\t100.00\tSalary

    with path.open("a", encoding="utf-8") as handle: 
        #open the file in append mode, and write the line to the file.
        handle.write(line)


def report(path): #report is a function that reads the ledger file and returns a report of the transactions and the total amount.
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
