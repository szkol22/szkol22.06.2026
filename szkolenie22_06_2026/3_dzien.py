#############################################################################
# 11. Zaawansowane przetwarzanie kolekcji # 11. Zaawansowane przetwarzanie ko
#############################################################################

# List comprehension
lista_compr = [x for x in range(1,10)]
print(lista_compr)

# list compr z filtracja
lista_compr_filtr = [x for x in range(1,21) if x % 2 == 0]
print(lista_compr_filtr)

# list compr działanie na liście (etykiety)

lista_compr_etykiety = ['tak' if x > 10 else 'nie' for x in range(1,21)]
print(lista_compr_etykiety)

# list compr ety(transformacja) + filtracja 
lista_compr_all = ['tak' if x > 10 else 'nie' for x in range(1,21) if x % 2 == 0]
print(lista_compr_all)

# **** NOWOŚĆ: zagnieżdżone comprehension -- spłaszczanie listy 2D
macierz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_splasz = [i for element in macierz for i in element] #--> zewnętrzna lista najpierw, potem wewnętrzna
print(lista_splasz)

"""
k = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in k:
    for b in i:
        pass
"""

# **** Tworzenie krotki z dwóch list
kolory = ["czerwony", "niebieski"]
rozmiary = ["S", "M", "L"]
ubranie = [(kolor,rozmiar) for kolor in kolory for rozmiar in rozmiary]
print(ubranie)

# 11.1 -- Mając listę ["hello", "WORLD", "Python", "CODE"], stwórz nową listę 
# z list comprehension, # gdzie wszystkie słowa są małymi literami, ale tylko te dłuższe niż 4 znaki.

lista = ["hello", "WORLD", "Python", "CODE"]
lista_11_1 = [slowo.lower() for slowo in lista if len(slowo) > 4]
print(f"Zadanie 11.1: {lista_11_1}")

# 11.2 -- Spłaszcz listę 2D [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]] 
# do jednej listy 1D za pomocą zagnieżdżonego comprehension.

list_2d = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
result_11_2 = [number for sublist in list_2d for number in sublist]
print("11.2:", result_11_2)

# 11.1A -- Mając listę liczb [7, 12, 5, 20, 3, 18, 9, 14], 
# stwórz listę zawierającą kwadraty tylko liczb parzystych (filtr if na końcu).

l4 = [7, 12, 5, 20, 3, 18, 9, 14]
l5 = [i**2 for i in l4 if i % 2 == 0]
print(l5)

# 11.2A -- Mając listę liczb [15, -3, 0, 8, -12, 4, 0, -7], stwórz listę etykiet, 
# gdzie każda liczba dodatnia to "+", a każda pozostała (zero lub ujemna) 
# to "-" (transformacja if/else na początku).

liczby_11 = [15, -3, 0, 8, -12, 4, 0, -7]
liczby_11_2A = ['+' if x>0 else '-' for x in liczby_11]
print(f"Zadanie 11.2A: {liczby_11_2A}")

# 11.2B -- Mając listę słów ["Python", "Go", "JavaScript", "C", "Rust"],
# stwórz listę krotek (słowo, długość) -- ale tylko dla słów dłuższych niż 2 znaki.

words = ["Python", "Go", "JavaScript", "C", "Rust"]
result_11_2B = [(word, len(word)) for word in words if len(word) > 2]
print("11.2B:", result_11_2B)

# 11.5A* -- Mając listę liczb od 1 do 30 (range(1, 31)), stwórz listę, 
# w której każdą liczbę podzielną przez 3 zamieniasz na tekst 
# "Fizz", a pozostałe zostawiasz bez zmian (jako liczbę).

l10 = ['Fizz' if i % 3 == 0 else i for i in range(1,31)] #->> range(start,stop+1)
print(l10)

# Dict comprehension

slownik = {key:value for key,value in enumerate(range(1,11)) }
print(slownik)

# filtrowanie słownika
# Miałbym krótkie zadanie --> wyświetl range(0,100) tylko dla liczb powyżej 50

slownik2 = {key:value for key,value in enumerate(range(0,101),start=1) if value > 50}
print(slownik2)

# Transformacja słownika  --> etykiety
slownik3 = {key:value for key,value in enumerate(range(0,10),start=1) if value > 5}
slownik4 = {key:'tak' if value % 2 == 0 else 'nie' for key,value in slownik3.items()}
print(slownik4)

