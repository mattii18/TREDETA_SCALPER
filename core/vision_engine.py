import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def capture_chart_area(region=None):
    """Zrzut ekranu z określonego regionu (lub całego ekranu)"""
    img = ImageGrab.grab(bbox=region)
    img_np = np.array(img)
    return cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

def extract_text_from_image(image):
    """OCR na danym obrazie"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()

def detect_candlestick_patterns(image):
    """Wstępna analiza wykresu pod kątem świec"""
    # Placeholder – tu można dodać AI do rozpoznawania świec
    return "Brak jednoznacznych formacji świecowych"

# Przykład testowy
if __name__ == "__main__":
    screenshot = capture_chart_area()
    text = extract_text_from_image(screenshot)
    print("[OCR] Wykryty tekst:", text)
