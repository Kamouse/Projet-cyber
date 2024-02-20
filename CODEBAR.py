import requests 
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode
import base64

url = "https://cyber-learning.fr/cyber-challenge/programmation/barcode/sujet.php?jeton=exemple"

def fetch_image(img_data):
    img_data = img_data.replace('data:image/png;base64,', '')
    img_data = base64.b64decode(img_data)
    img = Image.open(BytesIO(img_data))
    return img

def decode_qrcode(image):
    decoded_objects = decode(image)      
    if len(decoded_objects) == 0:
        print("Aucun QR code dans l'image")
    else:
        return decoded_objects[0].data.decode("utf-8")


    
headers = {
  "exemple": "en json",
  
}

r = requests.get(url)
while True:  # Remplacez True par la condition d'arrêt que vous souhaitez
    
    soup = BeautifulSoup(r.content, 'html.parser')
    img_data = soup.find('img')['src']
    img = fetch_image(img_data)
    result = str(decode_barcode(img))

   

    if result is not None:
        r = requests.post(url, data={ 'barcode' : result },  headers=headers)

        
