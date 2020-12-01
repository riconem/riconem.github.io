from makeimage import reduce_and_crop_all
import os

file_dir = os.path.dirname(os.path.realpath(__file__))
image_dir = os.path.join(file_dir, "images", "Planarien_fast")
reduce_and_crop_all(image_dir, file_type = 'jpg', width=1920, height=1080)