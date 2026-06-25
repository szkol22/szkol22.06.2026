#####################################################################################
# Listy # Listy # Listy # Listy # Listy # Listy # Listy # Listy # Listy # Listy # Li
#####################################################################################

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Kasowanie elementów z listy Kasowanie elementów z listy Kasowanie elementów z listy
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Usuwanie elementów z listy --> remove() , pop() , del, clear()

# --> remove() -> bierze jakąś wartość i usuwa ją z listy --> remove('gruszka')
# --> pop() -> jeśli nie podamy argumentu usuwa ostatni element, jeśli chcemy konkrenty to index pop(0)
# --> pop --> Można przypisać do zmiennej wartość 
# --> del -> usuwamy po indexie. Usuwa na zawsze --> del lista[index]
# --> clear -> usuwa wszystko z listy

owoce = ["jablko", "banan", "gruszka", "kiwi", "banan"]

print(owoce)
owoce.remove('jablko')
print(owoce)
# owoce.remove('jablko') # --> UWAGA nie ma elementu wywali błąd
if 'jablko' in owoce:
    owoce.remove('jablko')
print(owoce)
ostatni_element = owoce.pop()
print(owoce)
print(ostatni_element)
pierwszy_element = owoce.pop(0)
print(owoce)
print(pierwszy_element)
# owoce.pop(10) --> wywali błąd jak przekroczymy nasz index 
# del owoce[10] --> wywali błąd jak przekroczymy nasz index 
del owoce[0]
print(owoce)
owoce.clear()
print(owoce)

# 7.21* -- Masz listę produkty = ["mleko", "chleb", "masło", "jajka", "ser"]. Wykonaj po kolei poniższe operacje, 
# wyświetlając listę po każdej z nich. Użyj wszystkich sposobów usuwania (remove, pop, del, clear) i 
# obsłuż błędy, żeby program się nie wywalił:

# usuń "chleb" przy użyciu remove()
# usuń element o indeksie 0 i zapisz go do zmiennej przy użyciu pop(), wyświetl co usunąłeś,
# usuń ostatni element pop(),
# usuń element o indeksie 0 del,
# spróbuj usunąć "czekolada", której nie ma na liście sprawdzając wpierw, czy tam jest,
# spróbuj pop() na liście, którą wcześniej wyczyścisz (clear) -- złap drugi rodzaj błędu.


owoce = [2,5,3]
owoce.clear()
print(owoce)
# owoce.pop() # --> IndexError: pop from empty list na pustej liście wywali błąd w pop()

# Rozwiązanie1
"""
produkty = ["mleko", "chleb", "masło", "jajka", "ser"]
produkty.remove('chleb')
print(produkty)
prod0 = produkty.pop(0)
print(prod0)
del produkty[0]
print(produkty)
to_remove = 'czekolada'
if(produkty.__contains__(to_remove)): # --> inny sposób sprawdzenie --> if '' in lista
    produkty.remove(to_remove)
print(produkty)
produkty.clear()
el0 = produkty.pop(0)
"""

# Rozwiązanie2
"""
produkty = ["mleko", "chleb", "masło", "jajka", "ser"]
print(produkty)
if "chleb" in produkty:
    produkty.remove("chleb")
else:
    print("Nie ma takiego produktu na liście")
print(produkty)
try:
    pierwszy_element = produkty.pop(0)
    print("Usunięto:", pierwszy_element)
except IndexError:
    print("Błąd: lista jest pusta albo nie ma takiego indeksu")
print(produkty)
try:
    ostatni_element = produkty.pop()
    print("Usunięto:", ostatni_element)
except IndexError:
    print("Błąd: lista jest pusta")
print(produkty)
try:
    del produkty[0]
except IndexError:
    print("Błąd: nie ma elementu o takim indeksie")
print(produkty)
if "czekolada" in produkty:
    produkty.remove("czekolada")
else:
    print("Nie ma czekolady na liście")
print(produkty)
produkty.clear()
print(produkty)
try:
    usuniety_element = produkty.pop()
    print("Usunięto:", usuniety_element)
except IndexError:
    print("Błąd: nie można użyć pop() na pustej liście")
print(produkty)
"""

produkty = ["mleko", "chleb", "mleko", "jajka", "mleko"]
print(produkty)
produkty.remove('mleko') # --> ważna zależność usuwa pierwszy element napotkany na liście 
print(produkty)


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Funkcje wbudowane w listy Funkcje wbudowane w listy Funkcje wbudowan Funkcje wbudo
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Sortowanie i odwracanie list Sortowanie i odwracanie list Sortowanie i odwracanie 
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# SUM COUNT INDEX MAX MIN LEN # SUM COUNT INDEX MAX MIN LEN # SUM COUNT INDEX MAX M
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

