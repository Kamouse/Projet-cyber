from Crypto.Cipher import AES

key = b'0123456789abcdef'
cipher = AES.new(key, AES.MODE_EAX)

with open('flag.notes', 'rb') as file:
    ciphertext = file.read()

nonce = ciphertext[:16]
ciphertext = ciphertext[16:]

cipher.set_nonce(nonce)
plaintext = cipher.decrypt(ciphertext)

print(plaintext)
