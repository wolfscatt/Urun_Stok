# ---------------------- Resimlerde bulunan yazıları text'e dönüştürüp gösteren program ----------------------
import cv2
import pytesseract

yol = "Dosya_yolu"
pytesseract.pytesseract.tesseract_cmd = "tesseract.exe dosyasının yüklendiği dosya yolu"

image = cv2.imread(yol)
text = pytesseract.image_to_string(image)
print(text)

