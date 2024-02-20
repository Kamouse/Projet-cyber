from cryptography.fernet import Fernet

# Votre clé de chiffrement
key = b'nmXnI7JUw29F6uRm1xKJfKqwr8igayxRmJU9bao14dk='

# Le message chiffré
encrypted_message = b'gAAAAABlfJghQF_5HEh7rBOfJ3ejbxvw4h6_v_9Sr9GV5eWe6ziltB5pgZCApkSp6c_krkK3XHoN9fbGZ-tRc7xz4Chi7ixWjRuDfEJ-CHAVJfKJxVrbMfEl1akaKuHHOYDnuZhfezkU'
print("message crypté : ",encrypted_message)
print("clé : ",key)
# Créer une instance Fernet avec votre clé
cipher_suite = Fernet(key)

# Déchiffrer le message
decrypted_message = cipher_suite.decrypt(encrypted_message)

print("Le message déchiffré est : ", decrypted_message.decode())
