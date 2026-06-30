"""
atrybut klasowy vs atrybut w __init__

= (przypisanie) zawsze tworzy/nadpisuje atrybut tylko na jednej instancji
i nigdy nie zmienia wartosci dla wszystkich.
Wspoldzielenie ("zmiana dla wszystkich") widac dopiero przy mutacji
(.append, [i]=, .update) i tylko dla mutowalnych (lista, dict, set).
"""


# ===========================================================
# 1. dwa miejsca gdzie nadajesz wartosc
# ===========================================================

class Przyklad:
    atrybut_klasowy = 'wartosc'        # 1) w ciele klasy --> jeden obiekt, wspolny dla wszystkich instancji

    def __init__(self):
        self.atrybut_instancji = 'wartosc'   # 2) w __init__ --> nowy obiekt przy kazdym tworzeniu, osobny

# - atrybut klasowy   --> istnieje raz, nalezy do klasy. Wszystkie instancje patrza na ten sam.
# - atrybut instancji --> tworzony od nowa przy kazdym __init__, kazdy obiekt ma swoj.


# ===========================================================
# 2. model "etykietek i pudelek"
# ===========================================================
# Zmienna / atrybut = etykietka naklejona na pudelko (obiekt w pamieci).
#
#    k1.x --> ['stary']      jedno pudelko (atrybut klasy)
#    k2.x --> ['stary']
#
# operacja = (przypisanie / rebinding): nie zmienia zawartosci pudelka,
# przekleja etykietke k1 na inne pudelko:
#
#    k1.x --> ['nowy']     nowe pudelko, tylko k1
#    k2.x --> ['stary']    stare pudelko (klasowe) - k2 nadal tu wisi
#
# --> Dlatego po = na k1 obiekt k2 ma stara wartosc. Zawsze. Niezaleznie od typu.

class K:
    x = 'stary'

k1, k2 = K(), K()
k1.x = 'nowy'
print(k1.x)   # nowy
print(k2.x)   # stary   <- inaczej sie nie da

# operacja mutacji (.append, [i]=, .update):
#    k1.x.append('X')   # nie przeklejam etykietki - otwieram wspolne pudelko i grzebie w srodku
#    k1.x --> ['stary', 'X']    to samo pudelko - k2 tez widzi 'X'
#    k2.x --> ['stary', 'X']
# Etykietki sie nie ruszyly, obie wisza na jednym pudelku --> zmiana widocza u wszystkich.


# ===========================================================
# 3. dlaczego przy stringu nigdy nie zobaczysz wspoldzielenia
# ===========================================================
# String jest niemutowalny. Nie istnieje s.append(), nie zrobisz s[0]='x'.
# Jedyne co mozesz to s = 'nowy', czyli =, czyli rebinding, czyli tylko jedna instancja.
# Przy stringu (i kazdym immutable: int, float, bool, tuple, str)
# fizycznie nie ma operacji, ktora zmienilaby wartosc dla wszystkich.

class K:
    x = 'stary'

k1, k2 = K(), K()
k1.x = 'nowy'
print(k1.x)   # nowy
print(k2.x)   # stary   <- inaczej sie nie da

# czyli krotko:
# - k1.x = ...        (przypisanie) --> nowy atrybut tylko na k1, przykrywa klasowy. Tak samo string i lista.
# - k1.x.append(...)  (mutacja)     --> dla stringa nie istnieje; dla listy/dicta rusza wspolne pudelko (k1 i k2).


# ===========================================================
# 4. pulapka mutowalnego atrybutu klasowego
# ===========================================================

class Koszyk:
    produkty = []          # zle: jedna lista dla wszystkich koszykow

    def dodaj(self, x):
        self.produkty.append(x)

a, b = Koszyk(), Koszyk()
a.dodaj('jablko')
print(b.produkty)   # ['jablko']  <- b widzi produkt a!

# poprawnie - osobna lista na instancje, w __init__:

class Koszyk:
    def __init__(self):
        self.produkty = []     # ok: kazdy koszyk ma swoja liste

    def dodaj(self, x):
        self.produkty.append(x)


# ===========================================================
# kiedy ktory wybrac
# ===========================================================

# --- atrybut klasowy - gdy wartosc ma byc wspolna dla wszystkich ---

# licznik utworzonych obiektow:
class Uzytkownik:
    liczba_uzytkownikow = 0          # wspolny licznik dla calej klasy

    def __init__(self, imie):
        self.imie = imie             # osobne dla kazdego
        Uzytkownik.liczba_uzytkownikow += 1

u1 = Uzytkownik("Ala")
u2 = Uzytkownik("Bob")
print(Uzytkownik.liczba_uzytkownikow)   # 2

# wspolny rejestr / lista wszystkich instancji:
class Zamowienie:
    wszystkie = []                   # jedna wspolna lista - to celowe

    def __init__(self, numer):
        self.numer = numer
        Zamowienie.wszystkie.append(self)   # mutacja wspolnego pudelka

Zamowienie(101)
Zamowienie(102)
print([z.numer for z in Zamowienie.wszystkie])   # [101, 102]

