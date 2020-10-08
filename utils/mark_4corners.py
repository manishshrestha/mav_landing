"""
Tool to mark to the 4 corners visually using mouse clicks. The 4 corner should be marked from top left, top right,
 bottom right and bottom left sequentially.
 Press 'q' to quit. Press any other key to move to next images. 
 
Path to the folder containing images whose corners are to be detected. default: ./data/cornerDetectIn 
Output file: GroundTruthCornerDetection.csv

Sample output file content

sno	file_name		tl_x	tl_y	tr_x	tr_y	br_x	br_y	bl_x	bl_y
1	image_16.51.jpg	159		129		227		105		246		162		179		185
2	image_18.73.jpg	118		67		175		41		196		87		137		110
"""

import numpy as np
import glob
import os
import argparse
import cv2
import csv


__author__ = "Manish Shrestha"
__date__ = "06/13/2018"

counter = 1
current_file = ""
current_point_position = 0

register = []

def click(event, x, y, flags, param):
	global point, pressed, current_point_position, register
	if event == cv2.EVENT_LBUTTONDOWN:
		print("position %s, Pressed"%current_point_position, x, y)
		point = (x,y)
		register[counter-1][current_point_position*2+2] = x
		register[counter-1][current_point_position*2+3] = y
		current_point_position +=1
		if current_point_position>=4:
			current_point_position = 0



def begin_marking_4corners(inputfolder):
	global counter, register

	output_file_loc = "GroundTruthCornerDetection.csv"
	out_file = open(output_file_loc,'w')
	out_fieldnames = ['sno', 'file_name', 'tl_x','tl_y', 'tr_x', 'tr_y', 'br_x','br_y', 'bl_x', 'bl_y']
	output_writer = csv.DictWriter(out_file, fieldnames=out_fieldnames, delimiter=',')
	output_writer.writeheader()

	for imname in glob.iglob(os.path.join(inputfolder, "*.jpg")):  
		filename = os.path.basename(imname)
		print(imname)
		print(filename)
		#imname= os.path.join(inputfolder, filename)

		current_file = filename
		register.append([counter, current_file, -1,-1,-1,-1,-1,-1,-1,-1])
		current_point_position = 0

		frame = cv2.imread(imname)
		cv2.namedWindow("Frame")
		cv2.setMouseCallback("Frame", click)

		cv2.imshow("Frame",frame)

		key = cv2.waitKey(0) & 0xFF
		if key == ord('q'):
			break

		counter +=1
		if counter>=30:
			break

	print(register)

	for row in register:
		output_writer.writerow({ 'sno':row[0],
		'file_name':row[1],
		'tl_x':row[2], 'tl_y':row[3], 
		'tr_x':row[4], 'tr_y':row[5],
		'br_x':row[6], 'br_y':row[7], 
		'bl_x':row[8], 'bl_y':row[9]
	})
	out_file.close()



	cv2.destroyAllWindows()


def main():
    INPUT_FOLDER="./data/cornerDetectIn"

    parser = argparse.ArgumentParser(
        description="Tool to mark to the 4 corners visually. The 4 corner should be marked from top left, top right, bottom right and bottom left ")
    parser.add_argument("--inputfolder", default=INPUT_FOLDER, help="Path to the folder containing images whose corners are to be detected. default: ./data/cornerDetectIn ")

    args = parser.parse_args()

    INPUT_FOLDER = args.inputfolder

    begin_marking_4corners(INPUT_FOLDER)


if __name__ == "__main__":
	main()
