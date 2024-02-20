import pickle
import hashlib

def lire_fichier(nom_fichier):
    with open(nom_fichier, 'rb') as f:
        data = pickle.load(f)
    return data

def detect_hash_type(cipher_text):
    hash_types = [hashlib.md5(), hashlib.sha1(), hashlib.sha224(), hashlib.sha256(), hashlib.sha384(), hashlib.sha512()]
    for hash_type in hash_types:
        hashed = hash_type.hexdigest()
        if hashed == cipher_text:
            return hash_type.name
    return "Unknown"

# Utilisation de la fonction de lecture de fichier
data = lire_fichier('C:/Users/nicol/OneDrive/Bureau/flag.notes')
print(data)

# Utilisation de la fonction de détection de hachage
cipher_text = data  # Utilisez vos données chiffrées ici
print(detect_hash_type(cipher_text))

