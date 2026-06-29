# WAŻNE: przed uruchomieniem zainstaluj bibliotekę requests --> pip install requests (bez niej sekcja sieciowa nie ruszy)
##################################################################################################
# Importowanie #  Importowanie # Importowanie # Importowanie # Importowanie # Importowanie # Impor
##################################################################################################

# Pierwszy sposób na import math

import math

#--> math to moduł, który zawiera funkcje,stałe (sqrt,pi,ceil(wgore),floor())
print(math.sqrt(5))
print(math.pi)
print(math.ceil(3.2))
print(math.floor(3.8))



# Pierwszy sposób na import math z aliasem

"""
import math as mt

print(mt.sqrt(5))
print(mt.pi)
print(mt.ceil(3.2))
print(mt.floor(3.8))
"""


# Drugi sposób na import math, żeby nie pisać modułu

"""
from math import *

print(sqrt(5))
print(pi)
print(ceil(3.2))
print(floor(3.8))
"""



# Drugi sposób na import math, żeby nie pisać modułu importując tylko co chcemy

"""
from math import sqrt,pi,ceil,floor

print(sqrt(5))
print(pi)
print(ceil(3.2))
print(floor(3.8))
"""


#

"""
def sqrt():
    pass
from math import sqrt as sq

print(sq(5)) # --> uniknąć problemu z nazwą
"""



# https://docs.python.org/3/library/math.html
# https://docs.python.org/3/library/random.html

# help() i dir() -- sprawdzanie zawartości modułu:


"""
import math
print(dir(math))      # lista dostępnych funkcji
help(math.sqrt)       # dokumentacja funkcji
"""


# Problem z importowaniem 


"""
from datetime import datetime
import datetime as dt
"""


# datetme.... --> 10 funkcji które były na wcześniejszym imporcie 
# funkcja() nowy import działa 


# moduł random -- losowanie
import random

print(random.randint(1, 10))       # losowa liczba 1-10
print(random.choice(["a", "b"]))   # losowy element z listy
print(random.random())             # losowa liczba 0.0 - 1.0


# moduł datetime -- daty i czas
from datetime import datetime, date

dzisiaj = date.today()
print(dzisiaj)                     # 2026-03-24

teraz = datetime.now()
print(teraz.strftime("%d.%m.%Y %H:%M"))   # 24.03.2026 14:30


# Zadanie 14.1 -- Zaimportuj cały moduł statistics. Mając listę oceny = [3, 5, 4, 2, 5, 4], 
# wypisz jej średnią i medianę -- odwołując się do funkcji przez prefiks modułu. (Użyj funkcji mean() i median().)
import statistics as st
oceny = [3, 5, 4, 2, 5, 4]
srednia = st.mean(oceny)
mediana = st.median(oceny)
print(srednia)
print(mediana)
# Zadanie 14.2 -- Z modułu string zaimportuj tylko wybrane nazwy tak, aby dało się ich używać bez string.: 
# stałą z małymi literami alfabetu oraz stałą z cyframi. Wypisz obie. 
# (Podpowiedź: nazwy stałych to ascii_lowercase i digits sam dobierz właściwą formę importu.)
from string import ascii_lowercase, digits
print(ascii_lowercase)
print(digits)

# Zadanie 14.3 -- Zaimportuj moduł calendar z własnym, krótkim aliasem. 
# Korzystając z tego aliasu, sprawdź funkcją isleap(), czy rok 2024 i rok 2025 są przestępne.
import calendar as cal
print(cal.isleap(2024))
print(cal.isleap(2025))
# Zadanie 14.4 -- Z modułu fractions zaimportuj samą nazwę potrzebną do tworzenia ułamków (sam 
# dobierz właściwą instrukcję importu). 
# Dodaj do siebie ułamki 1/3 i 1/6 tak, aby wynik pozostał ułamkiem -- powinno wyjść 1/2.
from fractions import Fraction
#Rozwiązanie nr1
print(Fraction(numerator=1, denominator=3)+Fraction(numerator=1, denominator=6))
#Rozwiązanie nr2
a = Fraction(1,3)
b = Fraction(1,6)
wynik = a + b
print(wynik)

# Moduły pisane przez siebie 


