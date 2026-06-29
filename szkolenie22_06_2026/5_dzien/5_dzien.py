# UWAGA: aby uruchomić CAŁY ten plik, trzeba mieć oczywiście zainstalowany psycopg2
# (pip install psycopg2) oraz oczywiście postawioną i działającą bazę PostgreSQL,
# bo połączenie conn = psycopg2.connect(...) wykonuje się przy starcie pliku.

###########################################################################################################
# Hermetyzacja Klasy # Hermetyzacja Klasy # Hermetyzacja Klasy # Hermetyzacja Klasy # Hermetyzacja Klasy #
###########################################################################################################
# **** 
# 1)Hermetyzacja = ukrywanie wewnętrznych danych obiektu i wystawianie ich tylko przez kontrolowany dostęp. 
# W Pythonie to konwencje, nie twarda blokada jak w Javie.

class Przyklad():
    def __init__(self):
        self.normalny = 'normalny'
        # self._normalny = 'prywatny' # --> inna nazwa _normalny != normalny
        self._chroniony = 'chroniony'   # pojedyncze _ = konwencja "chroniony" (protected)
        self.__prywatny = 'prywatny'    # podwójne __ = "prywatny" (name mangling)


przyklad = Przyklad()

print(f'Tutaj mamy przykład normalnego atrybutu "{przyklad.normalny}"')
print(f'Tutaj mamy przykład chronionego atrybutu "{przyklad._chroniony}"') # -> trzeba tutaj uważać
# print(f'Tutaj mamy przykład normalnego atrybutu "{przyklad._normalny}"')
# print(f'Tutaj mamy przykład prywatnego atrybutu "{przyklad.__prywatny}"') # -> 'Przyklad' object has no attribute '__prywatny'
print(f'Tutaj mamy przykład prywatnego atrybutu "{przyklad._Przyklad__prywatny}"') # --> name mangling: to NIE zamek, tylko zmiana nazwy (utrudnia dostęp + chroni przed kolizją nazw przy dziedziczeniu)

print(przyklad.__dict__)

# 2) Kontrolowany dostęp — @property (getter + setter z walidacją). Chowamy dane w __saldo, 
# a na zewnątrz wystawiamy „atrybut" 
# saldo, który pod spodem przechodzi przez metody — dzięki temu można dołożyć walidację:

class Konto:
    def __init__(self):
        self.__saldo = 1000

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, w):
        if w < 0:
            raise ValueError("Saldo nie może być ujemne!")
        self.__saldo = w

konto = Konto()
print(konto.saldo)     # 1000   (getter, bez nawiasów)
konto.saldo = 500      # setter (z walidacją)
print(konto.saldo)     # 500
konto.__saldo = 2000   # tworzy lewy atrybut, NIE rusza prawdziwego salda
print(konto.saldo)     # 500   (saldo bez zmian)
# konto.saldo = -1     # ValueError — setter odrzuca


import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres",
                         user="postgres", password="Password!")


# Tworzenie tabeli

