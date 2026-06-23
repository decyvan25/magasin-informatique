from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="magasin_user",
        password="magasin_pass",
        database="magasin_informatique",
        charset="utf8mb4",
        collation="utf8mb4_unicode_ci"
    )

@app.route("/")
def accueil():
    return render_template("accueil.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == "admin" and password == "1234":
            return redirect("/admin")

        connexion = get_db_connection()
        curseur = connexion.cursor(dictionary=True)

        curseur.execute(
            "SELECT * FROM clients WHERE email = %s AND password = %s",
            (email, password)
        )
        client = curseur.fetchone()

        curseur.close()
        connexion.close()

        if client:
            return redirect(f"/client/{client['id']}")
        else:
            return render_template("login.html", erreur="Email ou mot de passe incorrect")

    return render_template("login.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/client/<int:id_client>")
def client(id_client):
    return render_template("client.html", id_client=id_client)

@app.route("/produits")
def produits():
    connexion = get_db_connection()
    curseur = connexion.cursor(dictionary=True)

    curseur.execute("SET NAMES utf8mb4;")
    curseur.execute("SELECT nom, prix, stock FROM produits")
    produits_liste = curseur.fetchall()

    curseur.close()
    connexion.close()

    return render_template("produits.html", produits=produits_liste)

@app.route("/client/<int:id_client>/commander", methods=["GET", "POST"])
def commander(id_client):

    connexion = get_db_connection()
    curseur = connexion.cursor(dictionary=True)

    if request.method == "POST":
        id_produit = int(request.form["id_produit"])
        quantite = int(request.form["quantite"])

        curseur.execute(
            "SELECT id, nom, prix, stock FROM produits WHERE id = %s",
            (id_produit,)
        )
        produit = curseur.fetchone()

        if produit is None:
            curseur.close()
            connexion.close()
            return "Produit introuvable"

        if quantite > produit["stock"]:
            curseur.close()
            connexion.close()
            return "Stock insuffisant"

        total = produit["prix"] * quantite

        curseur.execute(
            """
            INSERT INTO commandes (id_client, date_commande, total, statut)
            VALUES (%s, CURDATE(), %s, %s)
            """,
            (id_client, total, "En attente")
        )

        id_commande = curseur.lastrowid

        curseur.execute(
            """
            INSERT INTO details_commandes (id_commande, id_produit, quantite, prix_unitaire)
            VALUES (%s, %s, %s, %s)
            """,
            (id_commande, id_produit, quantite, produit["prix"])
        )

        curseur.execute(
            """
            UPDATE produits
            SET stock = stock - %s
            WHERE id = %s
            """,
            (quantite, id_produit)
        )

        connexion.commit()

        curseur.close()
        connexion.close()

        return redirect(f"/client/{id_client}")

    curseur.execute("SELECT id, nom, prix, stock FROM produits")
    produits = curseur.fetchall()

    curseur.close()
    connexion.close()

    return render_template(
        "commander.html",
        produits=produits,
        id_client=id_client
    )

if __name__ == "__main__":
    app.run(debug=True)