slownik5 = {key:value**2 if value % 2 == 0 else 0 for key,value in slownik3.items()}
print(slownik5)

# ******* Odwracanie wartości comprehensi 
original = {"a": 1, "b": 2, "c": 3}
nowy_slownik = {value:key  for key,value in original.items()}
print(nowy_slownik)

# 11.3 -- Mając słownik oceny = {"Adam": 3, "Ola": 5, "Kasia": 4, "Bartek": 2, "Zofia": 5}, 
# stwórz nowy słownik (dict comprehension) zawierający tylko osoby z oceną >= 4.
oceny = {"Adam": 3, "Ola": 5, "Kasia": 4, "Bartek": 2, "Zofia": 5}
result_11_3 = {osoba: ocena for osoba, ocena in oceny.items() if ocena >= 4}
print("11.3:", result_11_3)

# 11.3A -- Mając dwie listy: produkty = ["mleko", "chleb", "masło"] i ceny = [3.5, 4.2, 6.0], 
# zbuduj słownik {produkt: cena} za pomocą dict comprehension i zip().

produkty = ["mleko", "chleb", "masło"]
ceny = [3.5, 4.2, 6.0]
print({i for i in zip(produkty, ceny)}) # --> to stworzy zbiór krotek

produkty = ["mleko", "chleb", "masło"]
ceny = [3.5, 4.2, 6.0]
result_11_3A = {produkt: cena for produkt, cena in zip(produkty, ceny)}
print(result_11_3A)

# 11.3B -- Mając słownik temperatur w stopniach Celsjusza temperatury = {"Warszawa": 20, "Madryt": 35, "Oslo": -5}, 
# stwórz nowy słownik z tymi samymi miastami, ale temperaturą przeliczoną na stopnie Fahrenheita (wzór: C * 9/5 + 32), 
# zaokrągloną do 1 miejsca po przecinku.

temperatury = {"Warszawa": 20, "Madryt": 35, "Oslo": -5}
print({k:round(v * 9/5 + 32,1) for k,v in temperatury.items()})

# 11.3C -- Mając słownik magazynu magazyn = {"jablka": 10, "banany": 0, "gruszki": 8, "sliwki": 0}, 
# stwórz słownik zawierający tylko produkty, których stan jest większy od 0 (czyli dostępne).

magazyn = {"jablka": 10, "banany": 0, "gruszki": 8, "sliwki": 0}
result_11_3C = {produkt: stan for produkt, stan in magazyn.items() if stan > 0}
print("11.3C:", result_11_3C)

# 11.3D -- Mając słownik kody = {"PL": "Polska", "DE": "Niemcy", "FR": "Francja"}, 
# odwróć go tak, by kluczem była nazwa kraju, a wartością kod (zamiana klucz↔wartość).

kody = {"PL": "Polska", "DE": "Niemcy", "FR": "Francja"}
print({v:k for k,v in kody.items()})

# 11.3E* -- Mając słownik ocen oceny = {"Adam": 2, "Ola": 5, "Kasia": 3, "Bartek": 4},
# stwórz nowy słownik, w którym dla osób z oceną >= 3 wartością jest "zdał", a dla pozostałych 
# "nie zdał" (filtr + if/else w wartości).

oceny = {"Adam": 2, "Ola": 5, "Kasia": 3, "Bartek": 4}
print({k:'zdal' if v>=3 else 'nie zdal' for k,v in oceny.items()})


# Update dodawanie elementów słowniki # comprehension
# 1 sposób
slownik = {x: x*x for x in range(1, 4)} 
slownik['nowyklucz'] = 'nowa wartosc'
slownik.update(name='Dominik')
print(slownik)

# 2 sposób operator  |
slownik = {x: x*x for x in range(1, 4)} | {'nowy': 100, 'a': 1}
print(slownik)

# 3 sposób ******* dodatkowa
slownik = {**{x: x*x for x in range(1, 4)}, 'nowy': 100, 'a': 1}
print(slownik)

# 4 sposób ******* Dodatkowa 
slownik = {k: v
            for x in range(1, 4)
            for k, v in ((x, x*x), (-x, x*x))}
print(slownik)

# map() problem z slownik.items() nie rozpakowywanie 

slownik = {'Alicja': 20, 'Katarzyna': 30, 'Marcelina': 40}
# list1 = list(map(lambda ky, vl: f'imie={ky}, wiek={vl}', slownik.items()))
# print(list1)

# od pythona 3 w górę umyślnie zostało rozpakowanie wycofane z map
# działa w pythonie 2