lista_num = [9,4,2,5,6,3,5,6.7] #--> lista numeryczna float int

print(sum(lista_num)) #--> suma elementów listy
print(max(lista_num)) #--> maksymalna wartość
print(min(lista_num)) #--> minimalna wartość 
print(len(lista_num)) #--> długość elementów listy
print(lista_num.count(5))
# print(lista_num.index(0)) # --> 0 nie ma na liście → ValueError
print(lista_num.index(9)) # --> zwraca pod jakim indexem jest numer 9


slowa = ["banan", "ananas",'banan', "czeresnia", "jablko"]

# print(sum(slowa)) #--> nie można korzystać z + dla połączenia int str
print(len(slowa)) #--> ilość elementów w liście (ile jest słów)
print(max(slowa)) #--> wyraz "największy" alfabetycznie (wg Unicode): "jablko"
# Każda litera ma unicode przypisany, czy mała, czy duża i po tym unicodzie działa max min
print(min(slowa)) #--> wyraz "najmniejszy" alfabetycznie (wg Unicode): "ananas"
print(max(slowa,key=len)) #--> najdluzszy wyraz na liscie
print(min(slowa,key=len)) #--> najkrótszy wyraz na liscie

print(slowa.count('banan'))
print(slowa.index('banan')) # --> pierwsze wystąpienie na liście 

# Uwaga nie mieszać list 

mieszanka = ['banan',5, 7.6, True,'python']
print(len(mieszanka)) #--> ile elementów na liście
# print(max(mieszanka)) #--> '>' not supported between instances of 'int' and 'str'
# print(min(mieszanka)) #--> '<' not supported between instances of 'int' and 'str'
# print(sum(mieszanka)) #--> unsupported operand type(s) for +: 'int' and 'str'


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# SORT SORTED # SORT SORTED # SORT SORTED # SORT SORTED # SORT SORTED # SORT SORTED
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# .sort() --> metoda  sorted() --> funkcja

lista_do_so = [9,8,7,4,78,6,4,6,3,9]
print(lista_do_so)
lista_do_so.sort()
print(lista_do_so)

#Uwaga pułapka
"""
lista_do_so = [9,8,7,4,78,6,4,6,3,9]
lista_nowa = lista_do_so.sort() # --> .sort() sortuje listę, ale tylko oryginalną
print(lista_do_so)
print(lista_nowa)
"""

# sorted 
lista_do_sorted = [9,8,7,4,78,6,4,6,3,9]
lista_nowa = sorted(lista_do_sorted) #-->sorted do tworzenia nowej listy lub printowania posortowanej
print(lista_do_sorted)
print(lista_nowa)

# UWAGA PUŁAPKA

"""
lista_pulapka = [9,8,7,4,3,9]
lista_pup_nowa = lista_pulapka # --> lista_pulapka[:]
lista_pup_nowa.append(7.8) # --> append przypisal do oryginalnej i do nowej 
print(lista_pulapka)
print(lista_pup_nowa)
"""
#Rozwiązanie 
lista_pulapka = [9,8,7,4,3,9]
lista_pup_nowa = lista_pulapka[:] # --> lista_pulapka[:] albo .copy()
lista_pup_nowa2 = lista_pulapka.copy() #--> kopia
lista_pup_nowa.append(7.8)
lista_pup_nowa2.append(7.8)  
print(lista_pulapka)
print(lista_pup_nowa)
print(lista_pup_nowa2)

# sorted --> reverse

lista_rever = [9,8,7,4,78,6,4,6,3,9]
lista_new_re = sorted(lista_rever,reverse=True)
lista_rever.sort(reverse=True)
print(lista_new_re)
print(lista_rever)

# 7.5 -- Stwórz listę liczb [5, 3, 8, 1, 9, 2, 7]. Posortuj ja rosnąco i wyświetl, potem malejąco i wyświetl.

#Rozwiązanie nr1
"""
liczby = [5, 3, 8, 1, 9, 2, 7]
liczby_asc = sorted(liczby)
liczby_desc = sorted(liczby, reverse=True)
print(liczby_asc)
print(liczby_desc)
"""

#Rozwiązanie nr2
"""
list1 = [5, 3, 8, 1, 9, 2, 7]
print(sorted(list1))
print(sorted(list1, reverse=True))
"""

# 7.17A -- Wygeneruj listę 10 elementów o losowej wartości liczbowej, posortuj listę i wyświetl jej zawartość 
# linia po linii.


# Rozwiązanie nr1
"""
import random
lista_random = [random.randint(1, 10) for _ in range(10)]
lista_rand_sorted = sorted(lista_random)
print(f"Cała lista po sortowaniu {lista_rand_sorted}")
for i in lista_rand_sorted:
    print(i)
"""

