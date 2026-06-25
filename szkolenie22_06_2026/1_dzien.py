################################################################################
# skroty klawiszowe # skroty klawiszowe # skroty klawiszowe # skroty klawiszowe#
################################################################################

# Ctrl '+' /	Wykomentowanie linijki
# Ctrl '+' C	Kopiowanie do schowka
# Ctrl '+' V	Wklejanie ze schowka
# Ctrl '+' S	Zapisz plik
# crtl '+' z cofanie zmian
# ctrl '+' y do przodu
# ctrl '+' + powiększenie okien
# ctrl '-' - pomniejszenie okien
# End	Kursor na koniec linii
# Home	Kursor na początek linii
# tab	przesuwanie dalej części kodu do przodu
# shift + tab	przesuwanie dalej części kodu do tyłu

################################################################################
# print na konsoli # print na konsoli # print na konsoli # print na konsoli # pr
################################################################################

print('python')

print('Hello wolrd')
print("Hello wolrd")
print('Hello "lakasda" ')

print("Książka \"Lalka\"") # --> '\"' w ten sposób wstawiamy cudzysłów
print("Książka \'Lalka\'") # --> "\'" w ten sposób wstawiamy apostrof
print("Książka 'Lalka' ")
print("Książka \t 'Lalka' ") # --> "\t" w ten sposób odsuwamy tekst
print("Książka \n 'Lalka' ") # --> "\n" przerzuca na kolejną linie
print("Książka", end='')
print(" Lalka") #--> string --> str

print("*"*50)

# 2.1 — Wyświetl swoje imię
print('Patrycja')
# 2.2 — Wyświetl imię ulubionej postaci, a w kolejnych liniach: nazwisko, wiek, ulubioną książkę (w cudzysłowie)
print('Wiktor\nWiesiołek\n18\n\"Harry Potter\"')
# 2.3* — Wyświetl liczbę 5, a następnie wyświetl w konsoli działanie dodawania 5 i 3
print('5')
print (5+3)

################################################################################
# działania na liczbach # działania na liczbach # działania na liczbach # działa
################################################################################

