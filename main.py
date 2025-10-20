# ===============================
# Glavni program: main.py
# Avtorja: Amadeja Roškarič, Lan Pušič
# Datum: 17. 10. 2025
# Opis: Interaktivni program za izračun in prikaz matematičnih funkcij
# ===============================

import numpy as np
import csv
from funkcije import *
from izris import narisiGraf

funkcije = [
    ("1", "Linearna: y = k*x", linearna),
    ("2", "Kvadratna: y = x²", kvadratna),
    ("3", "Kubična: y = x³", kubicna),
    ("4", "Koren: y = √x", koren),
    ("5", "Absolutna vrednost: y = |x|", absolutna),
    ("6", "Sinus: y = sin(x)", sinus),
    ("7", "Kosinus: y = cos(x)", kosinus),
    ("8", "Eksponentna: y = eˣ", eksponentna),
    ("9", "Logaritemska: y = ln(x)", logaritemska),
    ("10", "Tangens: y = tan(x)", tangens)
]


# === Funkcije za varen vnos z možnostjo izhoda ===
def varnoVnesiFloat(poziv, privzeta):
    while True:
        vnos = input(f"{poziv} [privzeto {privzeta}, 'q' za izhod]: ").strip()
        if vnos.lower() in ["q", "exit"]:
            print("Prekinjanje programa...")
            exit()
        if not vnos:
            return privzeta
        try:
            return float(vnos)
        except ValueError:
            print("Napaka: vnesi številsko vrednost.")


def varnoVnesiPozitivenFloat(poziv, privzeta):
    while True:
        vrednost = varnoVnesiFloat(poziv, privzeta)
        if vrednost > 0:
            return vrednost
        print("Korak mora biti pozitivno število.")


def varnoVnesiInt(poziv, privzeta):
    while True:
        vnos = input(f"{poziv} [privzeto {privzeta}, 'q' za izhod]: ").strip()
        if vnos.lower() in ["q", "exit"]:
            print("Prekinjanje programa...")
            exit()
        if not vnos:
            return privzeta
        try:
            return int(vnos)
        except ValueError:
            print("Napaka: vnesi celo število.")


def varnoDaNe(poziv, privzeto="da"):
    while True:
        vnos = input(f"{poziv} (DA/ne, 'q' za izhod): ").strip().lower()
        if vnos in ["q", "exit"]:
            print("Prekinjanje programa...")
            exit()
        if vnos == "":
            return privzeto
        if vnos in ["da", "ne"]:
            return vnos
        print("Vnesi 'da' ali 'ne'.")


# === Glavna funkcija za izris grafa ===
def izrisPrograma():
    """Interaktivni izris funkcij z označevanjem točk in shranjevanjem rezultatov."""
    print("=== TABELA FUNKCIJ ===")
    for idf, ime, _ in funkcije:
        print(f"{idf}. {ime}")

    # Izbira funkcije
    izbira = None
    while izbira not in [f[0] for f in funkcije]:
        izbira = input("\nVnesi številko funkcije (1–10): ").strip()
        if izbira not in [f[0] for f in funkcije]:
            print("Napačna izbira. Poskusi znova.")

    izbrana = [f for f in funkcije if f[0] == izbira][0]
    naziv, funkcija = izbrana[1], izbrana[2]

    # Parametri funkcije
    parametri = {}
    if izbira == "1":
        parametri["k"] = varnoVnesiFloat("Vnesi naklon (k)", 2)

    # Privzeti intervali glede na domeno funkcije
    privzetiMin, privzetiMax = {
        "4": (0, 10),       # koren
        "9": (0.1, 10)      # logaritem
    }.get(izbira, (-10, 10))

    # Interval z validacijo
    while True:
        xMin = varnoVnesiFloat("Od x", privzetiMin)
        xMax = varnoVnesiFloat("Do x", privzetiMax)

        if izbira == "4" and xMin < 0:
            print(f"Koren je definiran samo za x ≥ 0. Popravek: xMin = 0 namesto {xMin}.")
            xMin = 0
        if izbira == "9" and xMin <= 0:
            print(f"Logaritem je definiran samo za x > 0. Popravek: xMin = 0.1 namesto {xMin}.")
            xMin = 0.1
        if xMin > xMax:
            print("Začetna vrednost ne sme biti večja od končne. Poskusi znova.")
            continue
        break

    korak = varnoVnesiPozitivenFloat("Vnesi korak", 0.1)

    # Opozorila za posebne funkcije
    if izbira == "10":
        print("Tangens ima navpične asimptote pri π/2 + nπ.")
    elif izbira == "8" and xMax > 10:
        print("Eksponentna funkcija hitro raste, graf lahko postane težko berljiv.")

    # Izračun funkcije
    x = np.arange(xMin, xMax + korak, korak)
    try:
        y = funkcija(x, **parametri) if parametri else funkcija(x)
    except Exception as e:
        print(f"Napaka pri izračunu: {e}")
        return

    # Odstranitev neskončnih vrednosti (asimptote)
    maska = np.isfinite(y)
    if izbira == "10":
        asimptote = np.isclose(np.cos(x), 0, atol=1e-12)
        maska &= ~asimptote
    x, y = x[maska], y[maska]

    # Označevanje točk
    oznaci = varnoDaNe("Želiš samodejno označiti nekaj točk na grafu?", "da")
    izbraneTocke = []
    if oznaci == "da":
        stTock = varnoVnesiInt("Koliko točk želiš prikazati", 10)
        gostota = varnoVnesiInt("Vsako koliko točk naj se izbere", 10)
        if stTock > 0 and gostota > 0:
            indeksi = list(range(0, len(x), gostota))[:stTock]
            izbraneTocke = [(x[i], y[i]) for i in indeksi if i < len(x)]

    # Shranjevanje rezultatov
    with open("rezultati.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y"])
        writer.writerows(zip(x, y))

    print("Rezultati shranjeni v 'rezultati.csv'.")
    narisiGraf(x, y, naziv, tocke=izbraneTocke)


# === Glavna zanka programa ===
def main():
    """Zanka programa, ki omogoča večkratni izris grafov."""
    while True:
        izrisPrograma()
        ponovi = varnoDaNe("\nŽeliš narisati nov graf od začetka?", "da")
        if ponovi == "ne":
            print("Program zaključen. Hvala za uporabo programa :)")
            break


if __name__ == "__main__":
    main()