# Importing the os library
import os

# The path for listing items
import random
import shutil

path = r'F:\darknet_training\model_RAK_box_symbols\images'
# print(path)
save_path = r'F:\darknet_training\curve_model'

with open("train.txt", "w") as a:
    for path, folders, files in os.walk(path):
        # print("--",files)
        for file in files:
            # file_list.append(os.path.abspath(os.path.join(path, file)))
            f = os.path.join("data" + os.sep + "model_RAK_box_symbols" + os.sep + "images", file)
            a.write(str(f) + "\n")


test_list = []
with open('train.txt') as f:
    lines = f.readlines()
    ten_pc = int(len(lines) / 10)

    test_list.append(random.sample(lines, ten_pc))

#  with open("test.txt", "w+") as wr:
  #    for i in test_list:
   #       print(i)
   #       wr.write(i)

f.close()

# print(len(test_list))
# for i in test_list:
#     print(i)
#     print()

