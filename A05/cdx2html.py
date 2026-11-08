
import sys
import glob
import subprocess
import html
from pathlib import Path


def get_formula(filename):
    """Get the molecular formula using Open Babel."""
    result = subprocess.run(
        ["obabel", str(filename), "-oreport"],
        capture_output=True,
        text=True,
        check=True
    )

    for line in result.stdout.splitlines():
        if line.startswith("FORMULA:"):
            return line.split(":", 1)[1].strip()

    return "Unknown"


def main():
    if len(sys.argv) < 2:
        print("Usage: python cdx2html.py 'structures/*.cdxml'")
        sys.exit(1)

    files = []

    for pattern in sys.argv[1:]:
        files.extend(glob.glob(pattern))

    files = sorted(set(files))

    if not files:
        print("No CDXML files found.")
        sys.exit(1)

    rows = []

    for filename in files:
        path = Path(filename)

        if path.suffix.lower() != ".cdxml":
            continue

        png_path = Path(path.stem + ".png")

        try:
            subprocess.run(
                ["obabel", str(path), "-O", str(png_path)],
                check=True
            )

            formula = get_formula(path)

            rows.append(
                f"<tr>"
                f"<td>{html.escape(path.name)}</td>"
                f"<td>{html.escape(formula)}</td>"
                f'<td><img src="{html.escape(png_path.name)}" '
                f'width="300" alt="2D structure"></td>'
                f"</tr>"
            )

            print(f"Processed: {path.name}")

        except subprocess.CalledProcessError:
            print(f"Error processing: {path.name}")

    page = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Molecular Structures</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #aaa; padding: 10px; }
        th { background-color: #eee; }
        img { max-width: 300px; }
    </style>
</head>
<body>
    <h1>Molecular Structures</h1>
    <table>
        <tr>
            <th>filename</th>
            <th>formula</th>
            <th>2D structure</th>
        </tr>
        %s
    </table>
</body>
</html>
""".replace("%s", "\n".join(rows))

    Path("index.html").write_text(page, encoding="utf-8")

    print("Created index.html")


if __name__ == "__main__":
    main()