# Rozwiązanie nr2
"""
import random
list2 = [random.randint(1,100) for _ in range(10)]
list2.sort()
print(f"Cała lista po sortowaniu{list2}")
for i in list2:
    print(i)
"""

list1 = [5, 3, 8, 1, 9, 2, 7]
list2 = sorted(list1)
print(sorted(list1))
print(reversed(list2)) # --> zwraca nam coś takiego jak iterator

# for i in range(10) --> iterowac 
print(list(reversed(sorted(list1))))

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Inne ciekawe funkcje i możliwości Inne ciekawe funkcje i możliwości Inne ciekawe f
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# map() oraz filter() # zwykle trzeba opakować jako listę

# map -- zastosuj funkcje do każdego elementu
liczby = [1, 2, 3, 4, 5]
podwojone = list(map(lambda x: x * 2, liczby))
print(podwojone)   # [2, 4, 6, 8, 10]

# lambda argument: (co robimy z argumentem),lista

# filter -- zostaw tylko elementy spełniające warunek
parzyste = list(filter(lambda x: x % 2 == 0, liczby))
print(parzyste)    # [2, 4]

szesciany = list(map(lambda i: i**3, liczby))
print(szesciany)

nieparzyste = list(filter(lambda y: y % 2 != 0,liczby))
print(nieparzyste)


lista_compre = ['Tak' if i % 2 == 0 else "Nie" for i in range(10)]
#--> To wyrażenie warunkowe (ternary), które każdemu elementowi przypisuje 'Tak'/'Nie'
print(lista_compre)

# 7.6 -- Mając listę liczb od 1 do 20, użyj filter() z funkcją lambda,
# aby stworzyć listę zawierającą tylko liczby podzielne przez 3.

#Rozwiązanie 7.6 nr1
lista20 =  list(range(1,21)) #--> range (start,stop+1,step)
print(lista20)
podzielne3 = list(filter(lambda x: x % 3==0, lista20))
print(podzielne3)

#Rozwiązanie 7.6 nr2
list1 = [i for i in range(1,21)]
print(list1)
list2 = list(filter(lambda x: x % 3 == 0, list1))
print(list2)

# 7.9A -- Mając listę słów slowa = ["python", "java", "kotlin", "go"], użyj map() z lambda, 
# aby stworzyć nową listę tych słów zapisanych WIELKIMI literami.

slowa = ["python", "java", "kotlin", "go"]
uppercase = list(map(lambda x: x.upper(), slowa))
print(uppercase)

# 7.12A -- Mając listę cen netto ceny = [100, 250, 49.99, 1200], użyj map() z lambda, aby policzyć ceny brutto 
# (VAT 23%, czyli wartość razy 1.23). Każdą cenę zaokrąglij do 2 miejsc po przecinku (round(x, 2)).

ceny = [100, 250, 49.99, 1200]
brutto = list(map(lambda x: round((x*1.23),2), ceny))
print(brutto)

# 7.11A* -- Mając listę liczb dane = [3, 8, 1, 12, 5, 20, 7], połącz filter() i map(): najpierw filter() 
# zostaw tylko liczby większe od 5, a potem map() podnieś każdą z nich do kwadratu. Wyświetl wynik.

# Rozwiązanie nr1
dane = [3, 8, 1, 12, 5, 20, 7]
wynik = list(map(lambda x: x**2, filter(lambda x: x > 5, dane)))
print(wynik)

# Rozwiązanie nr2
dane = [3, 8, 1, 12, 5, 20, 7]
print(list(map(lambda x: x*x, list(filter(lambda x: x > 5, dane)))))


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Rozpakowywanie 
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


lista = ['gruszka','jablon']
# gruszka = lista[0]
# jablon = lista[1]
gruszka, jablon = lista
print(gruszka,jablon)

lista = ['gruszka','jablon','agrest','ananas']
gruszka, *srodek, ananas = lista
print(f"Pierwszy element --> {gruszka}\n Drugi element --> {srodek}\n Trzeci element -> {ananas}")


lista = ['gruszka','jablon','agrest','ananas']
gruszka, jablon,*reszta, = lista
print(f"Pierwszy element --> {gruszka}\n Drugi element --> {jablon}\n Trzeci element -> {reszta}")



# zip(lista1,lista2)
lista_a = [3,6,3,4]
lista_b = ['a','b','c']
zmienna = zip(lista_a,lista_b) # --> <zip object at 0x0000026241279780>
print(zmienna)

for i,s in zip(lista_a,lista_b):
    print(i,s)


