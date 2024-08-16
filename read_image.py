import cv2
import json

retangulos = []

x_inicial, y_inicial = 0, 0

def desenhar_retangulo(event, x, y, flags, param):
    global x_inicial, y_inicial
    if event == cv2.EVENT_LBUTTONUP:
        retangulos.append((x_inicial, y_inicial, x - x_inicial, y - y_inicial))
        cv2.rectangle(imagem, (x_inicial, y_inicial), (x, y), (0, 255, 0), 2)
        cv2.imshow('Imagem com Retângulos', imagem)

    # Se o botão esquerdo do mouse for pressionado, registre as coordenadas iniciais
    elif event == cv2.EVENT_LBUTTONDOWN:
        x_inicial, y_inicial = x, y

imagem = cv2.imread('Algoritmos/Meninas/sample-1.jpg')

cv2.namedWindow('Imagem com Retângulos')
cv2.setMouseCallback('Imagem com Retângulos', desenhar_retangulo)

while True:
    cv2.imshow('Imagem com Retângulos', imagem)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

# Salvar as coordenadas dos retângulos em um arquivo .json
with open('coordenadas.json', 'w') as f:
    json.dump({'retangulos': retangulos}, f)
