import cv2
import numpy as np


rows = len(img)
cols = len(img[0])
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h_shift = np.zeros((rows, cols, 1), np.uint8)
for i in range(0, rows):
    for j in range(0, cols):
        if hsv_image[i][j][0] <= 3 and hsv_image[i][j][1] <=1 :
            continue
        # if (hsv_image[i][j][0] <= 34 and hsv_image[i][j][0] >= 21):
        if (hsv_image[i][j][0] <= 10 or hsv_image[i][j][0] >= 178):
            h_shift[i][j] = 255



cv2.imshow('a', h_shift)


cv2.waitKey(0)

# Destroying present windows on screen
cv2.destroyAllWindows()


# Save image in set directory
# Read RGB image

# rows = len(img)
# cols = len(img[0])
#
# blue_image_8bit = img[:, :, 0]
# green_image_8bit = img[:, :, 1]
# red_image_8bit = img[:, :, 2]

# cv2.imshow('p', blue_image_8bit)
# cv2.imshow('q', green_image_8bit)
# cv2.imshow('r', red_image_8bit)

# blue_image_24bit = np.zeros((rows, cols, 3), np.uint8)
# green_image_24bit = np.zeros((rows, cols, 3), np.uint8)
# red_image_24bit = np.zeros((rows, cols, 3), np.uint8)
# for r in range(0, rows):
#     for c in range(0, cols):
#         blue_image_24bit[r][c][0] = blue_image_8bit[r][c]
#         green_image_24bit[r][c][1] = green_image_8bit[r][c]
#         red_image_24bit[r][c][2] = red_image_8bit[r][c]
#
# cv2.imshow('a', blue_image_24bit)
# cv2.imshow('b', green_image_24bit)
# cv2.imshow('c', red_image_24bit)

# let's convert our image to hue, saturation, intensity (brightness)
# read the csv file again
# hue_file = open(str(my_path) + "\\" + "hue_apples_array.csv", 'r')

# Maintain output window utill
# user presses a key
# cv2.waitKey(0)

# Destroying present windows on screen
# cv2.destroyAllWindows()