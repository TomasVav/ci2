import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Slozka, ve ktere je ulozen tento skript
folder = Path(__file__).resolve().parent

# Nacteni dat z CSV souboru
data = pd.read_csv(folder / "graph.csv")

# Vykresleni grafu
plt.figure(figsize=(9, 5))
plt.plot(data["x"], data["y"], label="y = cos(x)")

# Popisky a uprava grafu
plt.xlabel("x [rad]")
plt.ylabel("y")
plt.title("Graf funkce y = cos(x)")
plt.grid(True)
plt.legend()

# Ulozeni grafu
plt.savefig(folder / "graph.png", dpi=300, bbox_inches="tight")

# Zobrazeni grafu
plt.show()