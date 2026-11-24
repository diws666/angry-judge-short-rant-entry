import os

RANT_TEXT = (
    "The office printer has one job. It prints fine all morning, "
    "then the moment my deadline arrives it jams, flashes a light I "
    "have never seen before, and demands a cartridge that costs more "
    "than the printer."
)

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def rant_text() -> str:
    """The short rant submitted to the Angry Judge bounty."""
    return RANT_TEXT


def write_entry(path: str, text: str) -> None:
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    write_entry(OUT_PATH, rant_text())


if __name__ == "__main__":
    main()