# cur = conn.cursor()
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS klienci (
#         id SERIAL PRIMARY KEY,
#         imie VARCHAR(50) NOT NULL,
#         miasto VARCHAR(50),
#         saldo DECIMAL(10, 2) DEFAULT 0,
#         aktywny BOOLEAN DEFAULT TRUE
#     )
# """)
# conn.commit() 
# cur.close()
# conn.close()


# Napisz polecenie CREATE TABLE, które utworzy tabelę zwierzeta przechowującą następujące dane o każdym zwierzęciu:

# id — automatycznie nadawany numer, klucz główny,
# imie — tekst do 50 znaków, wymagany (nie może być pusty),
# gatunek — tekst do 50 znaków,
# pochodzenie — region pochodzenia (np. Azja), tekst do 50 znaków,
# wiek — liczba całkowita (lata).

# Dodanie jednego pojedyńczego inserta
"""
with conn:                       
    with conn.cursor() as cur:   
        cur.execute(          
            "INSERT INTO klienci (imie, miasto, saldo) VALUES (%s, %s, %s)",
            ("Anna", "Kraków", 1500)       
        )
"""


# Dodanie wielu insertów 
"""
klienci = [
("Jan", "Gdańsk", 800),
("Ola", "Warszawa", 2300),
("Marek", "Kraków", 0),
]

with conn:                       
    with conn.cursor() as cur:  
        cur.executemany(
            "INSERT INTO klienci (imie, miasto, saldo) VALUES (%s, %s, %s)",
            klienci
        )
"""

# SQL INJECTION --> gdy sklejamy zapytanie ze stringa (f-string/+), użytkownik może wstrzyknąć własne SQL:
# przerwać działanie inserta, dopisać złośliwe polecenie, usunąć całą kolumnę/tabelę itd.
# DLATEGO: NIGDY nie wklejamy danych do zapytania f-stringiem — wartości przekazujemy ZAWSZE jako parametry %s
# (psycopg2 sam je bezpiecznie escapuje), a nazwy kolumn/tabel przez psycopg2.sql.Identifier.


# SELECT zwrócenie jednego lub wielu elementów z tabeli

# with conn:                       
#     with conn.cursor() as cur:  
#         cur.execute(
#            "SELECT miasto,saldo FROM klienci"
#         )
#         # --> fetchone() --> tylko jeden
#         # --> fetchall() --> wszystkie 
#         pierwszy = cur.fetchone()
#         print(pierwszy)  
#         drugi = cur.fetchone()
#         print(drugi)  
#         wszyscy = cur.fetchall()
#         print(wszyscy) 


# Edytowanie za pomocą UPDATE

"""
saldo = 2000
id = 5

with conn:                       
    with conn.cursor() as cur:  
        cur.execute(
           "UPDATE klienci SET saldo = %s  WHERE id = %s",
           (saldo,id)
        )
"""

# Usuwanie za pomocą DELETE
"""
imie = 'Ola'

with conn:                       
    with conn.cursor() as cur:  
        cur.execute(
           "DELETE FROM klienci WHERE imie = %s",
           (imie,)
        )
"""

# operacje DDL (zmiana i kasowanie struktury tabeli)


# Rozwiązanie na sztywno z dodaniem kolumny
"""
with conn:                       
    with conn.cursor() as cur:  
        cur.execute(
           "ALTER TABLE klienci ADD COLUMN dzial VARCHAR(100)"
        )
"""
# LINE 1: ALTER TABLE klienci ADD COLUMN 'dział' VARCHAR(100) błąd jak przekazujemy stringa z nawiasami

# Rozwiązanie ze zmienną 
"""
def funkcja():
    import psycopg2.sql
    nazwa_kolumny = 'dział'
    with conn:                       
        with conn.cursor() as cur:  
            cur.execute(
psycopg2.sql.SQL("ALTER TABLE klienci ADD COLUMN {} VARCHAR(100)").format(psycopg2.sql.Identifier(nazwa_kolumny))
            )
funkcja()
"""


# Usuwanie kolumny z tabeli

# Rozwiązanie na sztywno z usunięciem kolumny
"""
with conn:
    with conn.cursor() as cur:
        cur.execute(
           "ALTER TABLE klienci DROP COLUMN email"
        )
"""

# Rozwiązanie ze zmienną 
"""
def funkcja():
    import psycopg2.sql
    nazwa_kolumny = 'email'
    with conn:                       
        with conn.cursor() as cur:  
            cur.execute(
psycopg2.sql.SQL("ALTER TABLE klienci DROP COLUMN {}").format(psycopg2.sql.Identifier(nazwa_kolumny))
            )
funkcja()
"""
# Zmiana nazwy kolumny 


# Rozwiązanie na sztywno ze zmianą nazwy kolumny
"""
with conn:
    with conn.cursor() as cur:
        cur.execute(
           "ALTER TABLE klienci RENAME COLUMN lokacja TO miasto"
        )
"""

# Rozwiązanie ze zmienną 
"""
def funkcja():
    import psycopg2.sql
    nks = 'lokacja'
    nkn = 'miasto'

    with conn:                       
        with conn.cursor() as cur:  
            cur.execute(
psycopg2.sql.SQL("ALTER TABLE klienci RENAME COLUMN {} TO {}").format(psycopg2.sql.Identifier(nks),psycopg2.sql.Identifier(nkn))
            )
funkcja()
"""

# -- TRUNCATE --> kasowanie danych z tabeli

# Rozwiązanie na sztywno z czyszczeniem tabeli
"""
with conn:
    with conn.cursor() as cur:
        cur.execute(
           "TRUNCATE TABLE klienci"
        )
"""

# Rozwiązanie ze zmienną 
"""
def funkcja():
    import psycopg2.sql
    tabela = 'klienci'

    with conn:                       
        with conn.cursor() as cur:  
            cur.execute(
psycopg2.sql.SQL("TRUNCATE TABLE {}").format(psycopg2.sql.Identifier(tabela))
            )
funkcja()
"""


# -- DROP --> USUNIĘCIE CAŁKOWITE TABELI

# Rozwiązanie na sztywno z usunięciem całej tabeli
"""
with conn:
    with conn.cursor() as cur:
        cur.execute(
           "DROP TABLE IF EXISTS klienci"
        )
"""

# Rozwiązanie ze zmienną 
"""
def funkcja():
    import psycopg2.sql
    tabela = 'klienci'

    with conn:                       
        with conn.cursor() as cur:  
            cur.execute( 
psycopg2.sql.SQL("DROP TABLE IF EXISTS {}").format(psycopg2.sql.Identifier(tabela))
            )
funkcja()
"""