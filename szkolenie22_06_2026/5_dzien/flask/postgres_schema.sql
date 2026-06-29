-- ============================================================================
-- WAZNE: zeby aplikacja Flask (main.py) w ogole dzialala, trzeba NAJPIERW
-- przygotowac baze PostgreSQL:
--   1. Postawic/uruchomic baze, do ktorej laczy sie get_db() w main.py
--      (host=localhost, dbname=postgres, user=postgres, password=Password!).
--   2. Wykonac ponizsze CREATE TABLE (obie tabele: szkolenie_users i szkolenie_todos).
--   3. ODKOMENTOWAC i wykonac INSERT-y na dole pliku (uzytkownik testowy + zadania),
--      bo bez konta anna@test.pl / haslo123 nie da sie zalogowac do aplikacji.
-- Bez tych trzech krokow Flask wyrzuci blad "relation ... does not exist" / brak logowania.
-- ============================================================================

-- TABELA: szkolenie_users (logowanie do aplikacji)
CREATE TABLE IF NOT EXISTS szkolenie_users (
    id SERIAL PRIMARY KEY,
    imie VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    haslo VARCHAR(255) NOT NULL,
    data_rejestracji TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- TABELA: szkolenie_todos (zadania przypisane do uzytkownika)
CREATE TABLE IF NOT EXISTS szkolenie_todos (
    id SERIAL PRIMARY KEY,
    tytul VARCHAR(200) NOT NULL,
    opis TEXT,
    wykonane BOOLEAN DEFAULT FALSE,
    data_dodania TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uzytkownik_id INTEGER REFERENCES szkolenie_users(id) ON DELETE CASCADE
);


SELECT * FROM szkolenie_users;
SELECT * FROM szkolenie_todos;

-- Uzytkownik testowy
-- INSERT INTO szkolenie_users (imie, email, haslo) VALUES
--     ('Anna', 'anna@test.pl', 'haslo123');

-- -- Zadania testowe dla Anny (uzytkownik_id = 1)
-- INSERT INTO szkolenie_todos (tytul, opis, uzytkownik_id) VALUES
--     ('Kupic mleko', 'Z Biedronki, 2 kartony', 1),
--     ('Nauczyc sie Flask', 'Routing, szablony, formularze, baza danych', 1),
--     ('Zadzwonic do lekarza', 'Umowic wizyte na piatek', 1),
--     ('Zrobic pranie', NULL, 1),
--     ('Oddac ksiazke do biblioteki', 'Na Dlugiej 15', 1);