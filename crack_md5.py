import hashlib

hash_cible = "81dc9bdb52d04dc20036dbd8313ed055"

mots_de_passe = [
    "admin",
    "password",
    "1234",
    "azerty",
    "qwerty",
    "bonjour"
]

for mot in mots_de_passe:
    hash_test = hashlib.md5(mot.encode()).hexdigest()

    if hash_test == hash_cible:
        print(f"Mot de passe trouvé : {mot}")
        break
else:
    print("Mot de passe non trouvé")
