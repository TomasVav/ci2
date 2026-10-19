
import argparse
import re


class Texter:
    def __init__(self, filename):
        self.filename = filename

    def run(self):
        total_lines = 0
        sed_lines = 0

        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                total_lines += 1

                if re.search(r"\bsed\b", line, re.IGNORECASE):
                    sed_lines += 1

        print(f"Total number of lines: {total_lines}")
        print(f"Lines containing 'sed': {sed_lines}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Count lines and lines containing the word 'sed'."
    )
    parser.add_argument("filename", help="Path to the text file")
    args = parser.parse_args()

    texter = Texter(args.filename)
    texter.run()
