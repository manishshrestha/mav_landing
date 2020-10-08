"""
Partitions the JPG images in the current folder into training and test set. 10 % is used for
test set and 90% for training set. The corresponding filename of the images will be put at test.txt and train.txt.

In order to use this script, 
- copy this script to the directory containing the jpg images 
- change the variable path_data to indicate the relative path of the image folder w.r.t. darknet.exe file
- run this script.

For ex:
Manish@DESKTOP-P2JM14I MINGW64 ~/Documents/MachineLearning/darknet_alexeyAB/darknet/build/darknet/x64/lspot_data/img (master)
$ /c/Python27/python.exe separate_train_test_set.py


Source code for this script has been referenced from https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/ .
"""
import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory where the data will reside, relative to 'darknet.exe'
path_data = 'lspot_data/img/'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    #file = open(title + '.txt', 'w')
    #file.write('0 0.5 0.5 1 1')
    #file.close()

    if counter == index_test:
        counter = 1
        file_test.write(path_data + title + '.jpg' + "\n")
    else:
        file_train.write(path_data + title + '.jpg' + "\n")
        counter = counter + 1
