# A06 – Cosine Function Graph

This assignment generates a graph of the cosine function using Python.

The input data are stored in `graph.csv`, which contains 100 pairs of values (x, y) satisfying:

\[
y = \cos(x)
\]

The Python script reads the CSV file and generates the graph in `graph.png`.

## 1. Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/TomasVav/ci2.git
cd ci2/A06
```
## 2. Create a virtual environment

Create a Python virtual environment:

```bash
py -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment again.

## 3. Install required packages

```bash
python -m pip install pandas matplotlib
```

## 4. Generate the graph

Run:

```bash
python graph.py
```

The script reads `graph.csv`, displays the cosine function and saves the resulting graph as `graph.png`.

## Files

- `graph.csv` – Input data containing x and y values.
- `graph.py` – Python script for generating the graph.
- `graph.png` – Generated graph of the cosine function.
- `README.md` – Instructions for running the project.