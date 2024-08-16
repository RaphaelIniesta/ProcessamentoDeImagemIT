import cv2
import json

imagem = cv2.imread('sample-1.jpg')

with open('coordenadas.json', 'r') as f:
    data = json.load(f)
    retangulos = data['retangulos']

for retangulo in retangulos:
    x, y, w, h = retangulo
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (255, 255, 0), 2)

cv2.imshow('Imagem com Retângulos', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