# int --> 5,10,4,3,29
# dodawanie
print(5+3)
# odejmowanie
print(5-3)
# mnożenie 
print(5*5)
# dzielenie
print(10/5) #--> zwraca nam zmiennoprzecinkową liczbę 3.0,12.25,6.5 --> float
print(11//5) #--> dzielenie bez reszty
print(11/5)

################################################################################
# działania na stringach # działania na stringach # działania na stringach # dzi
################################################################################
print("ala"*50) # --> mnożenie na str jest możliwe 
# print("ala"/8) # --> dzielenie nie działa na stringach
# print("ala" + 5) # --> dodawanie str do int nie działa
print('ala' + ' koniec') # --> dodawanie str działa
# print('ala' - 'ala') # --> nie str nie ma odejmowania


# 2.4 — Wykonaj w konsoli działanie 3 * 15 * 99 / 121 + 3
# 2.5 — Napraw: print("Teraz mamy przyzwolenie numer" + 593)
# 2.6 — Napraw: print("57" + 35)

# 2.4 — Wykonaj w konsoli działanie 3 * 15 * 99 / 121 + 3
print(3*15*99/121+3)
# 2.5 — Napraw: print("Teraz mamy przyzwolenie numer" + 593)
print("Teraz mamy przyzwolenie numer" +" 593")
# 2.6 — Napraw: print("57" + 35)
print(57 + 35)
print("57" +  " 35")

################################################################################
# zmienne # zmienne # zmienne # zmienne # zmienne # zmienne # zmienne # zmienne 
################################################################################
x = 54 #--> int
nasz_string = 'Dominik'
age = 25 #--> int

print('*'*200)
print(x,nasz_string,age)
print(x*age)

"""
nasz_wiek = input('Podaj swój wiek:') # input zawsze zwraca str
print(nasz_wiek*6) # 6*6=36    666666 --> mnożenie na stringach 
print(int(nasz_wiek)*6) # --> str(6) --> '6'
"""

print('#'*40)
print(x)
x = 70
print(x)

# 3.1 — Za pomocą input() zapytaj użytkownika ( o wybrany aspekt) 
# i go wyświetl#
"""
aspekt = input("Podaj wybrany aspekt: ")
print("Wybrany aspekt:", aspekt)
"""

# 3.2* — Za pomocą input() zapytaj o bok a i bok b prostokąta, 
# następnie oblicz pole P = a * b

"""
a = input("Podaj bok a prostokąta: ")
b = input("Podaj bok b prostokąta: ")
a = float(a) # --> zmiana stringa na float 
b = float(b)
pole = a * b
print("Pole prostokąta wynosi:", pole)
# print("Pole prostokąta wynosi:", a*b)
"""

print("Tutaj wynik:",x,"tutaj dalsza część opisu")
print(f"Tutaj wynik: {x} tutaj dalsza część opisu")
print(f'Tutaj wynik: {x} tutaj dalsza część opisu')

# print(X) # --> wielkość liter ma znaczenie

# imie --> first_name_person

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Cechy zmiennych
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# Można przypisać napisy i liczby, bool, listy,słwoniki....
# Wielkość liter ma znaczenie (name ≠ Name)
# Nazwy najlepiej po angielsku
# Kilka wyrazów łączymy w jeden ciąg (snake_case)
# Wartość zmiennej jest edytowalna


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# konwencja stylów 
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# Styl	        Przykład	Gdzie używany

# snake_case	moje_imie	Zmienne i funkcje w Pythonie
# camelCase	    mojeImie	JavaScript
# PascalCase	MojeImie	Nazwy klas w Pythonie

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Poprawne nazwy zmiennych
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#1 wiek                      # jeden wyraz
#2 first_name                # dwa wyrazy
#3 liczba_punktow_koncowych  # trzy wyrazy
#4 gracz1                    # wyraz + cyfra
#5 total_score_2             # wiele wyrazów + cyfra
#6 _prywatna_zmienna         # podkreślnik na początku
#7 max3_proby                # cyfra w środku

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Niepoprawne nazwy zmiennych
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#1 2gracz          # zaczyna się od cyfry
#2 imie studenta   # zawiera spację
#3 średnia_ocen    # polski znak (ś) --> pep-8 niezalecane
#4 moje-imie       # zawiera myślnik
#5 suma!punktow    # znak specjalny (!)
#6 class           # słowo zastrzeżone Pythona
#7 Imie_Studenta   # wielkie litery (PascalCase, nie snake_case)

Imie_studneta = 'sdsd' # ->> pep8

import keyword
print(keyword.kwlist)

# float = 5.7 # --> to może wywoływać błędy float()

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
# 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

################################################################################
# Typy zmiennych # Typy zmiennych # Typy zmiennych # Typy zmiennych # Typy zmien
################################################################################

# Typ	Opis	                    Przykład

# str	Tekst	                    "Alicja ma kota" ''
# int	Liczba całkowita	        23, -74
# float liczba zmiennoprzec         5.6, 2.56
# bool  prawda,fałsz                False, True


# SPrawdzili type() na różnych typach danych
x = 78
x = 50
y = False
z = 4.5
zy = "Ala ma kota"
print(type(x))
print(type(y))
print(type(z))
print(type(zy))


# nasze floaty to często mamy jakiś brzydki wynik:

# Zaokrąglanie floatów

float_example_1 = 8.564534

print(float_example_1)
print(round(float_example_1,2)) # --> round(liczba_zmiennoprzecinkowa, liczb miejsc po przecinku)
print(round(float_example_1,4)) 
print(f"{float_example_1:.2f}") # --> działanie na stringu


# 3.3 — Stwórz zmienne: imie (str), wiek (int), waga (float). Wyświetl je w jednym zdaniu 
# za pomocą f-stringa. Oczekiwany wynik: Mam na imie Adam, mam 25 lat i waze 75.5 kg
name = 'Adam'
age = 25
weight = 75.5
print(f'Mam na imię {name}, mam {age} lat i waze {weight} kg')
# 3.6 — Poproś użytkownika o dwie liczby (input). Oblicz i wyświetl: 
# sumę, różnicę, iloczyn oraz iloraz (z dokładnością do 2 miejsc po przecinku).

#Rozwiązanie nr1.
"""
a = float(input('a: '))
b = float(input('b: '))
print(f'suma: {round(a+b,2)}, iloczyn: {round(a*b,2)}, iloraz: {round(a/b,2)}')
"""

#Rozwiązanie nr2.
"""
liczba_1 = float(input("Podaj pierwszą liczbę: "))
liczba_2 = float(input("Podaj drugą liczbę: "))
suma = liczba_1 + liczba_2
roznica = liczba_1 - liczba_2
iloczyn = liczba_1 * liczba_2
iloraz = liczba_1 / liczba_2
print(f"Suma: {suma:.2f}")
print(f"Różnica: {roznica:.2f}")
print(f"Iloczyn: {iloczyn:.2f}")
print(f"Iloraz: {iloraz:.2f}")
"""

# 3.8A — BMI = masa / (wzrost * wzrost). Napisz program, który odbierze od użytkownika jego 
# masę w kilogramach i wzrost w metrach, wyliczy i wypisze BMI.

#Rozwiązanie nr1.
"""
weight = float(input('podaj masę [kg]: '))
high = float(input('podaj wzrost [m]: '))
print(f'BMI: {round(weight/(high*high), 2)}')
"""

#Rozwiązanie nr2.
"""
masa = float(input("Podaj masę w kilogramach: "))
wzrost = float(input("Podaj wzrost w metrach: "))
bmi = masa / (wzrost * wzrost)
print(f"Twoje BMI wynosi: {bmi:.2f}")
"""

################################################################################
# Instrukcje warunkowe # Instrukcje warunkowe # Instrukcje warunkowe # Instrukcj
################################################################################

# operatory porównania
# > < >= <= != ==

# Operator	Znaczenie	Przykład	Wynik
# ==	Równe	            5 == 5	    True
# !=	Różne (nierówne)	5 != 3	    True
# >	    Większe	            5 > 3	    True
# <	    Mniejsze	        5 < 3       False
# >=	Większe lub równe	5 >= 5	    True
# <=	Mniejsze lub równe	3 <= 5	    True


print(5 == 5)
age = 18 

# Przypadek 1 warunku
if age == 18:
    print('Wiek tej osoby jest równy 18 lat')

# Przypadek co robić jak nie zgadza się warunek
if age == 20:
    print('Wiek tej osoby to 20 lat')
else:
    print('Wiek tej osoby to nie jest 20 lat')

# Przypadek kilku warunków

if age == 20:
    print('Wiek tej osoby to 20 lat')
elif age == 18:
    print('Wiek tej osoby jest równy 18 lat')
elif age == 60:
    print('Wiek tej osoby jest równy 60 lat')
else:
    print('Wiek się nie zgadza')

is_tak = 'tak'
if age == 18 and is_tak == 'tak':
    print(f"Wiek się zgadza i bilet użytkownik posiada")


# 4.2 — Poproś użytkownika o liczbę. Sprawdź czy jest dodatnia, ujemna czy równa zero. 
# Wyświetl odpowiedni komunikat.
"""
a = int(input('Podaj liczbę: '))
if a > 0:
    print('Liczba dodatnia')
elif a < 0:
    print('Liczba ujemna')
else:
    print('Liczba 0')
"""

"""
liczba = int(input('Wpisz liczbę: '))
if liczba > 0:
    print('Liczba jest dodatnia.')
if liczba < 0:
    print('Liczba jest ujemna')
if liczba == 0:
    print('liczba jest rowna 0')
"""

"""
a = int(input('Podaj liczbę: '))
if a > 0:
    print('Liczba dodatnia')
elif a == 0 :
    print('Liczba 0')
else:
    print('Liczba ujemna')
"""

# 4.4 — Poproś użytkownika o temperaturę. Jeśli jest powyżej 30 — wyświetl Gorąco, jeśli 
# między 15 a 30 — Przyjemnie, jeśli poniżej 15 — Zimno.

"""
temp = float(input('Podaj temperaturę: '))
if temp > 30:
    print('Goraco')
elif temp < 15:
    print('Zimno')
else:
    print('Przyjemnie')
"""

"""
temp = float(input('Podaj temperaturę: '))
if temp >= 30:
    print(' goraco')
elif temp >= 15 and temp < 30:
    print('Przyjemnie')
else:
    print('Zimno') 
"""

# 4.5 — Poproś użytkownika o hasło. Jeśli hasło to "admin123" — wyświetl Zalogowano, 
# w przeciwnym razie Błędne hasło.

"""
passwd = input('Podaj haslo: ')
if passwd == 'admin123':
    print('Zalogowano')
else:
    print('Bledne haslo')
"""

# 4.6 — Poproś użytkownika o wiek i czy ma bilet (tak/nie). Jeśli ma 18+ i ma bilet — 
# wyświetl Wejście dozwolone. W przeciwnym razie Brak wejścia. Użyj and.

"""

# !!!!! Pułapka bool sprawdza, czy jest jakaś wartość, nie konwertuje, czy True, czy False
age = int(input('Podaj wiek: '))
has_ticket = bool(input('Czy masz bilet [true/false]: ')) # --> warunek has_ticket z bool samo sprawdzenie
print(has_ticket)


if age >= 18 and has_ticket == True:
    print('Wejscie dozwolone')
else:
    print('Brak Wejscia')
"""

"""
wiek = int(input('Podaj wiek?: '))
bilet = input('Czy masz bilet?: ')
if wiek >= 18 and bilet == 'Tak':
    print('Miejsce dozwolone:')
else:
    print('Brak wejscia')
"""

#################################################################################
# Operatory logiczne # Operatory logiczne # Operatory logiczne # Operatory logicz
#################################################################################

# and  --> ten i ten warunek spełniony
# or   --> ten albo ten warunek spełniony 

"""
wiek = int(input('Podaj wiek?: '))
bilet = input('Czy masz bilet?: ')
if wiek >= 18 and bilet == 'Tak':
    print('Miejsce dozwolone:')
else:
    print('Brak wejscia')
"""

# Przepisać ten warunek albo 18 lat albo posiada bilet

# age = float(input("Podaj wiek:"))
# bilet = input("masz bilet? (tak/nie):")
# if age >=18 or bilet =="tak":
#     print("wejście dozwolone")
# else:
#     print("Brak wejścia")

string_example = None

if string_example:
    print('Jest string')
if not string_example: # --> operator logiczny not --> None w string_example
    print('nie ma stringu')

# 4.10A — Rozbuduj swój program do BMI w taki sposób, by poza wyświetleniem obliczonego 
# BMI wyświetlił nam również odpowiedni opis wg skali z Wikipedii.

"""
height_1= float(input("podaj swój wzrost w metrach:"))
weight_2= float(input("podaj swoją wagę w kilogramach:"))
bmi_calculated = round(weight_2/(height_1*height_1),2)
if bmi_calculated < 16.0:
    print(f"Twoje BMI {bmi_calculated} - wygłodzenie")
elif bmi_calculated >=16.0 and bmi_calculated <16.99:
    print(f"Twoje BMI {bmi_calculated} - wychudzenie")
elif bmi_calculated >=17.0 and bmi_calculated <18.49:
    print(f"Twoje BMI {bmi_calculated} - niedowaga")
elif bmi_calculated >=18.5 and bmi_calculated <24.99:
    print(f"Twoje BMI {bmi_calculated} - pożądana masa ciała")
elif bmi_calculated >=25.0 and bmi_calculated <29.99:
    print(f"Twoje BMI {bmi_calculated} - nadwaga")
elif bmi_calculated >=30.0 and bmi_calculated <34.99:
    print(f"Twoje BMI {bmi_calculated} - otyłość I stopnia")
elif bmi_calculated >=35.0 and bmi_calculated <39.99:
    print(f"Twoje BMI {bmi_calculated} - otyłość II stopnia")
else: 
    print(f"Twoje BMI {bmi_calculated} - otyłość III stopnia")
"""


#################################################################################
# Pętle # Pętle # Pętle # Pętle # Pętle # Pętle # Pętle # Pętle # Pętle # Pętle #
#################################################################################


# Rozróniamy w pythonie dwa rodzaje pętli 

# 1 pętla while
# 2 pętla for 

# Pętla while
"""
i = 1
while i <= 10:
    print('Wykonuję pętle')
    print(i)
    # i = i + 1 
    i += 1 # --> ten proces incrementacja
"""

"""
odpowiedz = True
while odpowiedz:
    x = input('Daj tak, żeby skończyć pętlę:')
    if x == 'tak':
        odpowiedz = False
"""


# pętle for 

str_example = 'Python'

# P Y T H O N
# 0 1 2 3 4 5

for i in str_example:
    print(i)

# --> range(5) range(1,11) 
# range(start,stop,step)

# for i in range(1,11):
#     print(i)

for i in range(1,11,2):
    print(i)

# for index,i in enumerate(range(1,11,2)):
#     print(f"Index:{index} --> i: {i}")

for index,i in enumerate(range(1,11,2),start=1):
    print(f"Index:{index} --> i: {i}")


# Pętla zagnieżdzona: 
for i in range(1,11):
    for k in range(1,11):
        print(f"Wynik mnożenia {i}*{k}-->{i*k}")


# Pętla lista:
lista_example = [6,3,4,9,1,4,5] # przykład listy 

for element in lista_example:
    print(f"{element} jest elementem listy lista_example")

# Instrukcja break na zasadzie lista_example -->

for element in lista_example:
    if element == 4:
        print(f"{element} wywala 4, koniec pętli")
        break
    print(f"{element} jest elementem listy lista_example")
        
# Instrukcja warunkowa continue

# % 2 == 0 --> modulo sprwadza, czy liczba jest parzysta
lista_example = [6,3,4,9,1,4,5] 

for element in lista_example:
    if element % 2 == 0:
        continue
    print(f"{element} jest elementem listy lista_example")


# 5.4 — Wyświetl tabliczkę mnożenia dla liczby 7 (od 7x1 do 7x10) za pomocą pętli for.

for n in range(7,11):
    for i in range(1,11):
        print( f'Mnozenie {n}*{i} -->{n*i}')

for n in range(1,11):
    print(f"Mnożenie {n} x {7} = {n*7}")

# 5.5 — Poproś użytkownika o hasło. Daj mu maksymalnie 3 próby. Jeśli wpisze poprawne ("admin123") — 
# wyświetl Zalogowano i przerwij pętlę (break). Jeśli nie trafi — Brak prób.

#Rozwiązanie nr1
"""
max_attempt = 3
correct_passwd = 'admin123'
for i in range(1,max_attempt+1):
    passwd = input(f'Podaj haslo, proba {i}: ')
    if(passwd == correct_passwd):
        print('Zalogowano')
        break
    elif(i == max_attempt):
        print('Brak prob')
"""

#Rozwiązanie nr2
"""
haslo = "admin123"
proby = 3
for i in range(proby):
    podane = input("Podaj haslo:")
    if podane == haslo:
        print("zalogowano")
        break
    else:
        print("Niepoprawne haslo")
"""

# 5.6 — Wyświetl wszystkie liczby od 1 do 20, ale pomiń (continue) te, które dzielą się przez 3. !(modulo)

for i in range(1,20+1):
    if i % 3 == 0:
        continue
    print(i)


###############################################################################################################
# Łańcuchy znaków # Łańcuchy znaków # Łańcuchy znaków # Łańcuchy znaków # Łańcuchy znaków # Łańcuchy znaków ###
###############################################################################################################

# Funkcje wbudowane:
# – upper
# – lower
# – title
# – len w kontekście ciągów tekstowych
# – replace
# – count
# – strip
# – split i join - zamiana tekstu na listę i listy na tekst

# Łańcuch znaków jest przykładowo 'Python' --> str

string_example = '          AlA mA kOta i pSa w doMu roDziNnym        '

print(string_example) # bez formatowania
print(string_example.upper())               # -> tylko duże litery
print(string_example.lower())               # -> tylko małe litery
print(string_example.title())               # -> tylko pierwsz litera duża dla każdego słowa
print(string_example.capitalize())          # -> tylko pierwsz litera pierwszego słowa w zdaniu
print(string_example.swapcase())            # -> odwraca wielkości liter 
print(string_example.strip())               # -> Usuwa białe znaki z obu stron
print(string_example.lstrip())              # -> Usuwa białe znaki z lewej strony
print(string_example.rstrip())              # -> Usuwa białe znaki z prawej strony
print(string_example.count('doMu'))         # -> wielkość liter ma znaczenie szuka wystąpienia
print(string_example.replace('pSa','koTa'))

print(len(string_example))           # -> len zwraca długość 


nowa_lista = string_example.split(' ')
print(nowa_lista)
powrot_stringa = (' ').join(nowa_lista)
print(powrot_stringa)

"""
okazja = input("Wypisz 'tak' jeśli chcesz przejść dalej:")

if okazja.lower() == 'tak':
    print('przeszedłem')
"""

"""
# Funkcje i metody 
# Funkcja ---> funkcja()
# Metody --->  .metoda()

def elementy_sortowanie():
    pass
    # ssgdfgdfg....
    # ....
    # ...

print(type(elementy_sortowanie))
"""

##########################################################################################################
# Łańcuchy funkcji # Łańcuchy funkcji # Łańcuchy funkcji # Łańcuchy funkcji # Łańcuchy funkcji # Łańcuchy 
##########################################################################################################

# Łańcuchom - chaining 
nowa_lista = string_example.strip().lower().split()
print(nowa_lista)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  Iterowanie po łańcuchach tekstowych
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

iterable_string = 'Python'

for i in iterable_string:
    print(f"Element {i} stringa {iterable_string}")

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  – Mnożenie tekstu. Ale jak?
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

x = 'OdDo'

print(x*8)

# Weź string '    Amunicja gruSZka jaBlko wiSnia ananas   '
# Zamień metodą replace amunicja na 'agrest'
# wypisz wszystko z małych liter
# usuń białe spacje
# za pomocą metody split() dodaj elementy do listy nowej pod zmienna lista_nowa_owoce
# utworz nowy string za pomoca lista_nowa_owoce przy pomocy separatora ';'


tekst = '    Amunicja gruSZka jaBlko wiSnia ananas  '
tekst = tekst.replace('Amunicja', 'agrest').lower().strip()
print(tekst)
lista_nowa_owoce = tekst.split()
print(lista_nowa_owoce)
nowy_string = ';'.join(lista_nowa_owoce)
print(nowy_string)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  Wygodne sprawdzanie czy tekst zawiera frazę
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

przyklad_banan = 'W ulicy w sklepie jest banan'

if 'banan' in przyklad_banan:
    print(f"Banan jest w stringu")

# .isalpha()       — czy same litery
# .isdigit()       — czy same cyfry
# .isalnum()       — czy litery i/lub cyfry
# .isspace()       — czy same białe znaki
# .islower()       — czy wszystkie litery małe
# .isupper()       — czy wszystkie litery wielkie
# .istitle()       — czy każde słowo z wielkiej
# .isnumeric()     — czy same znaki numeryczne
# .isidentifier()  — czy poprawna nazwa zmiennej
# .startswith(x)   — czy zaczyna się od x
# .endswith(x)     — czy kończy się na x

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# – Czy Python>Java?
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

print('python'>'java')

# w pythonie > < etc. działa na zasadzie znaków  #unicode 
# p małe lub P duże zwraca nam inny unicode przez co jest możliwe sprawdzanie > <

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# – Cięcia, cięcia - o cięciu łańcuchów tekstowych słów kilka
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# 'Kot ma umaszczenie białe'
#  k| o |t |  |m |a |  |u |m |a  |s  |z  |c  |z  |e  |n  |i  |e  |   |b  |i  |a  |ł  |e
#  0| 1 |2 |3 |4 |5 |6 |7 |8 |9  |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23
kot =  'Kot ma umaszczenie białe'

print(f"{kot[0]}") #->wyprintowac 1 znak
print(f"{kot[7]}")
# print(f"{kot[30]}") #-> index ponad string
print(f"{kot[-1]}") #-> ostatniego elementu

# Slicing --> range(start,end,step)
# [start:end:step]
print(f"{kot[4:]}") # -> slicing ze startem
print(f"{kot[4:18]}") # -> slicing start, koniec
print(f"{kot[-2:]}") # -> dwa ostyatnie element
print(f"{kot[-9:-2]}") # -> slicing po indexach ujemnych
print(f"{kot[::2]}") # -> co drugi element 


# maskowanie numeru karty
karta = "1234567890123456"
zamaskowana = "****-****-****-" + karta[-4:]
print(zamaskowana)   # ****-****-****-3456

# sprawdźanie palindromu
słowo = "kajak"
print(słowo == słowo[::-1])   # True


imie = "Adam"
wiek = 25

print(f"{imie:<20}")     # Adam                 -- wyrównaj do lewej
print(f"{imie:>20}")     #                 Adam -- wyrównaj do prawej
print(f"{imie:^20}")     #         Adam         -- wyśrodkuj
print(f"{imie:*^20}")    # ********Adam******** -- wyśrodkuj z gwiazdkami


print(f"{1000000:,}")    # 1,000,000 -- separator tysięcy


##########################################################################################################
# Listy # Listy # Listy # Listy # Listy # Listy # Listy # Listy # Listy # Listy # Listy # Listy # Listy ##
##########################################################################################################

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# – Tworzenie list Tworzenie list Tworzenie list Tworzenie list
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Jeśli chodzi listy mieszane to staramy się ich unikać 
# sum(), max()

lista_mieszana  = ['python',56,3.6,True,'Dam','Rometa']
lista_liczbowa  = [6,4,7,3,4,5.7]
lista_stringowa = ['gruszka','jabłko','ananas','agrest']

lista_nowa = []
lista_nowa_dwa = list()  #-> int() bool() str()
lista_nowa_trzy = list(range(0,11))
print(lista_nowa_trzy)
lista_nowa_cztery = [i for i in range(0,11)] #--> list comprehension
print(lista_nowa_cztery)
lista_nowa_piec = [i for i in range(0,11) if i % 2 == 0 ] #--> list comprehension
print(lista_nowa_piec)

# Modulo --> modulo to ogólnie reszta z dowolnego dzielenia


lista_nowa_kwadraty = [i**2 for i in range(0,11) if i % 2 == 0 ] #--> list comprehension

"""
for i in lista:....
    if % 2 ==00....
"""


#  kwadrat każdego elementu

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Pobieranie wartości z list Pobieranie wartości z list Pobieranie wartości z list
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


owoce = ['gruszka','banan','agrest','jablko','ananas']

# |0          |1          |2          |3       |4
# |gruszka    |banan      |agrest     |jablko  |ananas

# pobieranie wartości:
# wyświetl 1 element
# wyświetl ostatni element
# wyświetl ostatnie 3 elementy
# Nie znasz ile elementów w liscie wyświetl wszystkie startujac od 2
# Wyświetl slicing od 1 elementu do ostatniego z krokiem 2 

el1 = owoce[0]
elLast = owoce[-1]
elLast3 = owoce[-3:]
elFrom2 = owoce[1:]
elBy2 = owoce[0::2]

print(el1)
print(elLast)
print(elLast3)
print(elFrom2)
print(elBy2)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Iterowanie po listach Iterowanie po listach Iterowanie po listach Iterowanie po li
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


lista_num = [5,7,3,5,7,3,4,6,2,21,9,4]

# a)wrzuć listę w pętlę, Przeiteruj przez nią i wyświetl tylko dla liczb nieparzystnych mnożenie tej cyfry 
# przez sztywną liczbę 10
# b) zrób to samo co dla a, tylko dla co drugiego elementu używając slicingu


# a) 
for i in lista_num:
    if i % 2 != 0:
        print(f"Mnożenie wartości {i} z {10} --> {i*10}")

# b)
for i in lista_num[::2]:
    if i % 2 != 0:
        print(f"Mnożenie wartości {i} z {10} --> {i*10}")


# enumerate()

lista_a = ['Damian','Andrzej','Rafał']
lista_b = [36,27,47,87]

for i,k in zip(lista_a,lista_b): # zip łączy elementy parami i kończy na krótszej liście (87 zostanie pominięte)
    print(f"Imię:{i},Wiek:{k}")




#Zagnieżdzenie list 
lista_zagn = [[2,6,3,4],['lista','zakupy','prad'],[6.5,4.6,3.7],[False,True,False]]

print(lista_zagn[0][0:]) # dostanie się do zagn po indexie

for i in lista_zagn:
    print(f"lista {i}")
    for k in i:
        print(f'Element {k}')

# pandas numpy --> biblioteki --> 

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Sprawdzanie czy element znajduje się na liście Sprawdzanie czy element znajduje si
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

lista_name = ['Damian','Andrzej','Rafał']

if 'Damian' in lista_name:
    print(f"Znajduje się imie w liście")

print('Damian' in lista_name)

if 'Batista' not in lista_name:
    print(f"Nie znajduje się imie w liście")

print('Batista' not in lista_name)


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Modyfikowanie zawartości listy Modyfikowanie zawartości listy Modyfikowanie zawart
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dodawanie nowych wartości i wstawianie w miejsce istniejących 
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# listy mają takie methody jak .append() .extend() .insert()

print("&"*40)
owoce = ['gruszka','banan','agrest','jablko','ananas']
print(owoce)
owoce[0] = 'wisnia' # podmiana 1 elementu na 'wisnia'
print(owoce)
# owoce[1:3] = 'czajnik' # trzeba dać nawias jeśli ma być jako jeden element 
owoce[1:3] = ['czajnik']
print(owoce)

owoce.append('czeresnia') #--> dodaje element na sam koniec
print(owoce)
owoce.append(['abc','cda']) # --> jeśli w appendz jest więcej wartości w to daje jako zagnieżdzoną
print(owoce)
owoce.extend(['abcd','degs']) # --> dodaje kilka elementów na koncu listy osobno
print(owoce)
owoce.insert(0,'granat')
print(owoce)


# owoce.remove('czeresnia') --> remove()
# 7.3 -- Stwórz listę imion. Dodaj nowe imie na koniec (append), wstaw jedno na pozycję 2 
# (insert), usun jedno po wartości (remove). Wyświetl listę po każdej operacji.

names = ['Alicja', 'Barbara', 'Agniszka', 'Aleksandra']
names.append('Michal')
print(names)
names.insert(1, 'Wojciech')
print(names)
names.remove('Agniszka')
print(names)


# !!!import random 
# !!!random.randint(1, 10) # --> losuje jedna liczbę pomiedzy 1 a 10

# 7.10A -- Stwórz dwie listy. Kazda z list ma zawierac 10 liczb losowych z zakresu 1-10. 
# Połącz te dwie listy do jednej i wyświetl na konsoli (extend albo +).

import random 
print(random.randint(1, 10))

lista_pierwsza = [random.randint(1, 10) for i in range(10)]
print(lista_pierwsza)
lista_druga = [random.randint(1, 10) for _ in range(10)]
print(lista_druga)

print(zip(lista_pierwsza,lista_druga))

nowa_lista = []
for i,k in zip(lista_pierwsza,lista_druga):
    nowa_lista.append(i)
    nowa_lista.append(k)
    # nowa_lista.extend([i,k])

for index,k in enumerate(range(10)):
    pass

print(nowa_lista)

print(list(zip(lista_pierwsza,lista_druga))) # --> sprawia problemy jeśli nie chcielibyśmy mieć zagnieżdzenia

nowa_lista_ext = lista_pierwsza[:]
nowa_lista_ext.extend(lista_druga)
print(nowa_lista_ext)

nowa_lista_plus = lista_pierwsza + lista_druga
print(nowa_lista_plus)

print(bool())
print(bool(''))
print(bool('False'))
print(bool('True'))

# int() str()
