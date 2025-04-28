from flask import Flask, request, render_template
import random
import string

app = Flask(__name__)

# --- Ta fonction existante, exactement comme tu l'as faite ---
def generate_password(length):
    if length < 8:
        return "❗ La longueur minimale requise est de 8 caractères."

    letters = string.ascii_letters
    numbers = string.digits
    symbol  = string.punctuation

    all_characters = letters + numbers + symbol

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# --- Routes Flask ---
@app.route('/')
def home():
    try:
        length = int(request.args.get('length', 12))
        password = generate_password(length)
    except ValueError:
        password = "Erreur de paramètre."

    return render_template('index.html', password=password)

@app.route('/generate')
def generate():
    try:
        length = int(request.args.get('length', 12))
        password = generate_password(length)
        return f"<h2>Votre mot de passe :</h2><p><strong>{password}</strong></p>"
    except ValueError:
        return "<p>❗ Veuillez fournir un nombre valide pour la longueur.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
