import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = "tajny_klucz_12345" # ->> bez tego leży logowanie, sesje

def get_db():
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="Password!"
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

def login_required(f): ## --> wrzucam 
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper


@app.route("/")
@login_required
def home():
    conn, cur = get_db()
    cur.execute(
        "SELECT * FROM szkolenie_todos WHERE uzytkownik_id = %s ORDER BY data_dodania DESC",
        (session["user_id"],)
    )
    zadania = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("index.html", zadania=zadania)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "")
        haslo = request.form.get("haslo", "")

        conn, cur = get_db()
        cur.execute(
            "SELECT id, imie FROM szkolenie_users WHERE email = %s AND haslo = %s",
            (email, haslo)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            session["user_imie"] = user["imie"]
            return redirect(url_for("home"))
        else:
            return render_template("login.html", blad="Bledny email lub haslo!")

    return render_template("login.html")


@app.route("/wyloguj")
def wyloguj():
    session.clear()
    return redirect(url_for("login"))

@app.route("/dodaj", methods=["GET", "POST"])
@login_required
def dodaj():
    if request.method == "POST":
        tytul = request.form.get("tytul", "").strip()
        opis = request.form.get("opis", "").strip()

        if tytul:
            conn, cur = get_db()
            cur.execute(
                "INSERT INTO szkolenie_todos (tytul, opis, uzytkownik_id) VALUES (%s, %s, %s)",
                (tytul, opis if opis else None, session["user_id"])
            )
            conn.commit()
            cur.close()
            conn.close()
        return redirect(url_for("home"))
    return render_template("dodaj.html")

@app.route("/edytuj/<int:id>", methods=["GET", "POST"])
@login_required
def edytuj(id):
    conn, cur = get_db()
    if request.method == "POST":
        tytul = request.form.get("tytul", "").strip()
        opis = request.form.get("opis", "").strip()

        cur.execute(
            "UPDATE szkolenie_todos SET tytul = %s, opis = %s WHERE id = %s AND uzytkownik_id = %s",
            (tytul, opis if opis else None, id, session["user_id"])
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("home"))
    
    cur.execute(
        "SELECT * FROM szkolenie_todos WHERE id = %s AND uzytkownik_id = %s",
        (id, session["user_id"])
    )
    zadanie = cur.fetchone()
    cur.close()
    conn.close()

    if not zadanie:
        return redirect(url_for("home"))

    return render_template("edytuj.html", zadanie=zadanie)

@app.route("/usun/<int:id>", methods=["GET", "POST"])
@login_required
def usun(id):
    conn, cur = get_db()
    if request.method == "POST":
        cur.execute(
            "DELETE FROM szkolenie_todos WHERE id = %s AND uzytkownik_id = %s",
            (id, session["user_id"]))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("home"))
    
    cur.execute(
        "SELECT * FROM szkolenie_todos WHERE id = %s AND uzytkownik_id = %s",
        (id, session["user_id"])
    )
    zadanie = cur.fetchone()
    cur.close()
    conn.close()
    if not zadanie:
        return redirect(url_for("home"))

    return render_template("usun.html",zadanie=zadanie)


@app.route("/wykonaj/<int:id>")
@login_required
def wykonaj(id):
    conn, cur = get_db()
    cur.execute(
        "UPDATE szkolenie_todos SET wykonane = NOT wykonane WHERE id = %s AND uzytkownik_id = %s",
        (id, session["user_id"])
    )
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for("home"))


@app.route('/lista')
@login_required
def lista():
    produkty = ["Laptop", "Mysz", "Monitor", "Klawiatura"]
    return render_template('lista.html',produkty=produkty,title="Produkty")

# Jak jest ten sam route to bierze pierwsze w kolejności
# @app.route("/test_ruting") # --> dekoratory 
# def test():
#     return "<h1>Witaj w Czechach!</h1>"

# ta sama nazwa funkcji -> leży cała aplikacja
# @app.route("/test_ruting") # --> dekoratory 
# def test_main_page():
#     return "<h1>Witaj w Polsce!</h1>"

@app.route("/test_ruting") # --> dekoratory 
def test_main_page():
    return "<h1>Witaj w Polsce!</h1>"


@app.route("/test_ruting/o_nas") 
def o_nas():
    return "<h1>Jesteśmy wielomilionową firmą w PL</h1>"

# Przekazanie parametru 

@app.route("/test_ruting/witaj/<imie>") 
def witaj(imie):
    return f"<h1>Cześć {imie}</h1>"

# Przekazanie parametry z typem
@app.route("/test_ruting/post/<int:post_id>") 
def post_bloga(post_id):
    return f"<h1>Jesteś na poście numer: {post_id}</h1>"


# URL: /szukaj?fraza=python&strona=2
@app.route("/szukaj")
def szukaj():
    fraza = request.args.get("fraza", "")
    strona = request.args.get("strona", 1, type=int)
    return f"<h1>Szukasz: {fraza}, strona {strona}</h1>"


if __name__ == "__main__":
    app.run(debug=True)



# https://getbootstrap.com/docs/5.3/components/buttons/