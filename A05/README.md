# A05 – CDXML to HTML Converter

This project contains a Python script `cdx2html.py` that converts chemical structures from CDXML files into PNG images using Open Babel and generates an HTML page displaying the results.

The generated `index.html` contains a table with three columns: filename, formula, and 2D structure.

## Requirements

- Python 3
- Open Babel 3.x
- Git

Open Babel can be downloaded from:
https://github.com/openbabel/openbabel/releases

The Open Babel executable (`obabel`) must be available in the system PATH.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/ci2.git
cd ci2/A05
```

Replace `USERNAME` with the actual GitHub username.

### 2. Create a virtual environment

On Windows (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Python packages

The script uses only Python standard library modules, so no additional Python packages are required.

Open Babel must be installed separately.

Verify the Open Babel installation:

```powershell
obabel -V
```

## Usage

The input CDXML files are located in the `structures` directory.

To process all CDXML files, run:

```powershell
py cdx2html.py "structures/*.cdxml"
```

To process a single file:

```powershell
py cdx2html.py structures/rx00005.cdxml
```

To process multiple selected files:

```powershell
py cdx2html.py structures/rx00005.cdxml structures/rx00153.cdxml
```

The script supports wildcard patterns.

## Output

The script generates:

- `index.html` – an HTML page containing a table of molecular structures.
- `.png` files – images generated from the input CDXML files.

The HTML table contains the following columns:

1. **filename** – the original CDXML filename.
2. **formula** – the molecular formula reported by Open Babel.
3. **2D structure** – the generated PNG image displayed using an HTML `<img>` element.

Open `index.html` in a web browser to view the results.

## Note

Some CDXML structures may contain atoms that Open Babel interprets without implicit hydrogen atoms. This can affect the reported molecular formulas and the appearance of the generated structures.

The script preserves the molecular formulas and images produced by Open Babel.