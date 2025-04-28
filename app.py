from flask import Flask, request
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
    return """
    <h1>🔒 Secure Password Generator 🔒</h1>
    <p>Utilisez l'URL : /generate?length=12 pour générer un mot de passe.</p>
    """

@app.route('/generate')
def generate():
    try:
        length = int(request.args.get('length', 12))
        password = generate_password(length)
        return f"<h2>Votre mot de passe :</h2><p><strong>{password}</strong></p>"
    except ValueError:
        return "<p>❗ Veuillez fournir un nombre valide pour la longueur.</p>"

if __name__ == "__main__":
    app.run(debug=True)
