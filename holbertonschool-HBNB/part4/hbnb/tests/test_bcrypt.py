from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Mot de passe brut
password = "admin1234"

# Étape 1 : Générer un hash
hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
print(f"Mot de passe brut : {password}")
print(f"Mot de passe hashé : {hashed_password}")

# Étape 2 : Vérifier le mot de passe avec le hash généré
is_valid = bcrypt.check_password_hash(hashed_password, password)
print(f"Le mot de passe est valide : {is_valid}")

# Étape 3 : Vérifier un autre mot de passe incorrect
is_invalid = bcrypt.check_password_hash(hashed_password, "wrongpassword")
print(f"Un mot de passe incorrect est valide : {is_invalid}")
