# -*- coding: utf-8 -*-

from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[..., :], [0.299, 0.587, 0.144])


imgName = 'fry.jpg'

img = misc.imread(imgName)
gray = img
if len(img.shape) == 3:# height, width, 3
    gray = rgb2gray(img)

lx, ly = gray.shape[0], gray.shape[1]
if ly > lx:
    gray = misc.imresize(gray, (int(lx * 150 / ly  * 0.5), 150))
else:
    gray = misc.imresize(gray, (int(150 * 0.5), int(ly * 150 / lx)))
lx, ly = gray.shape[0], gray.shape[1]

charList = ['@', '8', '5', '3', '0', '*', ',', '.']
cStr = ''

for indx in range(lx):
    for indy in range(ly):
        cStr += charList[int(gray[indx, indy] / 36)]
    cStr += '\n'

with open('img.txt', 'w') as fh:
    fh.write(cStr)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Obsolete
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# plt.imshow(gray, cmap=plt.cm.gray)
# plt.axis('off')
# plt.show()

# bsizex = 1
# bsizey = 1
# cArr = np.chararray((lx, ly))
# for indx in range(lx):
#     for indy in range(ly):
#         cArr[indx, indy] = charList[int(gray[indx, indy] / 36)]



