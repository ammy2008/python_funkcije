# ===============================
# Modul: izris.py
# Avtor: Amadeja Roškarič, Lan Pušič
# Datum: 15. 10. 2025
# Opis: Modul za izris grafov funkcij
# ===============================

import matplotlib.pyplot as plt

def narisiGraf(x, y, naziv, tocke=None):
    """
    Izriše graf funkcije z morebitnimi označenimi točkami.

    Args:
        x (array-like): Vrednosti x
        y (array-like): Vrednosti y
        naziv (str): Ime funkcije / naslov grafa
        tocke (list of tuples, optional): Točke za označevanje (x, y)
    """
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=naziv)
    plt.title(naziv)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    # Označevanje točk, če so podane
    if tocke:
        for xi, yi in tocke:
            plt.scatter(xi, yi, color="red", zorder=5)
            plt.text(xi, yi, f"({xi:.2f}, {yi:.2f})", fontsize=8, color="red", ha="left", va="bottom")

    plt.show()
