import requests 
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode
import base64

url = "https://cyber-learning.fr/cyber-challenge/programmation/barcode/sujet.php?jeton=dOMEW7X4u111"

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
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
  "Cache-Control": "max-age=0",
  "Content-Length": "19",
  "Content-Type": "application/x-www-form-urlencoded",
  "Cookie": "cookieyes-consent=consentid:UVB5VXpSOTFNZnNZeGhRbXNKMXNKb1RNQ2h0clBXODU,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; wordpress_test_cookie=WP%20Cookie%20check; PHPSESSID=f0023ac2b1c49514c39873d0fbe1bb53; FLAG=trop_simple..._Donc_c_est_pas_la_solution.; wordpress_logged_in_f2e0ddd3b6b9425a8eec551bcfe163f3=nicolas.coutot%7C1705655462%7CKRa0LI9n11DXmvCtmWupTIpnPS2ZZVp6TJHS1EzvFig%7Cb27bea2d2eb528bdeed83e9bdf315ad4d3b5b52052c4d30e505ccc8aabfcaf32; wfwaf-authcookie-9c9176d3190dfd1358d9c090e85bba0f=316%7Csubscriber%7Cread%7C0c1d7660afe46429f7718e04b73a21cd48333f45510e865f9ad67aafaaf85231",
  "Origin": "https://cyber-learning.fr",
  "Referer": "https://cyber-learning.fr/cyber-challenge/programmation/barcode/sujet.php?jeton=dOMEW7X4u111",
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
'''

r = requests.get(url)
while True:  # Remplacez True par la condition d'arrêt que vous souhaitez
    
    soup = BeautifulSoup(r.content, 'html.parser')
    img_data = soup.find('img')['src']
    img = fetch_image(img_data)
    result = str(decode_barcode(img))

   

    if result is not None:
        r = requests.post(url, data={ 'barcode' : result },  headers=headers)

        '''