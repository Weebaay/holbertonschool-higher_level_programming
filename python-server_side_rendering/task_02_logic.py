from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)  # Charger les données du fichier JSON
        # Obtenir la liste d'items, ou une liste vide si non trouvé
        items = data.get('items', [])
    return render_template('items.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