# https://www.jdoodle.com/python-programming-online -> interpreter python()

"""
# 3.14
slownik = {'Alicja': 20, 'Katarzyna': 30, 'Marcelina': 40}

# list1 = list(map(lambda ky, vl: f'imie={ky}, wiek={vl}', slownik.items()))

list1 = map(lambda (k, v): 'imie=%s, wiek=%s' % (k, v), slownik.items())
print(list1)
"""

# https://peps.python.org/pep-3113/ --> powód usunięcia 

from itertools import starmap

# ***** dodatkowy punkt
list1 = list(starmap(lambda ky, vl: f'imie={ky}, wiek={vl}', slownik.items()))
print(list1)

# https://www.geeksforgeeks.org/python/python-itertools-starmap/ --> wykorzystywanie przykłady



# Kilka argumentów jeśli chodzi o lambde map() filter() 

# --> filter() --> zawsze jeden argument --> więcej będzie sypać błędami

# --> map() --> 

produkty = ["Laptop", "Mysz", "Monitor"]
ceny     = [3500, 50, 1200,6000] # 4  <- 6000 ginie po cichu map ucina do najkrótszej listy
ilosci   = [2, 10, 3]
powystawowe = [True,False,True]

podsumowanie = list(map(lambda p, c, i,po: f"{p}: {c} zł x {i} = {c * i} zł Jest {'nie' if po == False else ''} powystawowe",produkty, ceny, ilosci,powystawowe))

print(podsumowanie)

# Dla stworzonej listy imie,oceny,srednia(sztywno z listy) stworzyli liste za pomocą map przekazując 3 argumenty 

imiona = ["Kasia", "Asia", "Jasia"]
oceny = [2, 3, 4]
srednie = [3.0, 4.5, 5.2]
lista = list(map(lambda i, o, s: (i, o, s), imiona, oceny, srednie))
print(lista)

## sorted( key =) ********

#Sortowanie po długości
slowa = ["Python", "Go", "JavaScript", "C", "Rust"]
nowe_slowa = sorted(slowa,key=len) # --> po długości znaków
nowe_slowa_rev = sorted(slowa,key=len,reverse=True) # --> długość znaków z reverse
print(slowa)
print(nowe_slowa) 
print(nowe_slowa_rev)


# Sortowanie stringów unicode
imiona = ["zofia", "ADam", "asia", "Bartek"]
print(sorted(imiona,key=str.lower)) # --> sortowania po niższym znaku alfab
print(sorted(imiona,key=str.lower,reverse=True)) # --> sortowania po niższym znaku alfab revers
print(sorted(imiona))

# A B C .......... a b c 

# sortowanie listy słowników
uczniowie = [
    {"imie": "Adam",  "ocena": 4},
    {"imie": "Ola",   "ocena": 5},
    {"imie": "Kasia", "ocena": 3}
]

print(sorted(uczniowie, key=lambda u: u["ocena"], reverse=True)) # --> sort po ocenie DESC
print(sorted(uczniowie, key=lambda u: u["ocena"]))   # --> sort po ocenie ASC

#pobieranie danych przykładowo z bazy  ocena != None

liczby = [3, -7, 1, -2, 5, -10]
print(sorted(liczby,key=abs)) # --> abs sortuje po odległości od 0 absolute 


ceny = ["100", "25", "9", "300"]
print(sorted(ceny,key=int)) # --> sortowanie po int nie zmieniając wartości oryginalnej listy

slowa = ["banan", "kiwi", "jablko", "cytryna"]
print(sorted(slowa,key=lambda k: k[-1])) # --> sortować po ostatnim znaku 

oceny = {"Adam": 4, "Ola": 5, "Kasia": 3, "Bartek": 5}
print(sorted(oceny.items(), key=lambda kv: kv[1], reverse=True)) #--> sortowanie po items()

uczniowie = [
    {"imie": "Adam", "ocena": 4},
    {"imie": "Ola", "ocena": 5},
    {"imie": "Bartek", "ocena": 5},
    {"imie": "Kasia", "ocena": 4},
]

print(sorted(uczniowie, key=lambda u: (-u["ocena"], u["imie"])))

# 11.4 -- Posortuj listę ["Python", "Go", "JavaScript", "C", "Rust", "Java"]
# po długości słowa rosnąco, a przy tej samej długości -- alfabetycznie.
l11_4 = ["Python", "Go", "JavaScript", "C", "Rust", "Java"]
print(sorted(l11_4, key=lambda x: (len(x),x)))