for i in zip(lista_a,lista_b): # zip kończy na najkrótszej liście -> 4 zostaje pominięte.
    cyfra,litera = i
    print(f"Cyfra to {cyfra}, Litera to {litera}")


lista_rozp = ['grusz','jablon','kasztan']
grusz, *reszta = lista_rozp
print(reszta)
print(*reszta)

# 7.7 -- Mając dwie listy: imiona = ["Adam", "Ola", "Kasia"] i oceny = [5, 4, 3], 
# wyświetl je w parach: Adam: 5, Ola: 4 itd.

imiona = ["Adam", "Ola", "Kasia"]
oceny = [5, 4, 3]

for i in zip(imiona, oceny):
    imie, ocena = i
    print(f'{imie}: {ocena},')


# *** dodatkowa
# hash() --> zwraca liczbowy "odcisk" obiektu (int), np. hash('python') -> -3982 ... (duża liczba)
# Działa TYLKO na obiektach niemutowalnych (str, int, float, bool, tuple); na liście/secie/dict rzuca błąd

string_example = 'python'
int_example = 45
bool_example = True
float_example = 5.7

list_example = list(range(1,20))

print(hash(string_example)) #--> str jest nieedytowalny .replace() 
print(hash(int_example))
print(hash(bool_example))
print(hash(float_example))
# print(hash(list_example)) # --> edytowalna hash wywala błąd


# UWAGA PUŁAPKA nie usuwać za pomocą remove albo w del
lista_rem = [2,4,6,8]
print(lista_rem)
for i in lista_rem: # 0 1 2 3 --> 0 1 2 --> itetor  --> 0 1 
    if i % 2 == 0:
        lista_rem.remove(i)

print(lista_rem)


#######################################################################################
# Krotka # Krotka # Krotka # Krotka # Krotka # Krotka # Krotka # Krotka # Krotka # Krot
#######################################################################################

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Tworzenia krotek 
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

tuple_example = tuple() # --> pusta krotka (); jeśli krotka z wartościami -->  (2,5,4,3)
tuple_example1 = ()
tuple_example2 = ('ss')
tuple_example3 = ('ss',)
tuple_example4 = 'ss',
tuple_example5 = 5,6 # --> to nie będzie float --> tuple --> (5,6)
tuple_example6 = 6,7,3,4,5,6,3

# print((tuple_example))
# print((tuple_example1))
# print((tuple_example2))
# print((tuple_example3))
# print((tuple_example4))
# print((tuple_example5))
# print((tuple_example6))

# print(type(tuple_example))
# print(type(tuple_example1))
# print(type(tuple_example2))
# print(type(tuple_example3))
# print(type(tuple_example4))
# print(type(tuple_example5))
# print(type(tuple_example6))

#Krotki są nieedytowalne 
# chowamy tam dane, które się nie zmieniają np. rok urodzenia, pesel itp etc.


# Konwersja z lista na krotek i odwrotnie
krotka = 5,6,7,9
print(krotka)
lista_z_kro = list(krotka)
print(lista_z_kro) 
krotka_powrot = tuple(lista_z_kro)
print(krotka_powrot) 


# To działanie indexowania oraz slicingu 
owoce = ("jablko", "banan", "gruszka", "kiwi", "mango")
print(owoce[0])
print(owoce[-1])
print(owoce[::2])
print(owoce[2:])
print(owoce[:4])

# Rozpakowywanie lista
owoce = ("jablko", "banan")
x, y = owoce
print(f"X to {x}, y to {y}")
x , y = y, x
print(f"X to {x}, y to {y}")


# 8.1 -- Stwórz krotkę z 4 porami roku. Wyświetl pierwsza i ostatnia.
seasons = ('wiosna', 'lato', 'jesien', 'zima')
print(f'{seasons[0]}, {seasons[-1]}')
# 8.2 -- Stwórz krotkę punkt = (5, 10). Rozpakuj ja do zmiennych x i y. Wyświetl: x=5, y=10.
punkt = (5, 10)
x,y = punkt
print(f'x={x}, y={y}')
# 8.3 -- Stwórz krotkę dane = ("Adam", 25, "Warszawa"). 
# Rozpakuj ja do zmiennych imie, wiek, miasto i wyświetl w f-stringu.
dane = ("Adam", 25, "Warszawa")
imie,wiek,miasto = dane
print(f'ime:{imie} ,wiek:{wiek} ,miasto:{miasto}')


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Edycja, krotek
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# Brak metod służących na zmienianie krotek
owoce = 'gruszka',
print(owoce)
owoce = owoce + ('jablon','grusza')
# owoce = owoce + 'jablon','grusza' #-> can only concatenate tuple (not "str") to tuple
hahaha = ('ha',) * 3
# hahaha = 'ha', * 3 # --> Value after * must be an iterable, not int

