from flask import Flask, request, render_template
import random
import string

DEFAULT_SIZE_PASS = 64
MIN_SIZE_REQUIRED = 8
PORT = 5088

app = Flask(__name__)

def generate_password(length, use_digits=True, use_symbols=True, use_uppercase=True):
    if length < MIN_SIZE_REQUIRED:
        return "❗ La longueur minimale requise est de 8 caractères."

    letters = string.ascii_lowercase  # de base : minuscules

    if use_uppercase:
        letters += string.ascii_uppercase
    if use_digits:
        letters += string.digits
    if use_symbols:
        letters += string.punctuation

    if not letters:
        return "❗ Aucun caractère sélectionné."

    password = ''.join(random.choice(letters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def home():
    password = None
    length = DEFAULT_SIZE_PASS
    use_digits = True
    use_symbols = True
    use_uppercase = True

    if request.method == 'POST':
        try:
            length = int(request.form.get('length', DEFAULT_SIZE_PASS))
            use_digits = 'use_digits' in request.form
            use_symbols = 'use_symbols' in request.form
            use_uppercase = 'use_uppercase' in request.form
            password = generate_password(length, use_digits, use_symbols, use_uppercase)
        except (ValueError, TypeError):
            password = "Erreur : valeur incorrecte."

    return render_template('index.html',
                           password=password,
                           length=length,
                           use_digits=use_digits,
                           use_symbols=use_symbols,
                           use_uppercase=use_uppercase)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