# 11.4A -- Posortuj listę liczb [3, -10, 1, -2, 7, -5] 
# według wartości bezwzględnej (odległości od zera) -- użyj key=abs.
l11_4A =  [3, -10, 1, -2, 7, -5] 
print(sorted(l11_4A, key=abs))

# 11.4B -- Masz ceny zapisane jako tekst ["45", "8", "120", "33", "9"]. 
# Posortuj je rosnąco po wartości liczbowej, a nie alfabetycznie.

l11_4B = ["45", "8", "120", "33", "9"]
print(sorted(l11_4B, key=int))

# 11.4C -- Mając słownik punktów punkty = {"Adam": 80, "Ola": 95, "Kasia": 60, "Bartek": 95}, 
# wyświetl pary (imie, punkty) posortowane po liczbie punktów malejąco.

punkty = {"Adam": 80, "Ola": 95, "Kasia": 60, "Bartek": 95}
print(sorted(punkty.items(), key=lambda x: x[1],reverse=True))

# 11.4D -- Mając listę krotek osoby = [("Adam", 30), ("Ola", 25), ("Kasia", 35), ("Bartek", 28)] (imię, wiek), 
# posortuj ją po wieku rosnąco.
osoby = [("Adam", 30), ("Ola", 25), ("Kasia", 35), ("Bartek", 28)]
print(sorted(osoby, key=lambda x: x[1]))
print(sorted(osoby, key=lambda x: (x[0],x[1]))) 

# 11.4E* -- Mając listę uczniów uczniowie = [{"imie": "Adam", "ocena": 4},
#  {"imie": "Ola", "ocena": 5}, {"imie": "Bartek", "ocena": 5}, {"imie": "Kasia", "ocena": 4}], 
# posortuj ją po ocenie malejąco, a przy tej samej ocenie -- alfabetycznie po imieniu (rosnąco).

uczniowie = [{"imie": "Adam", "ocena": 4}, 
             {"imie": "Ola", "ocena": 5}, 
             {"imie": "Bartek", "ocena": 5}, 
             {"imie": "Kasia", "ocena": 4}]
print(sorted(uczniowie, key=lambda x: (-x['ocena'], x["imie"])))

"""
uczniowie = [
    {"imie": "Adam", "ocena": 4},
    {"imie": "Ola", "ocena": 5},
    {"imie": "Bartek", "ocena": 5},
    {"imie": "Kasia", "ocena": 4},
]

print(sorted(uczniowie, key=lambda u: (-u["ocena"], u["imie"])))
# Sztuczka: minus odwraca sortowanie, ale działa TYLKO na liczbach (nie na stringach)
"""


l11_4 = ["Python", "Go", "JavaScript", "C", "Rust", "Java"]
print(sorted(l11_4, key=lambda x: (len(x),x)))
# po długości słowa rosnąco, a przy tej samej długości -- alfabetycznie.
# print(sorted(l11_4, key=lambda x: (-len(x), x),reverse=True))

#kilkanaście elementów --> widok w bazie --> pandas() 

#  any() i all()

# any() --> sprawdza nam czy jakikolwiek element jest poprawny z naszym warunkiem

# all() --> sprawdza czy wszystkie elementy zgadzają się z warunkiem

print(all([])) #--> True/ False --> all pusty zwróci True 
print(any([]))

liczby = [1, 2, 3, 4, 5, 6, 7, 8]

print(f'Lista liczby posiada parzyste liczby: {any(i % 2 == 0 for i in liczby)}')
print(f'Lista liczby posiada wszystkie parzyste liczby: {all(i % 2 == 0 for i in liczby)}')
print(f'Lista liczby posiada wszystkie liczby wyższe od zera: {all(i > 0 for i in liczby)}')


# 11.5 -- Mając listę liczb [12, 45, 67, 23, 89, 34, 56, 78], 
# sprawdź za pomocą any() czy jest liczba > 100, i za pomocą all() 
# czy wszystkie są dwucyfrowe.

liczby = [12, 45, 67, 23, 89, 34, 56, 78]
print(f'jest liczba > 100?: {any(i > 100 for i in liczby)}')
# 1 przypadek nie działający na listę z floatami
print(f'czy wszystkie liczby dwucyfrowe?: {all(len(str(i)) == 2 for i in liczby)}') # 1 przypadek
print(f'czy wszystkie liczby dwucyfrowe?: {all(10 <= i < 100 for i in liczby)}') # 2 przypadek


