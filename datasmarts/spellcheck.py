# Importamos las dependencias del script.
from argparse import ArgumentParser

import cv2
import pytesseract
from textblob import TextBlob
from textblob import download_corpora

# Descargamos los conjuntos de datos usados por TextBlob para entrenar sus modelos internos.
download_corpora.download_all()

# COMENTAR ESTA LÍNEA SI NO USAS WINDOWS
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

# Definimos el menú del programa.
argument_parser = ArgumentParser()
argument_parser.add_argument('-i', '--image', required=True, help='Ruta a la imagen de entrada.')
arguments = vars(argument_parser.parse_args())

# Cargamos la imagen y la mostramos.
image = cv2.imread(arguments['image'])
cv2.imshow('Imagen', image)
cv2.waitKey(0)

# Pasamos de BGR a RGB para garantizar compatibilidad con PyTesseract.
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Extraemos el texto de la imagen.
text = pytesseract.image_to_string(image)

print('Texto ANTES del autocorrector')
print(f'{text}\n')
print('---')

# Corregimos el texto usando TextBlob
text_blob = TextBlob(text)
corrected = text_blob.correct()

# Mostramos el texto corregido.
print('CORREGIDO')
print(corrected)

# Destruimos las ventanas creadas.
cv2.destroyAllWindows()
