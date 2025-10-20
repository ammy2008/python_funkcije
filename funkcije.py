# ===============================
# Modul: funkcije.py
# Avtor: Amadeja Roškarič, Lan Pušič
# Datum: 15. 10. 2025
# Opis: Matematične funkcije za izračun in risanje grafov
# ===============================

import numpy as np

def linearna(x, k=1):
    """Linearna funkcija y = k*x"""
    return k * x

def kvadratna(x):
    """Kvadratna funkcija y = x^2"""
    return x**2

def kubicna(x):
    """Kubična funkcija y = x^3"""
    return x**3

def koren(x):
    """Koren funkcija y = sqrt(x), x >= 0"""
    return np.sqrt(x)

def absolutna(x):
    """Absolutna vrednost y = |x|"""
    return np.abs(x)

def sinus(x):
    """Sinus funkcija y = sin(x)"""
    return np.sin(x)

def kosinus(x):
    """Kosinus funkcija y = cos(x)"""
    return np.cos(x)

def eksponentna(x):
    """Eksponentna funkcija y = exp(x)"""
    return np.exp(x)

def logaritemska(x):
    """Naravni logaritem y = ln(x), x > 0"""
    return np.log(x)

def tangens(x):
    """Tangens funkcija y = tan(x)"""
    return np.tan(x)