# reduce() # wykonuje działanie na liście zwracając nam np sume jako jedną wartość
from functools import reduce

liczby = [1, 2, 3, 4, 5]
suma = reduce(lambda a, b: a + b, liczby) # --> 15 
print(suma)

# Wykorzystaj na liście reduce, żeby pomnożyć przez wszystkie elemnty i zwrócić jeden wynik
# lista_liczb = [5,3,6,2,3]

"""
lista_liczb = [5,3,6,2,3]
suma_v1 = reduce(lambda a,b: a*b, lista_liczb)
print(suma_v1)
"""

"""
lista_liczb = [5,3,6,2,3]
print(reduce(lambda x,y: x*y, lista_liczb))
"""

# 11.7* -- Mając listę [3, 1, 4, 1, 5, 9, 2, 6, 5, 3], usuń duplikaty zachowując 
# oryginalną kolejność, 
# a następnie za pomocą reduce() oblicz iloczyn wszystkich unikalnych elementów.

# dict.fromkeys() --> użycie tego

"""
liczby = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique = list(dict.fromkeys(liczby))
iloczyn = reduce(lambda a, b: a * b, unique)
print("Unikalne:", unique)
print("Iloczyn:", iloczyn)
"""

"""
lista1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(list(dict.fromkeys(lista1)))
print(reduce(lambda x,y: x*y, list(dict.fromkeys(lista1))))
"""


print(sorted(osoby, key=lambda x: (x[0],x[1]))) 

from operator import itemgetter
print(sorted(osoby, key=itemgetter(1))) 


###########################################################################
# Wyjątki #  Wyjątki #  Wyjątki #  Wyjątki #  Wyjątki #  Wyjątki #  Wyjątki
###########################################################################

# Sposób na uniknięcie końca działania programu 

"""
try:
    input_value = int(input('Podaj nam wiek'))
    print(input_value)
except:
    print('Wprowadzona przez użytkownika wartość nie jest cyfrą')

print('Koniec działania programu')
"""


"""
try:
    float_example = 5.6/0
    # input_value = int(input('Podaj nam wiek'))
except ValueError:
    print('Value error')
except:
    print('Inny błąd')
"""

"""
try:
    float_example = float('dfgdfg')
except ValueError as e:
    print('Value error',e)
except:
    print('Inny błąd')
"""

# Najczęstsze błędy:
# W1. ValueError  -> value
try:
    liczba = int("abc")
except ValueError as e:
    print("Błąd: ValueError", e)

try:
    int('dasdas')
except ValueError as e:
    print(f"{type(e).__name__} error: {e}")

# W2. ZeroDivisionError --> dziele przez 0

try:
    wynik = 10 / 0
except ZeroDivisionError:
    print("Błąd: ZeroDivisionError")

try:
    a = 3/0
except ZeroDivisionError as e:
    print(f"{type(e).__name__} error: {e}")


# W3. IndexError    --> listy

try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError:
    print("Błąd: IndexError")

try:
    a = []
    b = a[1]
except IndexError as e:
    print(f"{type(e).__name__} error: {e}")

# W4. KeyError      --> slowniki 
try:
    slownik = {"a": 1}
    print(slownik["b"])
except KeyError:
    print("Błąd: KeyError")

try:
    a = {'k1':123}
    b = a['k2']
except KeyError as e:
    print(f"{type(e).__name__} error: {e}")

# W5. TypeError     --> niezgodne typy str + int

try:
    wynik = "5" + 3
except TypeError:
    print("Błąd: TypeError")

try:
    a = 3/'abc'
except TypeError as e:
    print(f"{type(e).__name__} error: {e}")


# 12.1 -- Napisz program, który pyta o liczbę i 
# wyświetla jej kwadrat. Jeśli użytkownik wpisze coś co nie jest liczbą
# wyświetl komunikat o błędzie.

"""
try:
    liczba = float(input("Podaj liczbę: "))
    print("Kwadrat liczby to:", liczba ** 2)
except ValueError:
    print("Błąd: Nie podałeś liczby")
"""

