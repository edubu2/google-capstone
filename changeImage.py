#!\\usr\\bin\\env python3

from PIL import Image
import os
import glob

image_dir = "C:\\Users\\Elliot\\Python\\Google\\capstone\\supplier-data\\images\\" # update to linux path
old_ext = '.tif' # change to .tiff for linux, .tif for windows
new_ext = '.jpg' # change to .jpeg for linux, .jpg for Windows

# get image filenames (full path) into a list
images = glob.glob(image_dir + '*')

def format_images(image_filenames):
  """Update image resolutions & format files as .jpeg"""
  for image in image_filenames:
    f, e = os.path.splitext(image) # separates filepath from it's extension (i.e. /home/file.ext --> '/home/file', '.ext')
    if e == old_ext:
      print("Working on {}...".format(image))
      im = Image.open(image).convert("RGB")
      new_im = im.resize((600,400)).save(f + new_ext)
      im.close()
      os.remove(image) # delete the original image

def main():
  format_images(images)

main()
