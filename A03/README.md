\# A03 - Molbase Parser



This script extracts compound names from an HTML file containing Molbase search results using BeautifulSoup.



\## Clone the repository



```bash

git clone https://github.com/TomasVav/ci2.git

cd ci2/A03

```



\## Create a virtual environment



```powershell

py -m venv .venv

```



\## Install required packages



```powershell

.\\.venv\\Scripts\\python.exe -m pip install beautifulsoup4

```



\## Run the script



```powershell

.\\.venv\\Scripts\\python.exe molbase\_parser.py molbase\_benzidine.html

```



The script prints the compound names, one per line.