# 12.1A -- Poproś użytkownika o dwie liczby i wyświetl wynik ich dzielenia. 
# Obsłuż dwa różne błędy osobno: gdy wpisze coś, co nie jest liczbą (ValueError), 
# oraz gdy dzielnik to zero (ZeroDivisionError).
"""
try:
    liczba1 = float(input("Podaj liczbę: "))
    liczba2 = float(input("Podaj liczbę: "))
    print("Wynik dzielenia:", liczba1/liczba2)
except ValueError:
    print("Błąd: Nie podałeś liczby")
except ZeroDivisionError:
    print("Błąd: pamiętaj cholero, nie dziel przez zero")
"""
# 12.1B -- Mając listę kolory = ["czerwony", "zielony", "niebieski"], poproś użytkownika 
# o indeks i wyświetl kolor spod tego indeksu. Obsłuż sytuację, gdy indeks jest poza 
# zakresem (IndexError) oraz gdy użytkownik wpisze coś, co nie jest liczbą (ValueError).

"""
kolory = ["czerwony", "zielony", "niebieski"]

try:
    index = int(input("Podaj indeks od 0 do 2:"))
    print(f"Kolor: {kolory[index]}")
except IndexError:
    print("Błąd: wartość poza indeksem")
except ValueError:
    print("Błąd: nie podałeś prawidłowej liczby")
"""

# 12.1C -- Mając cennik ceny = {"chleb": 4, "mleko": 3, "masło": 8}, poproś użytkownika o 
# nazwę produktu i wyświetl jego cenę. Obsłuż sytuację, gdy produktu nie ma w cenniku (KeyError).

"""
ceny = {"chleb": 4, "mleko": 3, "masło": 8}
try: 
    produkt_usr = input("Podaj produkt:")
    print(f"Cena: {ceny[produkt_usr.lower()]}")
except KeyError:
    print("Błąd: produktu nie ma na liście") 
"""

# 12.1D* -- Zbieraj od użytkownika kolejne liczby i dodawaj je do listy, aż wpisze koniec. Jeśli 
# wpisze coś, co nie jest liczbą -- wyświetl ostrzeżenie i pytaj dalej 
# (nie przerywaj programu). Na końcu wyświetl sumę i średnią. Pamiętaj o 
# przypadku, gdy lista jest pusta (ZeroDivisionError przy średniej).

"""
try:
    lista_sum_sred = []
    while True:
        liczba = input("Podaj liczbę:")
        if liczba == 'koniec':
            break
        try:
            lista_sum_sred.append(float(liczba))
        except ValueError:
            print('To nie jest liczba, pomijam')
    suma_listy = sum(lista_sum_sred)
    srednia = sum(lista_sum_sred) / len(lista_sum_sred)
    print(f"Suma listy{suma_listy}")
    print(f"Srednia listy{srednia}")
except ZeroDivisionError:
    print('Nie można dzielić przez zero')
"""



# While pętla:: -->

"""
try:
    while True:
        try:
            wiek = int(input('Podaj swój wiek:'))
            break
        except ValueError:
            print('Nie podano liczby')
except:
    print("Losowy błąd")

print(f'Wiek to:{wiek}')
"""


try:
    print('...')
    # ....
    # ....
    # działanie
    # ......
    # ....
    # ....
    # ....
    # ....
    # ....
    # ....
    # ....
    # ....
    # ....
    # ....
except TypeError as e:
    print(f"{type(e).__name__} error: {e}") # logach


# 12.3 -- Mając listę napisów dane = ["12", "abc", "7", "3.5", "20", "xyz"],
# przejdź po niej pętlą i zsumuj tylko te, które da się zamienić na liczbę całkowitą 
# (int). Elementy, których nie da się przekonwertować, pomiń i wypisz ostrzeżenie. 
# Na końcu wyświetl sumę. (Tu pętla NIE pyta o input w kółko 

dane = ["12", "abc", "7", "3.5", "20", "xyz"]

suma_dane = 0
for i in dane:
    try:
        suma_dane += int(i)
        print(f"Dodajemy do {suma_dane} nasze:{i}")
    except ValueError as e:
        print("Value Error",e)
        print('Pomijamy element')

print(f"Suma całkowita z tej list liczb całkowitych to: {suma_dane}")


# 12.4 -- Mając listę par (dzielna, dzielnik): pary = [(10, 2), (5, 0), (9, 3), (8, 0)], 
# policz i wyświetl wynik dzielenia każdej pary. Gdy dzielnik to zero -- 
# wypisz komunikat i kontynuuj (nie przerywaj pętli). Na koniec pokaż, 
# ile dzieleń się udało, a ile nie.

pary = [(10, 2), (5, 0), (9, 3), (8, 0)]