# stala / konfiguracja wspolna dla calej klasy (niemutowalna):
class KontoBankowe:
    WALUTA = 'PLN'                   # stala - kazde konto domyslnie PLN
    OPROCENTOWANIE = 0.05            # wspolna stawka

    def __init__(self, wlasciciel):
        self.wlasciciel = wlasciciel
        self.saldo = 0               # osobne dla kazdego konta

k = KontoBankowe("Ala")
print(k.WALUTA)                      # PLN  (czytasz wspolna stala)

# stale pisze sie wielkimi literami, sa niemutowalne -> bezpieczne jako klasowe.


# --- atrybut w __init__ - gdy kazdy obiekt ma miec swoje dane ---

# dane konkretnego obiektu (to jest 90% przypadkow):
class KontoBankowe:
    def __init__(self, imie, nazwisko='Kowalski'):
        self.imie = imie
        self.nazwisko = nazwisko     # default moze zalezec od argumentu
        self.saldo = 0               # kazde konto startuje od wlasnego 0
        self.historia = []           # kazde konto ma wlasna liste transakcji

    def wplata(self, kwota):
        self.saldo += kwota
        self.historia.append(('wplata', kwota))

k1 = KontoBankowe("Alicja", "Nowak")
k2 = KontoBankowe("Damian")          # nazwisko = 'Kowalski' (default z argumentu)

k1.wplata(100)
print(k1.saldo, k1.historia)         # 100 [('wplata', 100)]
print(k2.saldo, k2.historia)         # 0 []   <- Damian nie widzi wplaty Alicji

# To jest poprawiona wersja mojego KontoBankowe. Gdyby historia byla atrybutem
# klasowym, Damian widzialby transakcje Alicji - czyli bug.

# kazdy obiekt z wlasna mutowalna struktura:
class Gracz:
    def __init__(self, nick):
        self.nick = nick
        self.ekwipunek = []          # wlasny plecak kazdego gracza
        self.statystyki = {'hp': 100, 'mana': 50}   # wlasny dict

g1 = Gracz("Wojownik")
g2 = Gracz("Mag")
g1.ekwipunek.append("miecz")
print(g1.ekwipunek)   # ['miecz']
print(g2.ekwipunek)   # []   <- osobne plecaki


# --- stala klasowa jako domyslny argument (taki miks) ---
class KontoBankowe:
    DOMYSLNA_WALUTA = 'PLN'          # stala klasowa (zeby default byl w 1 miejscu)

    def __init__(self, wlasciciel, waluta=None):
        self.wlasciciel = wlasciciel
        # jesli nie podano - bierzemy domyslna klasowa, ale zapisujemy jako instancyjna
        self.waluta = waluta if waluta is not None else KontoBankowe.DOMYSLNA_WALUTA

k1 = KontoBankowe("Ala")             # waluta = 'PLN'
k2 = KontoBankowe("Bob", "EUR")      # waluta = 'EUR'
print(k1.waluta, k2.waluta)          # PLN EUR

# czyli stala mowi jaki jest default, a dane i tak siedza na obiekcie.


# ===========================================================
# a co z dziedziczeniem
# ===========================================================
# Glowne clue:

class BankAccount:
    atrybut_klasowy = 'kura'         # 1) w ciele klasy

    def __init__(self, gatunek='zwierze'):
        self.gatunek = gatunek       # 2) w __init__

# Oba wygladaja jak wartosc domyslna. Roznica wychodzi dopiero przy podklasie -
# bo zmienia sie gdzie Python szuka wartosci.
#
# obj.x szuka po kolei i bierze pierwsze trafienie:
#    obj  -->  klasa  -->  rodzic  -->  object
#
# - self.gatunek    - lezy na instancji, znajdzie od razu.
# - atrybut_klasowy - na instancji go nie ma, wiec idzie do klasy, a jak trzeba to do
#   rodzica. Dlatego dziedziczy sie sam.

# atrybut klasowy nadpisujesz jedna linijka:
class BankAccount:
    WALUTA = 'PLN'

    def __init__(self, wlasciciel):
        self.wlasciciel = wlasciciel

class KontoEuro(BankAccount):
    WALUTA = 'EUR'                   # nadpisanie - jedna linijka

class KontoUkryte(BankAccount):
    pass                            # nic nie pisze - dziedziczy 'PLN'

print(KontoEuro("Bob").WALUTA)      # EUR  (znalazl u siebie, do rodzica nie idzie)
print(KontoUkryte("Ula").WALUTA)    # PLN  (u siebie brak -> bierze z rodzica)

# Nadpisanie w dziecku nie rusza rodzica - BankAccount.WALUTA dalej 'PLN'.

# a atrybut z __init__ musisz przepisac caly __init__:
class BankAccount:
    def __init__(self, waluta='PLN'):
        self.waluta = waluta

class KontoEuro(BankAccount):
    def __init__(self, waluta='EUR'):     # przeslaniasz caly __init__
        super().__init__(waluta)          # i musisz pamietac o super()

# Wiecej pisania i latwo o blad (zapomniany super()). Przy atrybucie klasowym to byla jedna linijka.

# no to kiedy co:
# - decyduje klasa / podklasa (waluta, stawka, limit) --> atrybut klasowy.
# - decyduje konkretny obiekt (saldo, wlasciciel, historia) --> __init__.
