import cv2
from os import listdir
from os.path import isfile, join
import csv
import os
cwd = os.getcwd()

my_path = str(cwd) + "\\training_set\\"
a_path = str(my_path) + "apples\\"
b_path = str(my_path) + "bananas\\"
hue_apples_array = []
hue_bananas_array = []

ratio_dict = []

# def get_color_ratio(img) -> dict:
#     global ratio_dict
#     hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     hue_array = [0] * 195
#     rows = len(img)
#     cols = len(img[0])
#     red = 0
#     yellow = 0
#     pix = 0
#     for r in range(0, rows):
#         for c in range(0, cols):
#             ind = hsv_img[r][c][0]
#             b = hsv_img[r][c][1]
#             if ind <= 2 and b <= 5:
#                 continue
#             if 2 < ind < 15 or ind >= 170:
#                 red += 1
#             elif 21 < ind < 34:
#                 yellow += 1
#             pix += 1
#     print((red/pix)*100)
#     print((yellow/pix)*100)
#     ratio_dict.append({"red": (red/pix)*100, "yellow": (yellow/pix)*100})

#
# def write_to_csv_percentages():
#     global ratio_dict
#     print(ratio_dict)
#     r_op = []
#     rr = 0.0
#     yr = 0.0
#     for r in ratio_dict:
#         rr = rr + r['red']
#         yr = yr + r['yellow']
#     r_op.append(str(rr/len(ratio_dict)))
#     r_op.append(str(yr/len(ratio_dict)))
#     print(r_op)
#     outfile = open(str(my_path) + "ratio_component.csv", 'a')
#     writer = csv.writer(outfile)
#     writer.writerow(r_op)
#     outfile.close()

def get_hue(img) -> list:
    """
    Calculate hue values for every image and return the hue array.
    Discard all white pixels. Values belonging to Red hue range it < 10 and > 170 add it beyong 180 so that its easier
    to visual viz in 180 degree chart
    0 - 15 Shades of Red, 15 - 30 Shades of Orange - Yellow, 30 - 45 Shades of yellow - green, 45 - 60 Shades of Green,
    60 - 75 Shades of Green - Cyan, 75 - 90 Shades of Cyan - Blue, 90 - 105 Shades of Blue, 105 - 120 Shades of Blue - Purple,
    120 - 135 Shades of Purple - Magenta, 135 - 150 Shades of Magenta Pink, 150 - 165 - Shades of Pink
    165 - 0 - Shades of Pink - Red
    This will be divided now as
    0 - 15 None, 15 - 75 - Greens, 75 - 125 - Blues, 125 to 195 - Reds
    :param img:
    :return:
    """
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue_array = [0]*195
    rows = len(img)
    cols = len(img[0])
    for r in range(0,rows):
        for c in range(0, cols):
            ind = hsv_img[r][c][0]
            b = hsv_img[r][c][1]
            if ind <= 2 and b <= 5:
                continue
            if ind < 15:
                hue_array[ind+180] = hue_array[ind + 180] + 1
            else:
                hue_array[ind] = hue_array[ind] + 1
    for i in range(0, len(hue_array)):
        hue_array[i] = round(hue_array[i]/(rows * cols), 2)
    return hue_array


def process_images(path, files_folder) -> list:
    """
    Process all apples and bananas images from training set to calculate hue
    :return:
    """
    hue_array = []
    for each in files_folder:
        # my_path = my_path.replace("\\","\\")
        my_file = str(path)+str(each)
        img = cv2.imread(my_file)
        get_color_ratio(img)
        hue_arr = get_hue(img)
        hue_array.append(hue_arr)
    return hue_array

def process_ratio(path, files_folder):
        """
        Process all apples and bananas images from training set to calculate hue
        :return:
        """
        for each in files_folder:
            # my_path = my_path.replace("\\","\\")
            my_file = str(path) + str(each)
            img = cv2.imread(my_file)
            get_color_ratio(img)


def write_to_csv(hue_array, c=True):
    """
    Write calculate and normalized hue values to csv for further training
    :return:
    """
    if c:
        outfile = open(str(my_path) + "apples_analysis_data\\" + "hue_apples_array.csv", 'w')
    else:
        outfile = open(str(my_path) + "bananas_analysis_data\\" + "hue_bananas_array.csv", 'w')
    writer = csv.writer(outfile)
    for each in hue_array:
        writer.writerow(each)
    outfile.close()



if __name__ == "__main__":
    a_files = [f for f in listdir(a_path) if isfile(join(a_path, f))]
    b_files = [f for f in listdir(b_path) if isfile(join(b_path, f))]
    print("Start image preprocessing")
    hue_apples_array = process_images(a_path, a_files)
    hue_bananas_array = process_images(b_path, b_files)
    process_ratio()
    write_to_csv_percentages()
    write_to_csv(hue_bananas_array, False)
    write_to_csv(hue_apples_array, True)