udane = 0
nieudane = 0

for dzielnia,dzielnik in pary:
    try:
        print(f"Dzielenie '{dzielnia} / {dzielnik} kończy się wynikiem {dzielnia/dzielnik}")
        udane += 1
    except ZeroDivisionError as e:
        nieudane += 1
        print('Zerodivisionerror',e)

print(f'Udane dzialanie na parach to: {udane}, nieudane jednakże to {nieudane}')


#############################################################################################
# Funkcje # Funkcje # Funkcje # Funkcje # Funkcje # Funkcje # Funkcje # Funkcje # Funkcje #
#############################################################################################


def przywitaj():
    print('Witaj świecie')


przywitaj()

zmienna = przywitaj()
print(zmienna)

# return --> 

def linia():
    print("*"*100)
    return "*"*100

linia()

zmienna2 = linia()

print(zmienna2)

def zwroc_pi():
    return 3.14235423543

pi = zwroc_pi()
print(pi)

# argumenty oraz co to są parametry
# sumuj(4,6) --> temat moduły ////

def sumuj(a: int,b: int): #--> to będą nasze parametry
    return a + b

suma_d = sumuj(4,6) #--> przekazujemy argumenty
print(suma_d) 

def przyjmuje_zamowienie(a: str,b: int):
    print(f'Przyjęte zamówienie {a} w ilości {b}')

przyjmuje_zamowienie('koszulka', 20)

def przyjmuje_zamowienie2(a: str,b: int = 1): # --> wartość domyślna
    print(f'Przyjęte zamówienie {a} w ilości {b}')

# przyjmuje_zamowienie2('koszulka',456,34,25,34) # --> przyjmuje 2 argumenty, ale 5 zostało podanych

przyjmuje_zamowienie2('koszulka')

# przyjmuje_zamowienie2(1,'koszulka') --> kolejnosc przekazywania argumentów taka sama jak w funkcji parametry

# def funkcjeasdbv(a=245, b): # --> kolejność przekazywania argumentów jest ważna domyślne zawsze na koniec
#     print('...')


# 13a.1 -- Napisz funkcję linia() (bez parametrów), która wypisuje 30 gwiazdek * w jednej linii. 
# Wywołaj ją trzy razy.
def linia():
    print("*"*30)

linia()
linia()
linia()

# 13a.2 -- Napisz funkcję przywitaj(imie) z jednym parametrem, która wypisuje Cześć, <imie>!. 
# Wywołaj ją dla dwóch różnych imion.

def witaj(imie:str): #--> jeden parametr imię
    print(f'Cześć, {imie}!')

witaj('Dominik')
witaj('Robert')


# 13a.3**** -- Napisz funkcję przedstaw(imie, wiek, miasto) z trzema parametrami, 
# która wypisuje <imie> ma <wiek> lat i mieszka w <miasto>. 
# Wywołaj ją raz pozycyjnie, a raz z nazwanymi argumentami (w dowolnej kolejności).

def przedstaw(imie,wiek,miasto):
    print(f'{imie} ma {wiek} lat i mieszka w {miasto}')

przedstaw('Przemek', 60, 'Kraków')
przedstaw(miasto='Poznań',imie='Robert',wiek=40)
# przedstaw(40,miasto='Poznań',imie='Robert') --> albo pozycyjnie, albo nazwanymi argumentami

# 13a.4 -- Napisz funkcję suma_trzech(a, b, c), która wypisuje sumę trzech podanych liczb. Wywołaj ją dla 2, 5, 8.

def suma_trzech(a,b,c): #-> parametry
    print(sum([a,b,c]))

suma_trzech(2,5,8) # --> argumenty

# kilka returnów --> więcej niż jedna wartość zwracana

lista = [5,6,3,4,6,4]

def zwroc_min_max(lista):
    return min(lista),max(lista)

minimalna, maxymalna = zwroc_min_max(lista)

print(minimalna)
print(maxymalna)

# **** *args

def suma_elementow(pierwszy: str,*args,domyslny ='paca'):
    print(f"Tutaj: {pierwszy},{domyslny}")
    print(args)
    print(sum(args))


suma_elementow('sdfdsfsd',7,8,9,45,6,3,6,3,5,2,6,4)

# *args opakowuje elementy w krotkę niezależnie od ilości
# imie,age, *args, domyslne --> kolejność przekazywania argumentów do funkcji

