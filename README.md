# Interaktivni program za izračun in prikaz matematičnih funkcij

**Avtorji:** Amadeja Roškarič, Lan Pušič  
**Datum:** 20. oktober 2025  

---

## Opis projekta

Ta projekt je **interaktivni Python program**, ki uporabniku omogoča izračun in **vizualizacijo osnovnih matematičnih funkcij**.  
Uporabnik izbere funkcijo, določi interval, korak in (po potrebi) dodatne parametre, program pa nato:

- izračuna vrednosti funkcije,
- preveri domeno in veljavnost vhodnih podatkov,
- rezultate shrani v **CSV datoteko**,
- izriše graf funkcije z možnostjo **označevanja posameznih točk**.

Projekt je razdeljen v tri module:  
- `main.py` → glavni interaktivni program  
- `funkcije.py` → matematične funkcije  
- `izris.py` → risanje grafov s knjižnico Matplotlib  

---

## Struktura projekta

projekt_funkcije/

│

├── main.py # Glavni program

├── funkcije.py # Definicije matematičnih funkcij

├── izris.py # Funkcija za izris grafa

├── rezultati.csv # Samodejno ustvarjena datoteka z rezultati (ob zagonu)

└── README.md # Dokumentacija projekta

---

## Namestitev in zahteve

Program deluje z **Python 3.8+**.  
Pred uporabo je potrebno namestiti naslednji knjižnici:

```bash
pip install numpy matplotlib

Zagon programa

V terminalu se postavite v mapo projekta in zaženite:
    python main.py

Potek uporabe
    1. Ob zagonu se prikaže tabela funkcij:
        === TABELA FUNKCIJ ===
            1. Linearna: y = k*x
            2. Kvadratna: y = x²
            3. Kubična: y = x³
            4. Koren: y = √x
            5. Absolutna vrednost: y = |x|
            6. Sinus: y = sin(x)
            7. Kosinus: y = cos(x)
            8. Eksponentna: y = eˣ
            9. Logaritemska: y = ln(x)
            10. Tangens: y = tan(x)
        Uporabnik vnese številko funkcije (1–10).

    2. Če izbere linearna funkcija, mora vnesti naklon k.
    3. Nato vnese interval (x_min, x_max) in korak.
    4. Program preveri domeno funkcije (npr. √x ≥ 0, ln(x) > 0, opozori na asimptote pri tan(x)).
    5. Po želji označi nekaj točk na grafu (za preglednost).
    6. Rezultati se shranijo v rezultati.csv.
    7. Program nariše graf funkcije v novem oknu.

Izhodna datoteka
    Rezultati se samodejno shranijo v datoteko rezultati.csv, ki vsebuje dva stolpca:
        x,y
        0.0,0.0
        0.1,0.01
        0.2,0.04
        ...

Modul: funkcije.py
    Vsebuje definicije matematičnih funkcij, implementiranih z uporabo knjižnice NumPy:
        def linearna(x, k=1): return k * x
        def kvadratna(x): return x**2
        def kubicna(x): return x**3
        def koren(x): return np.sqrt(x)
        def absolutna(x): return np.abs(x)
        def sinus(x): return np.sin(x)
        def kosinus(x): return np.cos(x)
        def eksponentna(x): return np.exp(x)
        def logaritemska(x): return np.log(x)
        def tangens(x): return np.tan(x)

Modul: izris.py
    Skrbi za grafični prikaz funkcije z uporabo knjižnice Matplotlib.
        import matplotlib.pyplot as plt

        def narisi_graf(x, y, naziv, tocke=None):
            plt.figure(figsize=(8, 5))
            plt.plot(x, y, label=naziv)
            plt.title(naziv)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.grid(True)
            plt.legend()

            if tocke:
                for (xi, yi) in tocke:
                    plt.scatter(xi, yi, color="red", zorder=5)
                    plt.text(xi, yi, f"({xi:.2f}, {yi:.2f})", fontsize=8, color="red", ha="left")

            plt.show()
    # Označene točke se izrišejo v rdeči barvi in z oznakami koordinat.

Primer uporabe
    === TABELA FUNKCIJ ===
        1. Linearna: y = k*x
        ...

        Vnesi številko funkcije, ki jo želiš uporabiti (1–10): 1
        Vnesi naklon (k): 2
        Od x: -5
        Do x: 5
        Vnesi korak (npr. 0.1): 0.5
        Želiš samodejno označiti nekaj točk na grafu? (da/ne): da
        Koliko točk želiš prikazati: 3
        Vsako koliko točk naj se izbere (npr. 10): 4
        # Rezultati se shranijo v rezultati.csv
        # Graf funkcije y = 2x se izriše z označenimi točkami.

Možne nadgradnje
    Dodajanje novih funkcij (npr. y = 1/x, y = log₁₀(x), y = sin(x)/x)
    Možnost izrisa več funkcij hkrati
    Samodejno zaznavanje in označevanje ekstremov
    Uporaba argparse za zagon brez interaktivnega vnosa
    Grafični uporabniški vmesnik (GUI) s knjižnicami tkinter ali PyQt

Zaključek
    Projekt Interaktivni izračun in izris funkcij je namenjen učnim in raziskovalnim namenom.
    Omogoča enostavno vizualizacijo funkcij, razumevanje domen in prikaz obnašanja različnih matematičnih modelov.