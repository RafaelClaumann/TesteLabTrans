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

for i in range(nrows):
    for j in range(ncols):
        img_copy[i,j][:3] = img[i, j][0]*0.2126 + img[i, j][1]*0.7152 + img[i, j][2]*0.1722

plt.imsave('image_gray.jpg', img_copy)
plt.imshow(img_copy)
plt.show()