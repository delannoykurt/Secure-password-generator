import random
import string

# simple generate function in python with a (length) max or min size of password
def generate_password(length):
    if length < 8:
        print("La longueur minimale requis pour un bon mot de passe est d'au moins 8 caractères.")
        return None

    letters = string.ascii_letters
    numbers = string.digits
    symbol  = string.punctuation

    all_characters = letters + numbers + symbol

    # Génération du mot de passe
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password





#------------/
def main():
    print("🔒 Générateur de mots de passe sécurisé 🔒")
    try:
        length = int(input("Entrez la longueur désirée du mot de passe : "))
        mot_de_passe = generate_password(length)
        if mot_de_passe:
            print(f"\nVotre mot de passe généré : {mot_de_passe}")
    except ValueError:
        print("❗ Veuillez entrer un nombre valide.")

#--------------------------/
if __name__ == "__main__":
    main()
