"""
Convert images in a folder to local resources and write a file with their img tags.
Good for bulk uploading.
"""
# import our library
import pyimgur

# import system IO
import sys
import os

CLIENT_ID = 'your client id here'
im = pyimgur.Imgur(CLIENT_ID)

dir_path = input("Folder path? ")
output = input("Output name? ")
width = input("What width do you want your images to be? ")
images = {} # dict which will contain imgur links
files_in_dir = os.listdir(dir_path)

# iterate through folder files and obtain imgur link of each
for file in files_in_dir:
	uploaded_image = im.upload_image(dir_path + '\\' + file)
	images[file] = uploaded_image.link

# write to file with img tags
print("Writing file...")
target = open(dir_path + '\\' + output + '.html', 'w')

for image in images:
	file_link = images[image]
	target.write('<img src=\"' + file_link + '\" alt=\"' + image + '\" width=\"' + width + '\">')
	target.write("\n")

print("File written.")
target.close()




