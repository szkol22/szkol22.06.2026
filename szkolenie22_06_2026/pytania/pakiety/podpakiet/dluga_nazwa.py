# podpakiet/dluga_nazwa.py
# Moduł schowany WEWNATRZ pakietu "podpakiet".
# Celowo ma dluga nazwe pliku, zeby pokazac, jak meczacy bywa pelny import:
#     from podpakiet.dluga_nazwa import pole_prostokata
# W __init__.py pokazemy, jak ten import skrocic.

import math


def pole_prostokata(a, b):
    """Pole prostokata o bokach a i b."""
    return a * b


def pole_kola(promien):
    """Pole kola o danym promieniu."""
    return math.pi * promien ** 2


def silnia(n):
    """Silnia liczby n (n!)."""
    if n < 0:
        raise ValueError("Silnia jest okreslona tylko dla liczb >= 0")
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik
