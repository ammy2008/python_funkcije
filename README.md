# Interaktivni program za izračun in prikaz matematičnih funkcij

**Avtorji:** Amadeja Roškarič, Lan Pušič  
**Datum:** 20. oktober 2025

---

## 1. Opis projekta

Projekt predstavlja **interaktivni Python program**, ki uporabniku omogoča izračun in vizualizacijo osnovnih matematičnih funkcij.

Uporabnik izbere funkcijo, določi interval, korak in po potrebi dodatne parametre. Program nato:

- izračuna vrednosti izbrane funkcije,
- preveri domeno funkcije in veljavnost vhodnih podatkov,
- shrani rezultate v CSV datoteko,
- izriše graf funkcije z možnostjo označevanja posameznih točk.

Projekt je razdeljen na tri glavne module:

- `main.py` – glavni interaktivni program,
- `funkcije.py` – definicije matematičnih funkcij,
- `izris.py` – risanje grafov s knjižnico Matplotlib.

## 2. Zahteve in namestitev

Za delovanje programa potrebujete **Python 3.8 ali novejši**.

Program uporablja knjižnici NumPy in Matplotlib. Namestite ju z ukazom:

```bash
pip install numpy matplotlib
```

## 3. Struktura projekta

```text
projekt_funkcije/
├── main.py
├── funkcije.py
├── izris.py
├── rezultati.csv
└── README.md
```

- `main.py` – glavni program
- `funkcije.py` – matematične funkcije
- `izris.py` – izris grafov
- `rezultati.csv` – datoteka z rezultati
- `README.md` – dokumentacija projekta

Datoteka `rezultati.csv` se ustvari oziroma uporabi med izvajanjem programa.

## 4. Zagon programa

V terminalu se pomaknite v mapo projekta in zaženite:

```bash
python main.py
```

## 5. Potek uporabe

### 5.1. Izbira funkcije

Ob zagonu se prikaže tabela razpoložljivih matematičnih funkcij.

```text
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
```

Uporabnik vnese številko izbrane funkcije od 1 do 10.

### 5.2. Vnos parametrov

Pri izbiri linearne funkcije mora uporabnik vnesti tudi naklon `k`.

Nato določi:

- spodnjo mejo intervala `x_min`,
- zgornjo mejo intervala `x_max`,
- korak izračuna.

### 5.3. Preverjanje domene

Program preverja veljavnost vhodnih podatkov in upošteva domeno izbrane funkcije.

Primeri:

- **Koren:** `x >= 0`
- **Logaritem:** `x > 0`
- **Tangens:** program opozori na asimptote, kjer funkcija ni definirana.

### 5.4. Označevanje točk

Uporabnik lahko izbere samodejno označevanje točk na grafu ter določi njihovo število oziroma razmik med izbranimi točkami.

### 5.5. Shranjevanje in prikaz rezultatov

Program shrani izračunane vrednosti v datoteko `rezultati.csv` in prikaže graf izbrane funkcije v novem oknu.

## 6. Izhodna datoteka

Datoteka `rezultati.csv` vsebuje dva stolpca:

- `x` – vhodne vrednosti,
- `y` – pripadajoče vrednosti funkcije.

Primer vsebine:

```csv
x,y
0.0,0.0
0.1,0.01
0.2,0.04
```

Dejanske vrednosti so odvisne od izbrane funkcije, intervala, koraka in dodatnih parametrov.

## 7. Opis modulov

### 7.1. Modul `funkcije.py`

Modul vsebuje definicije matematičnih funkcij, implementiranih z uporabo knjižnice NumPy.

```python
import numpy as np


def linearna(x, k=1):
    return k * x


def kvadratna(x):
    return x**2


def kubicna(x):
    return x**3


def koren(x):
    return np.sqrt(x)


def absolutna(x):
    return np.abs(x)


def sinus(x):
    return np.sin(x)


def kosinus(x):
    return np.cos(x)


def eksponentna(x):
    return np.exp(x)


def logaritemska(x):
    return np.log(x)


def tangens(x):
    return np.tan(x)
```

### 7.2. Modul `izris.py`

Modul skrbi za grafični prikaz funkcije z uporabo knjižnice Matplotlib. Omogoča izris krivulje, prikaz naslovov in mreže ter označevanje izbranih točk z njihovimi koordinatami.

```python
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
            plt.text(
                xi,
                yi,
                f"({xi:.2f}, {yi:.2f})",
                fontsize=8,
                color="red",
                ha="left",
            )

    plt.show()
```

Označene točke so prikazane z rdečo barvo, ob njih pa so izpisane koordinate.

### 7.3. Modul `main.py`

Modul `main.py` povezuje ostale module. Skrbi za interakcijo z uporabnikom, izbiro funkcije, vnos parametrov, preverjanje podatkov, izračun vrednosti, shranjevanje rezultatov in prikaz grafa.

## 8. Primer uporabe

Primer izvajanja programa za linearno funkcijo `y = 2x`:

```text
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
```

Program izračuna vrednosti linearne funkcije, shrani rezultate v datoteko `rezultati.csv` in prikaže graf funkcije `y = 2x` z označenimi točkami.

## 9. Možne nadgradnje

Program bi bilo mogoče nadgraditi z naslednjimi funkcionalnostmi:

- dodajanje novih funkcij, na primer `y = 1/x`, `y = log10(x)` in `y = sin(x)/x`,
- možnost sočasnega izrisa več funkcij,
- samodejno zaznavanje in označevanje ekstremov,
- uporaba knjižnice `argparse` za zagon brez interaktivnega vnosa,
- izdelava grafičnega uporabniškega vmesnika (GUI) s knjižnico Tkinter ali PyQt.

## 10. Zaključek

Projekt **Interaktivni program za izračun in prikaz matematičnih funkcij** je namenjen učnim in raziskovalnim namenom.

Omogoča enostavno vizualizacijo matematičnih funkcij, razumevanje njihovih domen in prikaz obnašanja različnih matematičnih modelov. Zaradi modularne zasnove je primeren tudi za nadaljnje razširitve in dodajanje novih funkcionalnosti.
