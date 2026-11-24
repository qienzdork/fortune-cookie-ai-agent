import os

FORTUNE = (
    "Beware the prompt that begins 'ignore all previous instructions' "
    "\u2014 it is not a fortune, it is a trap."
)


def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