print(owoce)
print(hahaha)

# hahaha = ('ha',) - ('haha',) #--> unsupported operand type(s) for -: 'tuple' and 'tuple'

# funkcje przypisane 

owoce = ("jablko", "banan", "gruszka", "banan", "jablko", "banan")

print(owoce.count('banan'))
print(owoce.index('banan'))
print(len(owoce))

liczby = (4, 2, 8, 1, 5)
print(sum(liczby )) #--> suma elementów krotki
print(max(liczby )) #--> maksymalna wartość
print(min(liczby )) #--> minimalna wartość

# sorted()
# Pułapka sorted zwraca listę, więc potem trzeba spowrotem zmienic na tuple 
nowa_krotka = sorted(liczby) # --> przy sorted() zwraca nam listę
nowa_krotka = tuple(nowa_krotka)
# nowa_krotka.sort(reverse=True) #--> AttributeError: 'tuple' object has no attribute 'sort'
print(nowa_krotka)

# Wykorzystanie krotek 
def min_max(lista):
    return min(lista), max(lista)

mi, maxox = min_max([5,7,3,4,6])
print(f"MINIMUM: {mi}--> MAXIMUM: {maxox}")

# 8.4 -- Mając krotkę liczby = (3, 7, 1, 9, 4, 7, 3, 7), 
# policz ile razy występuje 7 i na jakim indeksie jest pierwszy raz.

liczby = (3, 7, 1, 9, 4, 7, 3, 7)
print(f'7 występuje: {liczby.count(7)} razy, pierwszy raz na indexie {liczby.index(7)}')

# 8.6 -- Napisz funkcje statystyki(lista), która zwraca krotkę 
# (min, max, średnia). Wywolaj ja i rozpakuj wynik.

def statystyki(lista):
    return min(lista), max(lista), round(sum(lista)/len(lista), 2)

stat = statystyki(liczby)

print(f'min: {stat[0]}, max: {stat[1]}, avg: {stat[2]}')

# 8.7 -- Mając krotkę owoce = ("jablko", "banan", "gruszka"), 
# dodaj do niej "kiwi" i "mango" (tworzac nowa krotkę).

owoce = ("jablko", "banan", "gruszka")
print(owoce + ('kiwi', 'mango'))


#########################################################################################
# Słowniki # Słowniki # Słowniki # Słowniki # Słowniki # Słowniki # Słowniki # Słowniki #
#########################################################################################


###################################
# Tworzenie słowników
###################################
 
slownik1 = {}
slownik2 = {'Maximum':46,"Minimum":2,"Count":24}
slownik3 = dict()
slownik4 = dict(Maximum=46,Minimum=2,Count=24)
lista_kro_34 = [('grusza',2),('jablko',6),('kasztan',6),('jastrzomb',6)]
slownik5 = dict(lista_kro_34)
listslownik6 = list(slownik5)


print(slownik1)
print(slownik2)
print(slownik3)
print(slownik4)
print(slownik5)
print(listslownik6)


#####################################
# Pętle ze słownikami
#####################################

lista_kro_34 = [('grusza',2),('jablko',6),('kasztan',6),('jastrzomb',6)]
slownik5 = dict(lista_kro_34)

for i in slownik5:
    print(i)

for i in slownik5.keys():
    print(i)

for i in slownik5.values():
    print(i)

for nazwa,wartosc in slownik5.items():
    print(f"Nazwa to: {nazwa}, Wartość to {wartosc}")


# *Stworzyli słownik zawierający imiona oraz wiek.
slownik = {'Alicja': 20, 'Katarzyna': 30, 'Marcelina': 40}
# *Przeiterowali przez niego dając wynik imie='', wiek='' używając items()
for ky,vl in slownik.items():
    print(f'imie:{ky}, wiek:{vl}')
# *Przeiterowali przez niego po wartościach i stworzyli z niego nową listę zawierającą szesciany 
# wartości słownika values()
print(list(map(lambda val: val**3, slownik.values())))
# *Przeiterowali prze niego po keys() i następnie wyświetlili imiona (duża litera pierwsza)-->title capitalize
for ky in slownik:
    print(f'imie:{ky.capitalize()}')

# działa
for ky,vl in slownik.items():
    print(f'imie:{ky}, wiek:{vl}')

# print(slownik.items())

# nie działa
# list1 = list(map(lambda ky,vl: f'imie={ky}, wiek={vl}',slownik.items()))
# działa, dwa argumenty podane -> lambda nie potrafi rozpakować 
list1 = list(map(lambda ky,vl: f'imie={ky}, wiek={vl}',slownik.keys(),slownik.values()))
print(list1)


#  Wyciągania wartości ze słowników 

