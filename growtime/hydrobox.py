from datetime import datetime
from makeimage import *
from crop import *

picID = 'hydrobox'
shot_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
resize=1

# new file in /images/picID/shot_time.jpg
file_dir = os.path.dirname(os.path.realpath(__file__))
image_dir = os.path.join(file_dir, "images")
pic_dir = os.path.join(image_dir, picID)
file_name = shot_time + ".jpg"
file_path = os.path.join(pic_dir, file_name)
createFolder(pic_dir)

# capture image and resize
captureImages(file_path)
size = 1920, 1080
resize_and_crop(file_path, file_path, size)

# create JSON from File Names in picDir
JSONfromFileNames(pic_dir)

# add JSON data to js dist/images.js
add_JSON_to_js(picID)

# make git changes
git_change()
