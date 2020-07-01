from os import listdir
from os.path import isfile, join
import csv
from pprint import *
import os

cwd = os.getcwd()
i = 1
op = {}


def write_train_data():
    global op
    global i
    op = {}
    set1_path = str(cwd) + "/classifier1/test_set/set1"
    files = [f for f in listdir(str(set1_path)) if isfile(join(str(set1_path), f))]
    for f in files:
        f_name = str(set1_path) + "/" + str(f)
        d = {"Image": f_name, "Class" : "Apple", "Hue_Result" : None, "Ratio_Result": None,"Eval" : None}
        op[str(i)] = d
        i += 1

    set2_path = str(cwd) + "/classifier1/test_set/set2"
    files = [f for f in listdir(str(set2_path)) if isfile(join(str(set2_path), f))]
    for f in files:
        f_name = str(set2_path) + "/" + str(f)
        d = {"Image": f_name, "Class" : "Banana", "Hue_Result" : None, "Ratio_Result": None, "Eval" : None}
        op[str(i)] = d
        i += 1

    # pprint(op)


def write_final_csv(file_name, hue_class, ratio_class):
    global op
    for each in op:
        if op[each]['Image'] == str(file_name):
            op[each]['Hue_Result'] = str(hue_class)
            op[each]['Ratio_Result'] = str(ratio_class)
            if op[each]['Hue_Result'] == op[each]['Ratio_Result'] == op[each]['Class']:
                op[each]['Eval'] = 1
            else:
                op[each]['Eval'] = 0
            print(op[each])
            break

def print_op():
    pprint(op)
    csv_file = str(cwd) + "/test_set/final_data.csv"
    with open(csv_file, 'a', newline='') as c:
        writer = csv.DictWriter(c, fieldnames=['Image', 'Class', 'Hue_Result', 'Ratio_Result', 'Eval'])
        writer.writeheader()
        for i in op:
            writer.writerow(op[i])
    c.close()


if __name__ == "__main__":
    write_train_data()