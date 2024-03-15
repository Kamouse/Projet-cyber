from PIL import Image
import pytesseract

# Si vous n'avez pas l'exécutable tesseract dans votre PATH, incluez ce qui suit :
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'
# Par exemple, tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

# Conversion d'une image simple en chaîne de caractères
print(pytesseract.image_to_string(Image.open(r'c:\Users\exemple\Downloads\téléchargé (5).png')))
