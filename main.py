import sys
from PIL import Image
import cv2
import os
import time

def diaplay_ascii(image):
	os.system('cls')
	print(image)

def img_to_ascii(img, ascii_filename):
	# resize the image
	width, height = img.size
	aspect_ratio = height/width
	new_width = 120
	new_height = aspect_ratio * new_width * 0.55
	img = img.resize((new_width, int(new_height)))
	# new size of image
	# print(img.size)

	# convert image to greyscale format
	img = img.convert('L')

	pixels = img.getdata()

	# replace each pixel with a character from array
	chars = ["B","S","#","&","@","$","%","*","!",":","."]
	new_pixels = [chars[pixel//25] for pixel in pixels]
	new_pixels = ''.join(new_pixels)

	# split string of chars into multiple strings of length equal to new width and create a list
	new_pixels_count = len(new_pixels)
	ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
	ascii_image = "\n".join(ascii_image)
	diaplay_ascii(ascii_image)

	# # write to a text file.
	with open(ascii_filename, "a") as f:
		f.write(ascii_image)
		f.write('\n\n\n\n')


def main():
	# pass the image as command line argument
	video_path = sys.argv[1]
	txt_file_name = os.path.splitext(video_path)[0] + ".txt"
	# clears the file if it already exists.
	open(txt_file_name, "w").close()

	cap = cv2.VideoCapture(video_path)
	while True:
		ret, frame = cap.read()
		if not ret:
			break
		pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
		img_to_ascii(pil_img, txt_file_name)

if __name__ == "__main__":
	main()