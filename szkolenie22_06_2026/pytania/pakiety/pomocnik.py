# pomocnik.py
# Moduł leżący w TYM SAMYM folderze co main.py.
# main.py zaimportuje go bezpośrednio po nazwie (bez kropek, bez podpakietu).

def powitanie(imie):
    """Zwraca prosty tekst powitania."""
    return f"Czesc, {imie}! (z modulu pomocnik.py)"


def dodaj(a, b):
    """Sumuje dwie liczby."""
    return a + b


# Zmienna na poziomie modułu - też da się ją zaimportować.
WERSJA = "1.0"
