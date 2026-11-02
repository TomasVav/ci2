# A04 – World SQLite database

This assignment imports CSV files from `world.zip` into the SQLite database `db.sqlite` and answers question 2: **What is the total population of Southern Europe?**

## Clone the repository

```bash
git clone https://github.com/TomasVav/ci2.git
cd ci2/A04
```

## Run the script

Requires Python 3 (no external packages). Run from the `A04` directory:

```bash
py db.py city.csv country.csv countrylanguage.csv
```

The script creates `db.sqlite`, creates tables for the requested CSV files if absent, imports their records, and prints the question and answer. Further runs skip existing tables. To ask the question using the existing database, run:

```bash
py db.py
```

To create just the table needed for question 2, use `py db.py country.csv`. The CSV files in this folder use semicolons as separators. Keep `world.zip` in the same directory as `db.py` when importing tables.