import kalkulator as kal

print("*"*30)
print('SWÓJ WŁASNY MODUŁ')
print(kal.dodaj(2,5))
print(kal.odejmij(9,6))
print(kal.mnoz(4,4))


from kalkulator import dodaj,odejmij,mnoz

# pułapka: własna funkcja o tej samej nazwie NADPISUJE zaimportowaną dodaj()
def dodaj():
    print('DODAJ DODAJ DODAJ DODAJ DODAJ')

dodaj()              # --> woła NASZĄ dodaj() (0 argumentów), import został przykryty
print(odejmij(9,6))  # odejmij i mnoz dalej działają normalnie
print(mnoz(4,4))


# Pułapki import funkcji dla bezpieczeństwa z prefixem, 
# wentualnie jeśli chodzi o nazwy funkcji korzystać z aliasów, lub dawać nietypowe nazwy


# modul to podfolder obok skryptu --> import działa od razu
# folder skryptu jest automatycznie w sys.path, więc nie trzeba kombinować ze ścieżką
# (__init__.py nie jest wymagany w py 3.3+, modul działa jako namespace package)

import modul.kalk

print(modul.kalk.dodaj_2(3,6))

# można też wyciągnąć samą funkcję:
from modul.kalk import odejmij_2

print(odejmij_2(2,5))

###


# Zadanie 14c.1 -- Stwórz własny moduł figury.py (w stylu kalkulator.py) 
# z dwiema funkcjami: pole_kwadratu(a) zwracającą a * a oraz pole_kola(r) 
# zwracającą 3.14 * r ** 2. Dodaj blok if __name__ == "__main__":, 
# w którym testowo wypiszesz wynik jednej z funkcji. Następnie 
# w głównym pliku zaimportuj moduł figury i wywołaj obie funkcje.

"""
from math import fma
print('*'*100)
print(fma(2,2,2))

def wlasna_fma(x,y,z):
    return float((x*y)+z)

print(wlasna_fma(2,2,2))
"""

import figury
print(figury.pole_kwadratu(2))
print(figury.pole_kola(4))

##
import sys

print(sys.version)       # wersja Pythona
print(sys.platform)      # system operacyjny ('win32', 'linux', 'darwin')


import time

start = time.time()
time.sleep(1)            # pauza 1 sekunda
koniec = time.time()
print(f"Minęło: {koniec - start:.2f} sekund")

