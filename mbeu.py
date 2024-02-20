import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import io
import urllib.request
import re
import pytesseract  # Importez la bibliothèque pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR'

url = "https://cyber-learning.fr/cyber-challenge/programmation/captcha/sujet.php?jeton=EXWA3dRHN8"

def decode_text(image):
    text = pytesseract.image_to_string(image, lang='fra')  # Utilisez pytesseract pour extraire du texte
    return text

def fetch_image(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tag = soup.find('img')
    img_url = img_tag['src']
    return img_url

def download_image(url):
    response = urllib.request.urlopen(url)
    img_data = response.read()
    img = Image.open(io.BytesIO(img_data))
    return img

headers = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
  "Cache-Control": "max-age=0",
  "Content-Length": "12",
  "Content-Type": "application/x-www-form-urlencoded",
  "Cookie": "cookieyes-consent=consentid:UVB5VXpSOTFNZnNZeGhRbXNKMXNKb1RNQ2h0clBXODU,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; wordpress_test_cookie=WP%20Cookie%20check; PHPSESSID=f0023ac2b1c49514c39873d0fbe1bb53; FLAG=trop_simple..._Donc_c_est_pas_la_solution.; wfwaf-authcookie-9c9176d3190dfd1358d9c090e85bba0f=316%7Csubscriber%7Cread%7C5977a4263310b428c2e95f722eb60db6413580da785d1fc2b204e70a175fa3e2; wordpress_logged_in_f2e0ddd3b6b9425a8eec551bcfe163f3=nicolas.coutot%7C1705694320%7C3DAgw0h0H4bJSiKBu5T42gYNI5gR8A4Ln5gldOJuS28%7C3f70aee0b195a7e41d362121c8eef918b230494659619b856cf887821f008883",
  "Origin": "https://cyber-learning.fr",
  "Referer": "https://cyber-learning.fr/cyber-challenge/programmation/captcha/sujet.php?jeton=EXWA3dRHN8",
  "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Opera GX\";v=\"106\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-User": "?1",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
}


for i in range(3):  # Remplacez True par la condition d'arrêt que vous souhaitez

    r = requests.get(url)
    
    print(r.text)  # Imprimez la réponse du GET

    soup = BeautifulSoup(r.content, 'html.parser')
    img_url = fetch_image(url)
    img = download_image(img_url)
    result = decode_text(img)

    print(result)

    match = result

    print(match)
    
while True:
    r = requests.post(url, data={ 'codeqr' : match },  headers=headers)
    print(r.content)    
        
    # Si la réponse est correcte, sortir de la boucle
    if 'BRAVO' in r.content.decode('utf-8'):
            break