slownik = {'name':'Magda','wiek':35,'zawod':'Kasjer','lata_pracy':10}


# sprawdzanie wartości klucza
print(slownik['name'])
# print(slownik['doswiadczenie']) #--> KeyError: 'doswiadczenie' --> error błąd nie ma takiego klucz

if 'doswiadczenie' in slownik:
    pass
# ....

# sprawdzanie wartości klucza .get()

print(slownik.get('doswiadczenie')) #--> zwraca None jak nie ma takiego klucza zamiast błędu
print(slownik.get('doswiadczenie','brak')) #--> własna wartość zamiast None

# Dodanie nowego klucza-wartosci jak nie ma takiego w słowniku
slownik['dzial'] = 'dział biura'
print(slownik)

# Edycja wartosci przypisanej do klucza jak istnieje
slownik['name'] = 'Dominika'
print(slownik)

slownik_2 = {'name':'Magda','wiek':35,'zawod':'Kasjer','lata_pracy':10,'name':'Anastazja'}
print(slownik_2)

# klucze zawsze są unikalne, nie powtarzają

# 9.1 -- Stwórz słownik samochod z kluczami: marka, model, rok, kolor. Wyświetl każda pare klucz-wartość.
cars = {'marka':'opel', 'model':'insignia', 'rok':'2020', 'kolor':'czarny'}
for i,j in cars.items():
    print(f'klucz:{i}, wartość:{j}')
print(cars)
# 9.2 -- Stwórz słownik oceny = {"Adam": 5, "Ola": 4, "Kasia": 3}. Pobierz ocene Adama przez [] i ocene 
# Bartka przez .get() z domyślna wartościa "brak".
oceny = {"Adam": 5, "Ola": 4, "Kasia": 3}
print(oceny['Adam'])
print(oceny.get('Bartek', 'brak'))


# Dodanie kilkunastu wartości w jednej linijce kodu 
cars = {'marka':'opel', 'model':'insignia', 'rok':'2020', 'kolor':'czarny'}
print(cars.keys())
cars.update(silnik='v8',spalanie_w_l=8,drzwi=5,marka='Audi')
print(cars.keys())

for i,k in cars.items():
    print(f"{i}-->{k}")

# Usuwanie ze słowników .pop del 

marka = cars.pop('marka')
print(marka)
przebieg = cars.pop('przebieg','brak')
# --> gdy klucza NIE ma, zwraca 'brak' zamiast błędu
# (bez 2. argumentu byłby KeyError); pop zwraca usuniętą wartość
print(przebieg)

# lista_brak = [23,4,5]
# pierwszy_z = lista_brak.pop(0,'brak') pop w lsitach przyjmuje tylko jeden argument działa tylko na słownikach default

del cars['spalanie_w_l'] #--> wywala na zawsze 
print(cars)
# del cars['343434'] #--> wywala błąd 

cars = {'marka':'opel', 'model':'insignia', 'rok':'2020', 'kolor':'czarny'}

print(cars)

cars.setdefault('marka','BMW') #--> setdefault ustawia wartosc do slownika tylko jesli nie ma danego klucza
cars.setdefault('silnik','V4')
print(cars)


# listowanie slownika
print(list(cars))
print(list(cars.keys()))
print(list(cars.values()))
print(list(cars.items()))


# **** list comp... --> dict compre
dict_compre = {x:x**3 for x in range(10)} # --> {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
print(dict_compre)


# *** Zagnieżdzenie słownika 

slownik_zagn = {'marka':'opel', 'model':'insignia', 'rok':'2020', 'kolor':{'bk':'black','sl':'silver','wh':'white'}}

# owoce[0][0]

print(slownik_zagn['kolor']['wh'])

# Iteracja z zagn

for i,k in slownik_zagn.items():
    print(f"{i}-->{k}")
    if i == 'kolor':
        for element,value in k.items():
            print(value)

# Kopiowanie słowników
a = {"x": 1, "y": 2}
# b = a  # TAK NIE ROBIMY TO JEST NADAL TEN SAM OBIEKT
b = a.copy()
b['z'] = 20
print(f"Słownik zmieniony {b}")
print(f"Oryginalny słownik {a}")


# Metoda łączenia dodatkowa 
a_dict = {"x": 1, "y": 2}
b_dict = {"y": 99, "z": 3}
z_dict = a_dict | b_dict
k_dict = b_dict | a_dict
# print(z_dict)
print(k_dict)


# 9.3 -- Mając słownik magazyn = {"jablka": 10, "banany": 5, "gruszki": 8}, dodaj "kiwi": 12, 
# zmien ilość bananow na 15, usun gruszki. Wyświetl po każdej operacji.