# matplotlib -- wykresy
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Mój wykres")
plt.show()
"""

# wirtualne środowiska (venv) i instalacja bibliotek (pip)

# globalne środowisko --> instaluje biblioteki na całego pythona w systemie (wszystkie projekty wspólnie --> konflikty wersji)
# wirtualne (venv) --> biblioteki tylko w folderze projektu, każdy projekt ma swoje

# ręczne ustawianie venv (windows, cmd):
# python --version --> czy python w ogóle jest
# cd 'sciezka' --> wchodzimy do folderu
# python -m venv venv --> tworzy środowisko (folder venv)
# .\venv\Scripts\Activate --> aktywacja (pojawia się (venv))
# deactivate --> wyjście ze środowiska

# pip:
# pip list --> co jest zainstalowane
# pip install matplotlib --> instaluje najnowszą wersję
# pip install matplotlib==3.8.0 --> konkretna wersja
# pip uninstall pillow --> odinstalowanie

# pip freeze > requirements.txt --> zapis bibliotek do pliku
# pip install -r requirements.txt --> instalacja z pliku

# pułapka na pipa --> instaluje to co mu dasz, nawet złośliwe rzeczy
# np. scikit-learn a ktoś wrzuca sciksit-learn (literówka) --> uważać na nazwy

print(f'{2*2}')


# Biblioteki pythona

# === DANE I OBLICZENIA ===
# numpy           Obliczenia numeryczne, tablice          pip install numpy
# pandas          Analiza danych, tabele (DataFrame)      pip install pandas
# matplotlib      Wykresy i wizualizacje                  pip install matplotlib
# seaborn         Ładniejsze wykresy statystyczne         pip install seaborn
# scikit-learn    Uczenie maszynowe (ML)                  pip install scikit-learn
# scipy           Obliczenia naukowe, statystyka          pip install scipy

# # === WEB / API ===
# requests        Zapytania HTTP / API                    pip install requests
# flask           Lekkie aplikacje webowe                 pip install flask
# django          Duży framework webowy ("z bateriami")   pip install django
# fastapi         Nowoczesne, szybkie API                 pip install fastapi
# beautifulsoup4  Scraping -- parsowanie HTML              pip install beautifulsoup4
# selenium        Automatyzacja przeglądarki              pip install selenium
# httpx           Nowoczesny klient HTTP (async)          pip install httpx

# # === BAZY DANYCH ===
# psycopg2        Łączenie z PostgreSQL                   pip install psycopg2-binary
# sqlalchemy      ORM -- baza danych jako obiekty         pip install sqlalchemy
# pymongo         Łączenie z MongoDB                      pip install pymongo

# # === RÓŻNE / NARZĘDZIA ===
# pillow          Praca z obrazami (zdjęcia)              pip install pillow
# pytest          Testy automatyczne                      pip install pytest
# python-dotenv   Wczytywanie zmiennych z pliku .env      pip install python-dotenv
# rich            Kolorowy, ładny wydruk w terminalu      pip install rich
# tqdm            Pasek postępu w pętli                   pip install tqdm


##############################################################################################################
# Odczytywania plików # Odczytywania plików # Odczytywania plików # Odczytywania plików # Odczytywania plików 
# ###############################################################################################################

from pathlib import Path
BASE = Path(__file__).parent   # katalog, w którym leży 4_dzien.py -> pliki szukamy obok skryptu

# ścieżka bezwzględna vs względna
# BASE --> pełna ścieżka do folderu w którym leży ten skrypt, np. C:\Users\<TwojaNazwa>\...\4_dzien
# BASE / "dane.txt" --> sklejamy folder z nazwą pliku --> pełna ścieżka do pliku
print(BASE)                 # --> jaki folder wykrył skrypt
print(BASE / "dane.txt")    # --> pełna ścieżka do dane.txt

# względna --> open("dane.txt") --> liczy się skąd odpalasz skrypt (cwd) --> zawodne
# bezwzględna --> open(BASE / "dane.txt") --> zawsze obok skryptu --> działa wszędzie
# Path(__file__).parent --> zawsze folder skryptu, niezależnie od użytkownika

dane = BASE / "dane.txt"
bledny = BASE / "asasasa.txt"   # celowo nieistniejący -> demo FileNotFoundError

# open() funkcja pozwalająca otwierać pliki oraz nasze pliki.
# -r read --> tylko odczyt
# open(dane, "r", encoding="utf-8")  # ŹLE: brak przypisania i brak close()
# -> uchwyt zostaje otwarty. Zawsze używaj 'with open(...)'

ksiazka = open(dane, "r", encoding="utf-8")

# Wystąpił błąd

# ksiazka.close()

# metody open() close() staramy się unikać

# with open 
with open(dane, "r", encoding="utf-8"):
    pass

# odczyt całego pliku jako jeden string

with open(dane, "r", encoding="utf-8") as plik:
    nasz_string = plik.read()
    print(nasz_string)
    print('*'*50)
    print(plik.tell()) #--> 140
    print(plik.seek(0)) #--> ustawienie na konkretnym miejscu
    print(plik.read())

# Książka, przekartowujemy --> koniec 
# open korzysta kursor 0 
# 'pythonsdsds' tell()

# readlines()

with open(dane, "r", encoding="utf-8") as plik:
    linie = plik.readlines()
    print(linie)
    for i in linie:
        print(i.strip())

with open(dane, "r", encoding="utf-8") as plik:
    print(plik.readlines())
    print('*'*20)
    print(plik.readlines())   # drugi readlines() -> [] (kursor jest już na końcu pliku)

with open(dane, "r", encoding="utf-8") as plik:
    linie = plik.readlines()
    print(linie[0])
    print(linie[-1])
    #   print(linie[100])   #--> błąd: IndexError (poza zakresem listy)
    print(linie[2:])
    print(linie[::2])

with open(dane, "r", encoding="utf-8") as plik:
    # linie = plik.readlines()
    print(plik.readline())
    print(plik.readline())
    print(plik.readline())
    print(plik.readline())
    tell_spot = plik.tell()
    print(plik.readline())
    print(plik.readline())
    plik.seek(tell_spot)
    print(plik.readline())

with open(dane, "r", encoding="utf-8") as plik:
    linie = len(plik.readlines())
    print(f'Mamy liczbę linii --> {linie}')

try:
    with open(bledny, "r", encoding="utf-8") as plik:
        plik_file = plik.readlines()
except FileNotFoundError as e:
    print(f'FileNotFoundError',e)


try:
    with open(dane, "r", encosding="utf-8") as plik:
        plik_file = plik.readlines()
except TypeError as e:
    print(f'Błąd typowania --> {e}')


# 15. Utwórz plik imiona i dane personalne --> Przemek-M-pesel-rok urodzni .... 
dane15 = BASE / "dane15.txt"


# Zadanie 15a.1 -- Odczytaj cały plik 'dane.txt' metodą read() i wypisz jego zawartość.

with open(dane15, "r", encoding="utf-8") as plik:
    nasz_string = plik.read()
    print(nasz_string)

# Zadanie 15a.2 -- Odczytaj plik jako listę linii (readlines()). Wypisz, ile linii ma plik, 
# a następnie każdą linię z numerem (np. 1: Ala ma kota). Skorzystaj z enumerate.

with open(dane15, "r", encoding="utf-8") as plik:
    lines = plik.readlines()
    print(len(lines))
    print(list(enumerate(lines)))
    for index,i in enumerate(lines,start=1):
        print(f'{index}: {i.strip()}')

# Zadanie 15a.3 -- Przejdź po pliku linia po linii (iteracja po pliku) i wypisz tylko 
# te linie, które po usunięciu \n mają więcej niż 10 znaków.

with open(dane15, "r", encoding="utf-8") as plik:
    lines = plik.readlines()
    print([i.replace('\n','') for i in lines if len(i.replace('\n','')) > 10])

# Zadanie 15a.4 -- Spróbuj odczytać plik o nazwie raport.txt. Jeśli plik nie istnieje, 
# nie pozwól programowi się wywalić -- zamiast tego wypisz komunikat Plik 'raport.txt' 
# nie istnieje! (użyj try/except FileNotFoundError).
sciezka_raport = 'raport.txt'
try:
    with open(sciezka_raport, "r", encoding="utf-8") as plik:
        nasz_string = plik.read()
        print(nasz_string)
except FileNotFoundError:
    print(f'plik {sciezka_raport} nie istnieje')


# Zadanie 15a.5* -- Odczytaj plik dane.txt do listy linii, 
# a następnie wypisz przedostatnią i ostatnią linię 
# (czyli „cofnij się o dwie" od końca). Zabezpiecz się na wypadek, gdyby plik miał mniej niż 2 linie.
 
with open(dane15, "r", encoding="utf-8") as plik:
    lines = plik.readlines()
    if len(lines) >= 2:
        print(lines[-2:])

# W oraz A 
# with open(dane15, "r", encoding="utf-8") as plik: -->r-->read
# with open(dane15, "w", encoding="utf-8") as plik: -->w-->write
# with open(dane15, "a", encoding="utf-8") as plik: -->a-->append

#### W OD A
# w nadpisuje plik --> czyści wszystko co jest w pliku
# A dodaje na sam koniec --> dodaje wartości do pliku

auta = BASE / "auta.txt"

with open(auta, "w", encoding="utf-8") as plik: # --> "w" nadpisuje plik: czyści dotychczasową zawartość i pisze od nowa
        plik.write('BMW\n')
        plik.write('Audi\n')
        plik.write('Toyota\n')


with open(auta, "w", encoding="utf-8") as plik: #--> nadpisuje wcześniejsze nadpisanie
        plik.write('Ford\n')
        plik.write('Porsche\n')


# append 

with open(auta, "a", encoding="utf-8") as plik: 
        plik.write('BMW\n')
        plik.write('Audi\n')
        plik.write('Toyota\n')

with open(auta, "a", encoding="utf-8") as plik: 
        plik.write('BMW\n')
        plik.write('Audi\n')
        plik.write('Toyota\n')

# z metodą append uważać szczególnie w pętlach


liczby_txt = BASE / "liczby.txt"
suma_write = BASE / "suma.txt"

# czytamy liczby z pliku, obliczamy sumę, zapisujemy wynik
with open(liczby_txt, "r", encoding="utf-8") as plik:
    liczby = [int(linia.strip()) for linia in plik]

suma = sum(liczby)

with open(suma_write, "w", encoding="utf-8") as plik:
    plik.write(f"Suma liczb: {suma}\n")
    plik.write(f"Średnia: {suma / len(liczby):.2f}\n")


lista_15 = BASE / "lista_15.txt"
dni_15 = BASE / "dni.txt"
test_15 = BASE / "test.txt"
# Zadanie 15b1 — zapis ("w")
# Utwórz plik lista.txt w trybie "w" i zapisz do niego 3 dowolne zakupy, każdy w osobnej linii.
# Pamiętaj o \n na końcu każdej linii.

with open(lista_15, "w", encoding="utf-8") as plik:
        plik.write('chleb\n')
        plik.write('mleko\n')
        plik.write('ser\n')


# Zadanie 15b2 — dopisywanie ("a")
# Dopisz do pliku lista.txt jeszcze jeden zakup (tryb "a"). 
# Uważaj: gdybyś użył "w", skasowałbyś
# poprzednie linie!

with open(lista_15, "a", encoding="utf-8") as plik:
        plik.write('szynka\n')

# Zadanie 15b3 — zapis listy w pętli ("w")
# Masz listę dni = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek"]. 
# Zapisz każdy element w osobnej linii do pliku dni.txt.

dni = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek"]
with open(dni_15, "w", encoding="utf-8") as plik:
        for ln in dni:
            plik.write(f'{ln}\n')



# Zadanie 15b4 — różnica "w" vs "a"
# Zapisz do pliku test.txt linię "Start\n" (tryb "w"). Następnie dwa razy uruchom dopisanie 
# linii "Kolejna linia\n" (tryb "a"). Na końcu odczytaj i wypisz cały plik — powinny być 3 linie.

with open(test_15, "w", encoding="utf-8") as plik:
        plik.write('Start\n')
with open(test_15, "a", encoding="utf-8") as plik:
        plik.write('Kolejna linia\n')
        plik.write('Kolejna linia\n')
with open(test_15, "r", encoding="utf-8") as plik:
        print(plik.read())


### Odczytywanie plików csv
# Wymaga biblioteki csv

# Imie;Nazwisko;Wiek;Dział --> przykład csv
# Przemek;Ss;28;it
# Dominik;Tar;24;Manager
# Adrianna;Słowik;48;Kasjer

csv_15 = BASE / "tabela.csv"
import csv


with open(csv_15 , "r", encoding="utf-8") as plik:
    czytnik = csv.reader(plik, delimiter=";")
    # next(czytnik) # --> next jest częścią wspólna w działaniu iteratorów --> sredn
    # next(czytnik)
    # czytnik.seek() #--> seek wywali błąd nie ma tejk metody w csv.reader 
    for i in czytnik:
         print(i)

with open(csv_15 , "w", newline="", encoding="utf-8") as plik:
     # newline="" -> bez tego na Windows CSV ma puste linie między wierszami
     czytnik = csv.writer(plik,delimiter=";")
     czytnik.writerow(['Ania','Łabądź',68])


with open(csv_15 , "a", newline="", encoding="utf-8") as plik:
     # przy csv.writer ZAWSZE dawaj newline="" (Windows wstawia \r\n, csv dokłada swoje -> puste wiersze)
     czytnik = csv.writer(plik,delimiter=";")
     czytnik.writerow(['Ania','Łabądź',68])
     czytnik.writerow(['Ania','Łabądź',68])
     czytnik.writerow(['Ania','Łabądź',68])
     czytnik.writerow(['Ania','Łabądź',68])
     
     

csv_15c = BASE / "osoby.csv"
dane_csv = BASE / "dane.csv"

# 15.c1 Stwórz plik osoby.csv z nagłówkiem Imie;Wiek;Miasto i 
# zapisz w nim 5 dowolnych osób (użyj csv.writer z delimiter=";").
with open(csv_15c , "w", newline="" ,encoding="utf-8") as plik:
        czytnik = csv.writer(plik, delimiter=";")
        czytnik.writerow(['Imie','Wiek','Miasto'])
        czytnik.writerow(['Ania',26,'Kraków'])
        czytnik.writerow(['Aneta',65,'Poznań'])
        czytnik.writerow(['Dominik',94,'Lublin'])
        czytnik.writerow(['Damian',25,'Lubartów'])
        czytnik.writerow(['Eris',19,'Władysławowo'])
        



# 15.c2 Wczytaj plik osoby.csv i wypisz tylko imiona wszystkich osób (pomijając nagłówek).
with open(csv_15c , "r", encoding="utf-8") as plik:
    czytnik = csv.reader(plik, delimiter=";")
    next(czytnik)
    for i in czytnik:
        print(i[0].split(';')[0])


# 15.c3 Oblicz średni wiek wszystkich osób w pliku i wypisz wynik. dane.csv

with open(dane_csv, "r", encoding="utf-8") as plik:
    czytnik = csv.reader(plik, delimiter=";")
    next(czytnik)
    suma_elementow = 0
    licznik = 0
    for i in czytnik:
        suma_elementow = suma_elementow + int(i[1]) # csv.reader już rozdzielił kolumny, split niepotrzebny
        licznik += 1

    print(f'Nasza średnia {suma_elementow/licznik}')


################################################################################################
# wykorzystanie usług sieciowych # wykorzystanie usług sieciowych # wykorzystanie usług sieciowych
################################################################################################

# Pobieranie danych za pomocą GET
# Przesyłanie danych za pomocą POST

# API (Application Programming Interface) to sposób komunikacji między programami. 
# Najczęściej pobieramy dane w formacie JSON za pomocą żądania GET.

import requests #--> wymagana biblioteka niewbudowana
link = 'https://jsonplaceholder.typicode.com/todos/'

# --> https://jsonplaceholder.typicode.com/todos/

odpowiedz = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print(odpowiedz.status_code) 

# STatusy kody
# 200 --> 2xx --> wszystko git
# 404 --> 4xx --> błąd po stronie klienta (zła nazwa, brak strony itp)
# 500 --> 5xx --> błędy serwera (coś leży po stronie serwera)


todo_1 = odpowiedz.json()

print(todo_1)

odpowiedz2 = requests.get("https://jsonplaceholder.typicode.com/todos/")
uzytkownicy = odpowiedz2.json()


for u in uzytkownicy[:3]:   # pierwsze 3
    print(f"{u['title']} -- {u['id']}")


# GET z parametrami -- zamiast doklejać je do URL, podajemy je jako słownik (params=...)

params = {"userId": 1,"id":1}

post_odpowiedz = requests.get(
    "https://jsonplaceholder.typicode.com/posts", params=params)

print(post_odpowiedz.status_code) 

posty = post_odpowiedz.json()
print(posty)


import requests

url = "https://jsonplaceholder.typicode.com/posts/999"

try:
    odpowiedz = requests.get(url, timeout=5) #--> timeout 
    if odpowiedz.status_code == 200:
        wynik_json = odpowiedz.json()
        print(wynik_json)
    elif odpowiedz.status_code == 404:
        print("Nie znaleziono zasobu!")
    else:
        print(f"Błąd: {odpowiedz.status_code}")
except requests.exceptions.ConnectionError:
    print("Brak połączenia z internetem!")
except requests.exceptions.Timeout:
    print("Przekroczono czas oczekiwania!")


# Post

nowy_post = {
    "title": "Mój post",
    "body": "Treść posta",
    "userId": 1
}

odpowiedz = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=nowy_post
)

print(odpowiedz.status_code)  # --> poprawny kod 201 --> dodanie zostalo zakończone sukcesem 
print(odpowiedz.json())


# Testowe api
# -> sonplaceholder.typicode.com
# -> pokeapi.co/api/v2/pokemon/pikachu
# -> 	dog.ceo/api/breeds/image/random

"""
# Bonus --> APi 
# headers = {
#     "Authorization": "Bearer TWOJ_TOKEN",
#     "Content-Type": "application/json"
# }
# odpowiedz = requests.get("https://api.example.com/dane", headers=headers)

