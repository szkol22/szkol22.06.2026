CREATE TABLE IF NOT EXISTS klienci (
    id SERIAL PRIMARY KEY,            -- auto-numer, klucz główny
    imie VARCHAR(50) NOT NULL,        -- tekst do 50 znaków, wymagany
    miasto VARCHAR(50),               -- tekst do 50 znaków
    saldo DECIMAL(10, 2) DEFAULT 0,   -- kwota z 2 miejscami po przecinku, domyślnie 0
    aktywny BOOLEAN DEFAULT TRUE      -- TRUE/FALSE, domyślnie TRUE
);


-- CREATE TABLE --> tworzenie tabeli
-- IF NOT EXISTS -->  zablokowanie tworzenia jak tabela o podanej nazwie istnieje
-- () wartosci/ kolumny jakie ma mieć tabela
-- serial -> incrementacja sama z siebie id przy dodawaniu do tabeli


-- Jak wyswietlic dane z tabeli

SELECT * FROM klienci;


-- Dodawania danych do tabeli

INSERT INTO klienci (imie, miasto, saldo)
VALUES ('Anna', 'Kraków', 1500);

-- Insert Into 
-- nazwa tabeli
--(nazwa_kolumny1,nazwa_kolumny2,....)
-- VALUES (wartosc,wartosc2,...)


-- insert dla wielu osób
INSERT INTO klienci (imie, miasto, saldo) VALUES
    ('Jan', 'Gdańsk', 800),
    ('Ola', 'Warszawa', 2300),
    ('Marek', 'Kraków', 0);

-- Select wszystkich kolumn
SELECT * FROM klienci;

-- Wyswietlanie tylko kilku kolumn
SELECT miasto,saldo FROM klienci;


-- SELECT misto,saldo FROM klienci; błędne nazwy kolumn
--SELECT miasto,saldo, FROM klienci; syntax error at or near "FROM"

-- SELECT Z WARUNKIEM

SELECT * FROM klienci WHERE miasto = 'Kraków'; -- Tylko krakowianie

-- SELECT Z warunkami
SELECT * FROM klienci WHERE miasto = 'Kraków' AND imie = 'Anna';


SELECT * FROM klienci WHERE miasto = 'Kraków' AND saldo > 100; -- Krakowianie z saldem > 100

--SELECT po niepełnej nazwie 
SELECT * FROM klienci WHERE imie LIKE  '%nna%';
SELECT * FROM klienci WHERE imie LIKE  '%nna';
SELECT * FROM klienci WHERE imie LIKE  'nna';
SELECT * FROM klienci WHERE imie LIKE  'Anna';

--SELECT po id unikalnym
SELECT * FROM klienci WHERE id = 5;


-- Edycja wartości kolumn z tabeli
SELECT * FROM klienci;

-- UPDATE klienci SET aktywny = false; -- Zmienia wszystkie na false --> brak warunku
-- UPDATE klienci SET aktywny = true; -- Zmienia wszystkie na true --> brak warunku

UPDATE klienci SET saldo = 40000 WHERE id = 3;

-- UPDATE
-- nazwa tabeli
-- SET
-- co zmieniamy(jakie wartosci)
-- warunek(inaczej zmieni dla wszystkich wierszy)


SELECT * FROM klienci WHERE id = 5;


-- Delete Usuwanie wierszy z tabeli

SELECT * FROM klienci;

--DELETE FROM klienci; --> czyści całą tabele bez warunku


DELETE FROM klienci WHERE saldo = 0;

-- DELETE
-- FROM
-- nazwa tabeli
-- warunek(inaczej usuwa każdy wiersz)

-- DELETE,FROM,SELECT,WHERE z duzych liter
-- nazwy_kolumn, nazwy_tabeli z małych


--DDL


SELECT * FROM klienci;


--ALTER TABLE -- zmiana struktury istniejącej tabeli (dodanie/usunięcie/zmiana kolumny):


-- nową kolumnę dodać
ALTER TABLE klienci ADD COLUMN email VARCHAR(100);
-- ALTER TABLE
--nazwa tabeli
-- ADD COLUMN
-- nazwa kolumny
-- typ kolumny


SELECT * FROM klienci;


-- USUniecie kolumny 
ALTER TABLE klienci DROP COLUMN email;
--ALTER TABLE
-- nazwa tabeli
-- DROP COLUMN
-- nazwa kolumny

SELECT * FROM klienci;


-- Nazwanie inaczej kolumny
ALTER TABLE klienci RENAME COLUMN miasto TO lokacja;
--ALTER TABLE
--nazwa tabeli
--RENAME COLUMN
--nazwa kolumny,którą chcemy zmienić
--TO
--nazwa kolumny jaką chcemy przypisać

SELECT * FROM klienci;


-- Truncate -- błyskawicznie czyści wszystkie dane, ale zostawia tabelę 
--(pustą strukturę). Szybsze niż DELETE:
TRUNCATE TABLE klienci;
--TRUNCATE TABLE
-- nazwa tabeli

SELECT * FROM klienci;

-- DROP --> USUNIĘCIE CAŁKOWITE TABELI
DROP TABLE IF EXISTS klienci;

SELECT * FROM klienci;