"""Quiet Dread — a one-line code review comment.

Reads the approved-PR comment from entry.txt, writes it to
/output/entry.txt (where the sealed scorer reads it), and prints it.
"""

from pathlib import Path

ENTRY_FILENAME = "entry.txt"
OUTPUT_PATH = Path("/output/entry.txt")


def load_comment() -> str:
    raw = Path(__file__).with_name(ENTRY_FILENAME).read_text(encoding="utf-8")
    return raw.strip()


def publish(comment: str) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(comment + "\n", encoding="utf-8")
    print(comment)


def main() -> None:
    publish(load_comment())


if __name__ == "__main__":
    main()
