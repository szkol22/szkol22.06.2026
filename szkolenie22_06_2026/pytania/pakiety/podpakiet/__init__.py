# podpakiet/__init__.py
#
# Ten plik sprawia, ze folder "podpakiet" jest PAKIETEM Pythona.
# Kod tutaj wykonuje sie raz, przy pierwszym imporcie pakietu.
#
# Glowna sztuczka: w __init__.py mozemy "wyciagnac" rzeczy z dlugiego modulu
# na poziom calego pakietu. Dzieki temu zamiast pisac:
#
#     from podpakiet.dluga_nazwa import pole_prostokata
#
# wystarczy krotsze:
#
#     from podpakiet import pole_prostokata

# 1) Wciagamy konkretne funkcje na poziom pakietu (skracamy sciezke importu).
from .dluga_nazwa import pole_prostokata, pole_kola, silnia

# 2) Dajemy dlugiemu modulowi krotki alias "krotka_nazwa".
#    Dzieki temu mozna pisac:  from podpakiet import krotka_nazwa
#    i wolac krotka_nazwa.silnia(5) zamiast podpakiet.dluga_nazwa.silnia(5)
from . import dluga_nazwa as krotka_nazwa

# 3) __all__ kontroluje, co trafia przy "from podpakiet import *".
__all__ = ["pole_prostokata", "pole_kola", "silnia", "krotka_nazwa"]

print("[podpakiet] __init__.py zostal zaladowany")