# Dokumentacja funkcji co robi i jak ją wywołać
def podaj_liczbe_i_sumuj():
    """Ta funkcja jest odpowiedzialna za przyjmowanie liczb oraz zwracanie ich sumy oraz sredniej """
    try:
        lista_sum_sred = []
        while True:
            liczba = input("Podaj liczbę:")
            if liczba == 'koniec':
                break
            try:
                lista_sum_sred.append(float(liczba))
            except ValueError:
                print('To nie jest liczba, pomijam')
        suma_listy = sum(lista_sum_sred)
        srednia = sum(lista_sum_sred) / len(lista_sum_sred)
        print(f"Suma listy{suma_listy}")
        print(f"Srednia listy{srednia}")
        return suma_listy , srednia
    except ZeroDivisionError:
        print('Nie można dzielić przez zero')

# suma_z_listy, srednia_z_listy = podaj_liczbe_i_sumuj()

# print(suma_z_listy,srednia_z_listy)


print(podaj_liczbe_i_sumuj.__doc__)

# sortowanie po wielu kolumnach za pomoca funkcji sort w pythonie 
ludzie = [
    {"imie": "Jan",   "nazwisko": "Abacki",    "wiek": 30, "pensja": 7000, "miasto": "Gdansk"},
    {"imie": "Anna",  "nazwisko": "Kowalska",  "wiek": 30, "pensja": 5000, "miasto": "Krakow"},
    {"imie": "Adam",  "nazwisko": "Kowalski",  "wiek": 30, "pensja": 6000, "miasto": "Krakow"},
    {"imie": "Adam",  "nazwisko": "Kowalski",  "wiek": 30, "pensja": 5500, "miasto": "Krakow"},
    {"imie": "Ola",   "nazwisko": "Nowak",     "wiek": 25, "pensja": 4000, "miasto": "Krakow"},
    {"imie": "Ewa",   "nazwisko": "Zielinska", "wiek": 30, "pensja": 7000, "miasto": "Gdansk"},
]


for i in ludzie:
    print(i)
print('*' * 70)

# ludzie.sort(key=lambda o: o["imie"])
# ludzie.sort(key=lambda o: o["pensja"], reverse=True)
# ludzie.sort(key=lambda o: o["nazwisko"])
# ludzie.sort(key=lambda o: o["wiek"], reverse=True)
# ludzie.sort(key=lambda o: o["miasto"])

# Jeśli sortujemy po linijce --> trzeba wykonać je w odwrotnej kolejności 
ludzie.sort(key=lambda o: o["miasto"])
ludzie.sort(key=lambda o: o["wiek"], reverse=True)
ludzie.sort(key=lambda o: o["nazwisko"])
ludzie.sort(key=lambda o: o["pensja"], reverse=True)
ludzie.sort(key=lambda o: o["imie"])

for i in ludzie:
    print(i)
print('*' * 70)

# sorted( ... imie, pensja,nazwisko,wiek,miasto)

# Funkcja rekurencyjnej 

# To jest taka funkcja która odwołuje do samej siebie

"""
def policz():
    return policz()
"""

# Dwa warunki
# Przerwanie pętli --> odliczanie w jedną stronę przerwane warunkiem
# odwołuje się do samej siebie obniżając wyniki

# Jak to działa krok po kroku dla silnia(5):

# silnia(5) = 5 * silnia(4)
#           = 5 * (4 * silnia(3))
#           = 5 * (4 * (3 * silnia(2)))
#           = 5 * (4 * (3 * (2 * silnia(1))))
#           = 5 * 4 * 3 * 2 * 1 = 120

def silnia(n):
    if n <= 1:
        return 1
    return n * silnia(n-1)

print(silnia(5))

# Ciąg Fibonacciego -- każdy element to suma dwóch poprzednich: 0, 1, 1, 2, 3, 5, 8, 13, 

# n-ty wyraz ciągu Fibonacciego
def fib(n):
    if n == 0:           # warunek bazowy
        return 0
    if n == 1:           # warunek bazowy
        return 1
    return fib(n - 1) + fib(n - 2)   # krok rekurencyjny -- dwa wywołania

print(fib(7))   # 13

# wypisanie kilku pierwszych wyrazów
for i in range(10):
    print(fib(i), end=" ")   # 0 1 1 2 3 5 8 13 21 34
print()

# *args ---> **kwargs
def funkcja_kwargs(**kwargs):
    for i in kwargs.values():
        print(i)


funkcja_kwargs(name='przemek',age=24,dom=True,element='yes')