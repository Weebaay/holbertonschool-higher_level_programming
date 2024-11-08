from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json(file_path):
    """Lit et renvoie les données du fichier JSON sous forme de liste de dictionnaires."""
    with open(file_path, 'r') as file:
        return json.load(file)


def read_csv(file_path):
    """Lit et renvoie les données du fichier CSV sous forme de liste de dictionnaires."""
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sqlite():
    """Lit et renvoie les données de la base de données SQLite sous forme de liste de dictionnaires."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    # Obtient les noms des colonnes
    columns = [column[0] for column in cursor.description]
    # Combine les colonnes avec les lignes
    products = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return products


@app.route('/display_products')
def display_products():
    # Récupérer les paramètres source et id depuis l'URL
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    # Charger les données en fonction de la source
    if source == 'json':
        try:
            products = read_json('products.json')
        except FileNotFoundError:
            error = "JSON file not found."
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
        except FileNotFoundError:
            error = "CSV file not found."
    elif source == 'sqlite':
        products = read_sqlite()
    else:
        error = "Wrong source. Please use 'json', 'csv', or 'sqlite'."

    if product_id and not error:
        try:
            product_id = int(product_id)
            products = [p for p in products if p["id"] == product_id]
            if not products:
                error = f"Product with ID {product_id} not found."
        except ValueError:
            error = "Invalid ID format. Please provide a numeric ID."

    return render_template('product_display.html', products=products, error_message=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