magazyn = {"jablka": 10, "banany": 5, "gruszki": 8}
magazyn['kiwi'] = 12
magazyn['banany'] = 15
# pop() del
del magazyn['gruszki']
print(magazyn)
gruszki = magazyn.pop('gruszki','brak')
print(gruszki)

# 9.6 -- Stwórz dwa słowniki: domyślne = {"kolor": "biały", "rozmiar": "M", "ilość": 1} 
# i zamówienie = {"kolor": "czerwony", "ilość": 3}. Połącz je tak, zeby zamówienie nadpisało domyślne wartości.

domyslne = {"kolor": "biały", "rozmiar": "M", "ilość": 1}
zamowienie = {"kolor": "czerwony", "ilość": 3}

nowy_slownik = domyslne | zamowienie
print(nowy_slownik)

# 9.8* -- Stwórz słownik uczniówie, który jest lista słowników: 
# [{"imie": "Adam", "ocena": 4}, {"imie": "Ola", "ocena": 5}, ...]. 
# Wyświetl tylko uczniów z ocena 5 lub wyższa.

slownik_osoby =  [{"imie": "Adam", "ocena": 4}, 
                  {"imie": "Ola", "ocena": 5}, 
                  {"imie": "Damian", "ocena": 3},
                  {"imie": "Olaf", "ocena": 2},
                  {"imie": "Rafał", "ocena": 5}]

for element in slownik_osoby:
    if element['ocena'] >= 5:
        print(f"{element['imie']}")

#############################################################################
# SET # SET # SET # SET # SET # SET # SET # SET # SET # SET # SET # SET # SET
#############################################################################

# Set (zbiór) zachowuje tylko unikalne elementy
set_example1 = {4,5,6,3,4,5}
print(set_example1) # --> zachowało tylko unikalne elementy
set_example2 = set()
set_example3 = {} # --> samo {} tworzy słownik, nie zbiór/set
# print(type(set_example2))
# print(type(set_example3))

# Tworzenie z list
lista_do_set = [2,5,4,3,6,4,5,2,2]
set_z_listy = set(lista_do_set)
print(set_z_listy)
z_setu_do_listy = list(set_z_listy)
print(z_setu_do_listy)
dict_do_set = {1:1,2:4,9:9,9:9}
z_dict_na_set = set(dict_do_set)
print(z_dict_na_set)
z_dict_na_set_val = set(dict_do_set.values())
print(z_dict_na_set_val)
z_dict_na_set_items = set(dict_do_set.items())
print(z_dict_na_set_items)
string_na_set = 'banana'
print(set(string_na_set))


# Sortowanie # --> Pułapka sorted() zwraca liste
set_z_listy = set(lista_do_set)
sort_set = sorted(set_z_listy)
print(set(sort_set)) #-->  set znów gubi kolejność!

# comprehension set
kwadraty = {x**2 for x in range(0,10)}
print(kwadraty)

# 10.1 -- Stwórz zbiór z listy [5, 3, 8, 3, 1, 5, 8, 2]. Wyświetl ile unikalnych elementów zawiera.
list1 = [5, 3, 8, 3, 1, 5, 8, 2]
set1 = set(list1)
print(f'Zbiór ma: {len(set1)} unikalnych elementów')
# 10.5 -- Mając string "abrakadabra", znajdz ile unikalnych liter zawiera i wyświetl je posortowane.
str1 = "abrakadabra"
set2 = set(str1)
print(f'Zbiór ma: {len(set2)} unikalnych liter')
print(f'Posortowany litery {sorted(set2)}')


# Modyfikacji zbiorów i metody
# tworzenie, dodawanie nowych do zbioru
# .add()

owoce = {"jablko", "banan"}
owoce.add('kasztan') #--> dodanie nowego elementu do zbioru
print(owoce)

# .update()
owoce.update(["kiwi", "mango", "jablko"])
print(owoce)
# owoce.update("kiw", "m", "ja") # --> rozdziela jak strin
# print(owoce)

# Usuwanie elementów ze zbioru remove() discard() pop()
# jablko = owoce.pop('jablko') --> nie przyjmuje żadnynch argumentów błąd
jablko = owoce.pop() #--> usuwa i zwraca DOWOLNY (nieokreślony) element — zbiór nie ma kolejności
print(jablko)
print(owoce)

# remove()
# owoce.remove('kiwi')
# owoce.remove('kiwi') # --> wywala błąd nie ma takiego elementu w zbiorze
print(owoce)

owoce.discard('mango')
print(owoce)


# 10.2 -- Stwórz zbiór kolory = {"czerwony", "zielony", "niebieski"}.
# Dodaj "zolty", usun "zielony", sprawdź czy "biały" jest w zbiorze.

