#https://flothesof.github.io/removing-background-scikit-image.html
from skimage import io as skio
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters
from scipy import ndimage as ndi
from skimage import morphology
import os

cwd = os.getcwd()

my_path = str(cwd) + "\\training_set\\bananas"
img = skio.imread(str(my_path) + '\\bimage13.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobel = filters.sobel(gray)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['figure.dpi'] = 200
blurred = filters.gaussian(sobel, sigma=1.5)
light_spots = np.array((gray > 250).nonzero()).T
dark_spots = np.array((gray < 3).nonzero()).T
bool_mask = np.zeros(gray.shape, dtype=np.bool)
bool_mask[tuple(light_spots.T)] = True
bool_mask[tuple(dark_spots.T)] = True
seed_mask, num_seeds = ndi.label(bool_mask)
ws = morphology.watershed(blurred, seed_mask)
background = max(set(ws.ravel()), key=lambda g: np.sum(ws == g))
background_mask = (ws == background)
rows = len(background_mask)
cols = len(background_mask[0])
for i in range(0, rows):
    for j in range(0, cols):
        if (background_mask[i][j] == False):
            # print(background_mask[i][j])
            # print(img[i][j])
            # break
            img[i][j][0] = 0
            img[i][j][1] = 0
            img[i][j][2] = 0
    # break
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imwrite(str(my_path) + "\\cleaned.jpg", rgb_img)
cv2.imshow('x', rgb_img)
# plt.imshow(img)
# Maintain output window utill
# user presses a key
cv2.waitKey(0)

# Destroying present windows on screen
cv2.destroyAllWindows()