"""

##################################################################################################
# OOP obiektów # OOP obiektów # OOP obiektów # OOP obiektów # OOP obiektów # OOP obiektów # OOP ob
##################################################################################################
# Wstęp do obiektowości
# Deklaracja klas
class KontoBankowe():
     pass

obiekt_1 = KontoBankowe()
print(obiekt_1) #--><__main__.KontoBankowe object at 0x00000291D02CBE00> 


class KontoBankowe(): 
     gatunek = 'Homo Sapiens' #--> atrybut klasy: wspólny i ten sam dla wszystkich obiektów (instancji)
     def __init__(self,imie,nazwisko,age=18): # Konstruktor 
          self.imie = imie          # --> atrybut instacji
          self.nazwisko = nazwisko  # --> atrybut instacji
          self.age = age            # --> atrybut instacji
# Napiszcie która będzie przechowywała książki --> strona, autor


# Tworzenie obiektów
konto_pierwsze = KontoBankowe('Przemek','Adamczyk',60)
print(konto_pierwsze.imie)
print(konto_pierwsze.nazwisko)
print(konto_pierwsze.age)
print(konto_pierwsze.gatunek)
konto_drugie = KontoBankowe('Artur','Polacki')
print(konto_drugie.imie)
print(konto_drugie.nazwisko)
print(konto_drugie.age)
print(konto_pierwsze.gatunek)


# Zadanie 18a.1 -- Stwórz klasę Gad z konstruktorem __init__, 
# który ustawia trzy atrybuty: gatunek, dlugosc (w cm) i jadowity 
# (True/False). Utwórz dwa obiekty (np. kobrę i pytona) i wypisz ich atrybuty.

class Gad():
    def __init__(self, gatunek: str, dlugosc: int, jadowity: bool):
        self.gatunek = gatunek
        self.dlugosc = dlugosc
        self.jadowity = jadowity

kobra = Gad("Kobra", 100, True)
pyton = Gad("Pyton", 200, False)   # pyton to dusiciel, nie jest jadowity

for i in [kobra, pyton]:
    print(f"gatunek {i.gatunek}, dlugosc {i.dlugosc}, jadowity {i.jadowity}")

# Metody
class AliorBank():
    def __init__(self,imie,saldo=1000):
          self.imie = imie
          self.saldo = saldo
    def __str__(self):
         return f'{self.imie} posiada saldo {self.saldo}'
    def wyplac(self,kwota):
         if kwota > self.saldo:
              return 'Brak możliwosći wypłaty pieniedzy.Brak środków'
         else:
            self.saldo -= kwota
            return f'Wypłacono {kwota} z konta o wartości {self.saldo}'
    def wplac(self,kwota):
         self.saldo += kwota
         return f'Wpłacono na konto {kwota}'


klient_jeden = AliorBank('Anna')
klient_dwa  = AliorBank('Dominik',2000)

print(klient_jeden.saldo,klient_jeden.imie)
print('*'*50)
print(klient_dwa.saldo,klient_dwa.imie)

print(klient_dwa.wyplac(3000))
print(klient_jeden.wplac(200))
print(klient_jeden.wplac(5000))
print(klient_jeden.saldo) 

# AliorBank MA __str__, więc print pokaże czytelny tekst, a NIE adres obiektu
print(klient_jeden) # --> Anna posiada saldo 6200

# Porównanie: KontoBankowe (z początku) NIE ma __str__ -> dostajemy domyślny adres obiektu
print(KontoBankowe('Ewa','Nowak')) # --> <__main__.KontoBankowe object at 0x...>

# Najczęściej używane metody magiczne


# Metody magiczne najczęściej wykonywane

# --> __init__ --> konstruktor 
# --> __str__ --> czyli wypisywanie wartości przy print() klasy
# --> __len__ --> len() zwrot długości atrybutu
# --> __eq__ --> który działa przy porównaniach ==
# --> __lt__ / __gt__ -->  < / > --> a < b
# --> __contains__ --> in
# --> __add__ --> a+b

# self # -->  _zmienna __zmienna i zmienna