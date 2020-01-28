# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# o código espera que a imagem esteja no mesmo diretório que ele
try:
  img = plt.imread('image.jpg')  # leitura da imagem como um numpy array
except:
  print("An exception occurred")
  exit(0)

nrows, ncols = img.shape[:2]  # obtendo as dimensões da imagem linhas x colunas
img_copy = img.copy()  # cópia da imagem(array) para ser alterado
threshold = 150  # threshold predefinido

for i in range(nrows):
    for j in range(ncols):
        lum = img[i, j][0]*0.2126 + img[i, j][1]*0.7152 + img[i, j][2]*0.1722  # luminosidade
        if lum >= threshold:
            img_copy[i,j][:3] = 255  # definindo o pixel branco
        else:
            img_copy[i,j][:3] = 0  # definindo o pixel preto

plt.imsave('image_threshold.jpg', img_copy)
plt.imshow(img_copy)
plt.show()
