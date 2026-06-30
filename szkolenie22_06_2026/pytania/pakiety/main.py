# main.py
# GLOWNY plik programu - tutaj startuje wykonanie.
# Uruchamiasz go z folderu "pakiety":   python main.py

# ---------------------------------------------------------------------------
# IMPORT 1: z modulu lezacego w TYM SAMYM folderze (pomocnik.py)
# ---------------------------------------------------------------------------
import pomocnik                          # caly modul
from pomocnik import dodaj, WERSJA       # tylko wybrane rzeczy

# ---------------------------------------------------------------------------
# IMPORT 2: z modulu w podpakiecie (podpakiet/dluga_nazwa.py)
# Pelna, dluga sciezka:
# ---------------------------------------------------------------------------
from podpakiet.dluga_nazwa import pole_kola

# ---------------------------------------------------------------------------
# IMPORT 3: SKROCONY dzieki __init__.py w podpakiecie
#   - funkcje wyciagniete na poziom pakietu
#   - oraz krotki alias "krotka_nazwa" na modul "dluga_nazwa"
# ---------------------------------------------------------------------------
from podpakiet import pole_prostokata, krotka_nazwa


def main():
    print("=== IMPORT 1: ten sam folder (pomocnik.py) ===")
    print(pomocnik.powitanie("Przemek"))      # uzycie przez nazwe modulu
    print("2 + 3 =", dodaj(2, 3))             # uzycie zaimportowanej funkcji
    print("Wersja pomocnika:", WERSJA)

    print("\n=== IMPORT 2: pelna sciezka do podpakietu ===")
    print("Pole kola (r=2):", round(pole_kola(2), 4))

    print("\n=== IMPORT 3: skrocony import dzieki __init__.py ===")
    print("Pole prostokata 4x5:", pole_prostokata(4, 5))
    print("Silnia 5 (przez alias krotka_nazwa):", krotka_nazwa.silnia(5))


# Ten warunek sprawia, ze main() odpala sie tylko gdy uruchamiamy plik
# bezposrednio (python main.py), a NIE gdy ktos go zaimportuje.
if __name__ == "__main__":
    main()
