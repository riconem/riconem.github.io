from time import sleep
from sh import raspistill, git
from subprocess import check_call, call
from PIL import Image
import os, glob, json
from crop import *

def captureImages(outputfile):
    raspistill("--output", outputfile)
    sleep(3)

def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def reduceResolution(filepath, resize=1):
    im = Image.open(filepath)
    width, height = im.size
    size = int(width*resize), int(height*resize)
    resized = im.resize(size, Image.ANTIALIAS)
    resized.save(filepath)

def reduceAll(folder, file_type = 'jpg'):
    glob_folder = os.path.join(folder, "*." + file_type)
    for image in glob.glob(glob_folder):
        reduceResolution(image)

def reduce_and_crop_all(folder, file_type = 'jpg', width=1920, height=1080):
    mod_folder = os.path.join(folder, 'reduced')
    createFolder(mod_folder)
    size = width, height
    glob_folder = os.path.join(folder, "*." + file_type)
    for image_path in glob.glob(glob_folder):
        mod_image =  os.path.join(mod_folder, os.path.basename(image_path))
        resize_and_crop(image_path, mod_image, size)

def JSONfromFileNames(folder, file_type = 'jpg'):
    glob_folder = os.path.join(folder, "*." + file_type)
    image_data = os.path.join(folder, 'images.json')
    images = []
    for image_path in sorted(glob.glob(glob_folder)):
        image_file = os.path.basename(image_path)
        images.append(image_file)
    with open(image_data, "w") as f:
        json.dump(images, f)

def removeImagesExcept(folder, hour='13', file_type = 'jpg'):
    glob_folder = os.path.join(folder, "*." + file_type)
    for image_path in glob.glob(glob_folder):
        image_file = os.path.basename(image_path)
        if "_" + hour in image_file:
            print(image_file)
        else:
            os.remove(image_path)

def add_JSON_to_js(picID):
    check_call(['./json_to_js.sh', picID])

def git_pull():
    git("pull", "origin", "master")

def git_change():
    call('./git_changes.sh')
