import requests
from flask import Flask, render_template, request

app = Flask(__name__)


def search_compound(smiles):
    url = "https://www.ebi.ac.uk/chembl/api/data/molecule.json"

    params = {
        "molecule_structures__canonical_smiles__connectivity": smiles,
        "limit": 1
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()
    molecules = data["molecules"]

    if molecules:
        return molecules[0]

    return None


@app.route("/", methods=["GET", "POST"])
def index():
    compound = None
    smiles = ""
    error = None

    if request.method == "POST":
        smiles = request.form["smiles"].strip()

        try:
            compound = search_compound(smiles)

            if compound is None:
                error = "Compound not found."

        except requests.RequestException:
            error = "Unable to connect to ChEMBL."

    return render_template(
        "index.html",
        compound=compound,
        smiles=smiles,
        error=error
    )


if __name__ == "__main__":
    app.run()