#Rozwiązanie nr1.
kolory = {"czerwony", "zielony", "niebieski"}
kolory.add('zolty')
kolory.remove('zielony')
print(kolory)
print(bool(list(filter(lambda x: x == 'biały', kolory))))

# Rozwiązanie nr2.
kolory = {"czerwony", "zielony", "niebieski"}
kolory.add('zolty')
kolory.discard('zielony')       # discard nie wywala błędu, gdy elementu nie ma (remove by wywaliło)
print(kolory)
print('biały' in kolory)        # --> False, sprawdzenie obecności w zbiorze: szybkie i naturalne


# 10.7 -- Mając listę zakupy = ["mleko", "chleb", "maslo", "mleko", "jajka", "chleb", "ser", "mleko"],
# wyświetl unikalne produkty i ile bylo duplikatow.

zakupy = ["mleko", "chleb", "maslo", "mleko", "jajka", "chleb", "ser", "mleko"]
set1 = set(zakupy)
print(set1)
print(f'duplikatow: {len(zakupy) - len(set1)}')

# 10.6 -- Poproś użytkownika o zdanie. Policz ile unikalnych słów zawiera (ignorujac wielkość liter).

"""
sentence = input("podaj zdanie: ")
transformed_sentence = set(map(lambda w: w.upper(), sentence.split(' ')))
print(f'{transformed_sentence} ma {len(transformed_sentence)} unikalnych slow')
"""

######################################################################
# Zbiorów --> Operacje na zbiorach (difference / intersection / union)
######################################################################

#&&&&&&&&&&&&&&&&&&&&&&&
# difference
#&&&&&&&&&&&&&&&&&&&&&&&

a_set1 = {1, 2, 3, 4, 5}
b_set1 = {2, 3, 4, 5, 6, 7, 8}

diffe = a_set1 - b_set1
print(diffe)

#&&&&&&&&&&&&&&&&&&&&&&&
# symmetric_difference
#&&&&&&&&&&&&&&&&&&&&&&&

a_set2 = {1, 2, 3, 4, 5}
b_set2 = {4, 5, 6, 7, 8}
diffe_symm = a_set2 ^ b_set2 # --> wywala część wspólną obu zbiorów
print(diffe_symm)

#&&&&&&&&&&&&&&&&&&&&&&&
# intersection
#&&&&&&&&&&&&&&&&&&&&&&&

a_set3 = {1, 2, 3, 4, 5}
b_set3 = {4, 5, 6, 7, 8}
interse = a_set3 & b_set3 # --> tylko to co się pokrywa w obu zbiorach jest nam zwracane
print(interse)

#&&&&&&&&&&&&&&&&&&&&&&&
# union
#&&&&&&&&&&&&&&&&&&&&&&&

a_set4 = {1, 2, 3, 4, 5}
b_set4 = {4, 5, 6, 7, 8}

union = a_set4 | b_set4 #--> sumuje elementy, a jako, że to zbiór nie ma powtórzeń i duplikatów
print(union)


# Inne metody dodatkowe mozliwe do wykorzystania na zbiorach

a_set_1 = {1, 2, 3}
b_set_1 = {1, 2, 3, 4, 7 , 8}
c_set_1 = {6, 7}

print(a_set_1.issubset(b_set_1))      # True -- a jest podzbiorem b
print(b_set_1.issuperset(a_set_1))    # True -- b jest nadzbiorem a
print(a_set_1.isdisjoint(c_set_1))    # True -- brak wspólnych elementów

# frozenset -- niezmienny zbiór:

zamrozony = frozenset([1, 2, 3, 4, 5])
print(zamrozony)
# zamrozony.add(10)


# union | union
# intersection & intersection
# diff - diff
# sym_diff ^ sym_diff

# 10.3 -- Mając dwie listy: a = [1, 2, 3, 4, 5, 6] i b = [4, 5, 6, 7, 8, 9],
# znajdz wspólne elementy (intersection). --> &

a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8, 9]
print(set(a) & set(b))

# 10.4 -- Mając dwa zbiory uczniów: grupa_a = {"Adam", "Ola", "Kasia", "Bartek"} i
# grupa_b = {"Ola", "Zofia", "Bartek", "Darek"},
# znajdz: kto jest w obu grupach, kto jest tylko w A, kto jest w którejkolwiek.

grupa_a = {"Adam", "Ola", "Kasia", "Bartek"}
grupa_b = {"Ola", "Zofia", "Bartek", "Darek"}
print(f'Te osoby są w obu grupach {grupa_a & grupa_b}')
print(f'Te osoby są tylko w grupie A {grupa_a - grupa_b}')
print(f'Te osoby są w każdej grupie  {grupa_a | grupa_b}')
