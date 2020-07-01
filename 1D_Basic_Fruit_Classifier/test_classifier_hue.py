from image_preprocessing import *
from py_classifier_training import *
from analyze_data import *
from os import listdir
from os.path import isfile, join
import csv
import cv2
import os

cwd = os.getcwd()
cent_file = str(cwd) + "/training_set/centroid_array.csv"
test_path = str(cwd) + "/test_set/"
ratio_file = str(cwd) + "/training_set/ratio_component.csv"
a_classified = str(cwd) + "/test_set/classified_apples"
b_classifies = str(cwd) + "/test_set/classified_apples"

def get_default_cent():
    c = {"apple" : None, "banana" : None}
    with open(cent_file) as f:
        reader = csv.reader(f, delimiter="\t")
        x = 0
        for i in reader:
            if x == 0:
                c['apple'] = float(i[0].split(",")[0])
            if x == 1:
                c['banana'] = float(i[0].split(",")[0])
            x += 1
    return c

def classify(img_c, cent, rc):
    print(img_c, cent, rc)
    hue_class = ""
    ratio_class = ""
    da = abs(img_c[0] - cent['apple'])
    db = abs(img_c[0] - cent['banana'])
    if da >= db:
        hue_class = 'Banana'
    else:
        hue_class = "Apple"
    if rc[0] >= rc[1]:
        ratio_class = 'Apple'
    else:
        ratio_class = 'Banana'
    return [hue_class, ratio_class]

def get_default_ratio():
    ratio = {"apple" : None, "banana" : None}
    with open(ratio_file) as f:
        reader = csv.reader(f, delimiter="\t")
        for i in reader:
            ratio['apple'] = float(i[0].split(',')[0])
            ratio['banana'] = float(i[0].split(',')[1])
    return ratio

if __name__ == "__main__":
    dirs = listdir(test_path)
    cent = get_default_cent()
    write_train_data()
    bc, ac = 0, 0
    for d in dirs:
        files = [f for f in listdir(str(test_path) + str(d)) if isfile(join(str(test_path) + str(d), f))]
        #process each image to get hue variants
        for f in files:
            f_name = str(test_path) + str(d) + "/" + str(f)
            img = cv2.imread(f_name)
            image_hue_arr = get_hue(img)
            image_centroid = centroid_cal(image_hue_arr)
            rc = calculate_ratio(img)
            cl = classify(image_centroid, cent, rc)
            write_final_csv(f_name, cl[0], cl[1])
            print(f_name, cl[0], cl[1])
            print("-------------------------------------------------------------------------")

    print_op()