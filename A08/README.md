
# A08 – ChEMBL Compound Search

This assignment implements a simple web application using Python and Flask.
The application allows users to search for chemical compounds in the ChEMBL
database by entering their chemical structures in SMILES format.

The application retrieves data using the ChEMBL Web API and displays
information about the first compound found. The search is based on molecular
connectivity and does not distinguish stereochemistry.

## 1. Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/TomasVav/ci2.git
cd ci2/A08
```

## 2. Create a virtual environment

Create a Python virtual environment:

```powershell
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

Then activate the virtual environment again.

## 3. Install required packages

```powershell
python -m pip install -r requirements.txt
```

## 4. Run the application

Start the Flask web server:

```powershell
python app.py
```

Open the following address in a web browser:

http://127.0.0.1:5000

## 5. Using the application

1. Enter a chemical structure in SMILES format.
2. Click the Search button.
3. The application retrieves and displays information about the compound
   from the ChEMBL database.
4. Enter another SMILES string to perform a new search.

If no compound is found, the application displays an error message.
If the compound name is unavailable, the application displays
"Not available".

An internet connection is required to retrieve data from ChEMBL.

## 6. Example output – Malic acid

Input SMILES:

```text
O=C(O)CC(O)C(=O)O
```

Output:

```text
Compound information

Name: Not available
ChEMBL ID: CHEMBL225986
Molecule type: Small molecule
Molecular formula: C4H6O5
Molecular weight: 134.09 g/mol
LogP: -1.09
Hydrogen bond donors: 3
Hydrogen bond acceptors: 3
Canonical SMILES: O=C(O)C[C@@H](O)C(=O)O
```
