import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import cv2
import os
cwd = os.getcwd()
# Read data from CSV
my_path = str(cwd) + "/training_set/"
a = pd.read_csv(str(my_path) + "apples_analysis_data/hue_apples_array.csv")
b = pd.read_csv(str(my_path) + "bananas_analysis_data/hue_bananas_array.csv")

#Convert to numpy array
app = a.to_numpy()
ba = b.to_numpy()


def plot_images_hue():
    """
    Plot Hue values from 1 - 180 degrees based for each image.
    :return:
    """
    # Plot hue distribution for individual image
    for i in range(0, len(app)):
        fig = plt.figure(figsize=(10,4)) # we create a blank canvas
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot(x,app[i][:], 'r')
        ax.set_xlabel('Hue indices')
        ax.set_ylabel('Normalized Val')
        ax.set_title('Hue Distribution for Apples')
        plt.savefig(str(my_path) + "apples_analysis_data/image" + str(i) + ".png")

    # Plot hue distribution for individual image
    for i in range(0, len(ba)):
        fig = plt.figure(figsize=(10,4)) # we create a blank canvas
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot(x,ba[i][:],'y')
        ax.set_xlabel('Hue indices')
        ax.set_ylabel('Normalized Val')
        ax.set_title('Hue Distribution for Bananas')
        plt.savefig(str(my_path) + "bananas_analysis_data/image" + str(i) + ".png")

def cal_aggregate_hue(arr):
    """
    Calculate centroids for 1d values segregating apples and bananas. Ie find the hue values closet to the subsets of
    apples and bananas.
    :param app:
    :return:
    """
    # Calculate aggregate hue for all apple and banana images
    final_arr = []
    for i in range(0, 195):
        sum = 0.0
        for j in range(0, len(arr)):
            sum = sum + arr[j][i]
        final_arr.append(sum)
    return final_arr

def calculate_ratio(img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue_array = [0] * 195
    rows = len(img)
    cols = len(img[0])
    red = 0
    yellow = 0
    pix = 0
    for r in range(0, rows):
        for c in range(0, cols):
            ind = hsv_img[r][c][0]
            b = hsv_img[r][c][1]
            if ind <= 2 and b <= 5:
                continue
            if 2 < ind < 15 or ind >= 170:
                red += 1
            elif 21 < ind < 34:
                yellow += 1
            pix += 1
    return [(red/pix)*100, (yellow/pix)*100]

# Calculate centroid for apples and bananas
def centroid_cal(arr):
    """
    Calculate centroid using weighted avgs to get the hue value on X axis.
    :param x:
    :param arr:
    :return:
    """
    x = np.arange(1,196)
    sum_i, sum_j = 0.0, 0.0
    for i,j in zip(x, arr):
        sum_j = sum_j + j
        sum_i = sum_i + (float(i) * j)
    centroid = sum_i / sum_j
    return [centroid, 0]


def plot_aggregated_hue_and_centroid(final_arr, centroid_arr, c=True):
    """
    Plot the aggregated values and centroid plot.
    :param final_arr:
    :param centroid_arr:
    :param c:
    :return:
    """
    # Plot Apple's Hue distribution and centroid
    x = np.arange(1,196)
    fig = plt.figure(figsize=(10,4)) # we create a blank canvas
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.plot(x, final_arr[:], 'magenta')
    ax.set_xlabel("Hue Distribution")
    ax.set_ylabel("Weights")
    ax.set_title("Centroid Point distinguishing classes")
    plt.plot(centroid_arr[0], centroid_arr[1], 'g*')
    if c:
        plt.savefig(str(my_path) + "bananas_analysis_data/aggregated_banana_hue.png")
    else:
        plt.savefig(str(my_path) + "apples_analysis_data/aggregated_apple_hue.png")

def save_centroids(arr):
    op = open(str(my_path) + "centroid_array.csv", 'a', newline='')
    writer = csv.writer(op)
    writer.writerow(arr)
    op.close()



if __name__ == "__main__":
    plot_images_hue()
    banana_final_arr = cal_aggregate_hue(ba)
    apple_final_arr = cal_aggregate_hue(app)
    banana_centroid = centroid_cal(banana_final_arr)
    apple_centroid = centroid_cal(apple_final_arr)
    print(banana_centroid, apple_centroid)
    # calculate_ratio()
    save_centroids(apple_centroid)
    save_centroids(banana_centroid)
    plot_aggregated_hue_and_centroid(banana_final_arr, banana_centroid, True)
    plot_aggregated_hue_and_centroid(apple_final_arr, apple_centroid, False)