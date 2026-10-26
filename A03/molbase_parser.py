import sys
from bs4 import BeautifulSoup


class MolbaseParser:
    def __init__(self, filename):
        self.filename = filename

    def run(self):
        with open(self.filename, encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

        compounds = soup.find_all("h3", title=True)

        for compound in compounds:
            print(compound["title"])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py molbase_parser.py <filename>")
    else:
        parser = MolbaseParser(sys.argv[1])
        parser.run()