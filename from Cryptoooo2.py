from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import itertools

print("test")

# Votre message chiffré
cipher_text = b'gAAAAABlfJghQF_5HEh7rBOfJ3ejbxvw4h6_v_9Sr9GV5eWe6ziltB5pgZCApkSp6c_krkK3XHoN9fbGZ-tRc7xz4Chi7ixWjRuDfEJ-CHAVJfKJxVrbMfEl1akaKuHHOYDnuZhfezkU'

# Générer toutes les clés possibles
keys = [''.join(i) for i in itertools.product('0123456789abcdef', repeat=32)]

# Essayer chaque clé
for key in keys:
    print("Essai avec la clé : ", key)  # Imprimer la clé en cours d'essai
    try:
        # Créer un nouvel objet AES avec la clé
        cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)

        # Déchiffrer le texte
        decrypted_text = unpad(cipher.decrypt(base64.b64decode(cipher_text)), AES.block_size)

        print(key)
        print(decrypted_text)
        break
    except:
        continue

