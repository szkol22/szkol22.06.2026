# notatki - pakiety i importy w pythonie
# plus dziala to wszystko na przykladzie z tego folderu

# najpierw jak to wyglada:
# pakiety/
#   main.py - glowny plik, odpalamy wlasnie jego
#   pomocnik.py - zwykly modul lezacy obok main.py
#   wytlumaczenie.py - to co teraz czytasz
#   podpakiet/ - to jest pakiet bo ma w srodku __init__.py
#       __init__.py
#       dluga_nazwa.py - tu sa funkcje

# szybko o pojeciach:
# modul = jeden plik .py
# pakiet = folder ktory ma plik __init__.py w srodku
# import = bierzemy kod z innego pliku zeby go uzyc u siebie


# 1) import z tego samego folderu
# main.py i pomocnik.py sa obok siebie wiec wystarczy sama nazwa (bez .py)
#
#   import pomocnik                     # caly modul, pozniej np pomocnik.powitanie(...)
#   from pomocnik import dodaj, WERSJA  # albo tylko to czego akurat chce
#
# obie wersje dzialaja, kwestia gustu.


# 2) import z modulu w podpakiecie
# dluga_nazwa.py jest schowane w folderze podpakiet. sciezke piszemy z kropka
# czyli pakiet.modul:
#
#   from podpakiet.dluga_nazwa import pole_kola
#
# albo caly modul na raz:
#   import podpakiet.dluga_nazwa
#   podpakiet.dluga_nazwa.pole_kola(2)


# 3) skracanie importow przez __init__.py
# ciagle pisanie "from podpakiet.dluga_nazwa import ..." jest zbyt długie.
# w pliku podpakiet/__init__.py mozan wyciagnac te funkcje wyzej, na poziom
# calego pakietu:
#
#   from .dluga_nazwa import pole_prostokata, pole_kola, silnia
#   from . import dluga_nazwa as krotka_nazwa
#
# ta kropka w ".dluga_nazwa" oznacza po prostu "z tego samego pakietu".
#
# i teraz w main.py jest krocej:
#   from podpakiet import pole_prostokata    # bez dlugiej sciezki
#   from podpakiet import krotka_nazwa       # alias na ten dlugi modul
#   krotka_nazwa.silnia(5)
#
# uwaga: kod z __init__.py odpala sie tylko raz przy pierwszym imporcie pakietu,
# dlatego widac w konsoli ten komunikat [podpakiet] __init__.py zostal zaladowany


# jak odpalic
# wchodzimy do folderu pakiety i piszemy:
#   python main.py
#
# powinno wyjsc cos w stylu:
#   [podpakiet] __init__.py zostal zaladowany
#   === IMPORT 1: ten sam folder (pomocnik.py) ===
#   Czesc, Damian! ...
#   2 + 3 = 5
#   ...


# na co uwazac:
# - main.py odpalamy z folderu pakiety, NIE z wnetrza podpakiet, bo inaczej
#   python nie widzi pakietu podpakiet
# - to if __name__ == "__main__" w main.py robi tyle, ze main() odpala sie
#   tylko jak uruchamiamy plik wprost, a nie gdy ktos go sobie zaimportuje
# - kazdy folder ktory ma byc pakietem powinien miec __init__.py, no i tutaj
#   jest on dodatkowo potrzebny wlasnie do tego skracania importow
