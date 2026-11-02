"""Import selected CSV files from world.zip into an SQLite database."""

import csv
import sqlite3
import sys
import zipfile
from pathlib import Path


class WorldDatabase:
    """Create and query a database populated from the world archive."""

    def __init__(self, arguments):
        self.directory = Path(__file__).resolve().parent
        self.archive_path = self.directory / "world.zip"
        self.database_path = self.directory / "db.sqlite"
        self.filenames = arguments

    def import_csv(self, connection, archive, member_name):
        """Create and populate a table unless it already exists."""
        table_name = Path(member_name).stem
        if not table_name.isidentifier():
            raise ValueError(f"Invalid table name: {table_name}")

        existing = connection.execute(
            "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = ?",
            (table_name,),
        ).fetchone()
        if existing:
            print(f"Table {table_name} already exists; skipping.")
            return

        with archive.open(member_name) as binary_file:
            import io

            with io.TextIOWrapper(binary_file, encoding="utf-8-sig", newline="") as text_file:
                reader = csv.reader(text_file, delimiter=";")
                columns = next(reader, None)
                if not columns or any(not name for name in columns):
                    raise ValueError(f"Missing CSV header in {member_name}")
                if len(columns) != len(set(columns)):
                    raise ValueError(f"Duplicate column names in {member_name}")

                # Double quotes inside SQL identifiers need to be escaped.
                quoted_columns = [f'"{name.replace(chr(34), chr(34) * 2)}"' for name in columns]
                quoted_table = f'"{table_name}"'
                schema = ", ".join(f"{name} TEXT" for name in quoted_columns)
                placeholders = ", ".join("?" for _ in columns)
                connection.execute(f"CREATE TABLE {quoted_table} ({schema})")
                connection.executemany(
                    f"INSERT INTO {quoted_table} VALUES ({placeholders})", reader
                )
                print(f"Imported {member_name} into {table_name}.")

    def answer_question(self, connection):
        """Print the answer to question 2 using the country table."""
        question = "What is the total population of Southern Europe?"
        try:
            result = connection.execute(
                "SELECT SUM(CAST(Population AS INTEGER)) "
                "FROM country WHERE Region = ?",
                ("Southern Europe",),
            ).fetchone()
        except sqlite3.OperationalError:
            print("Missing country table. First run: python db.py country.csv")
            return
        print(question)
        print(result[0] if result and result[0] is not None else "No data")

    def run(self):
        """Load requested files and then execute the assigned query."""
        if not self.filenames and not self.database_path.exists():
            print("Usage: python db.py table1.csv [table2.csv ...]")
            print("First supply CSV filenames from world.zip.")
            return

        with sqlite3.connect(self.database_path) as connection:
            if self.filenames:
                with zipfile.ZipFile(self.archive_path) as archive:
                    available = {
                        Path(name).name: name
                        for name in archive.namelist()
                        if name.lower().endswith(".csv")
                    }
                    for filename in self.filenames:
                        requested = filename if filename.endswith(".csv") else f"{filename}.csv"
                        if requested not in available:
                            raise FileNotFoundError(f"Not found in world.zip: {requested}")
                        with connection:
                            self.import_csv(connection, archive, available[requested])
            self.answer_question(connection)


if __name__ == "__main__":
    WorldDatabase(sys.argv[1:]).run()
