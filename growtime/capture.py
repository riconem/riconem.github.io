from time import sleep
from sh import raspistill
from subprocess import check_call
import os, glob, json
from crop import resize_and_crop
from datetime import datetime

def newfolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

class Camera:
    def __init__(self, cam, project_id):
        self.cam = cam
        self.project_id = project_id
        file_dir = os.path.dirname(os.path.realpath(__file__))
        image_dir = os.path.join(file_dir, "images")
        newfolder(image_dir)
        self.project_dir = os.path.join(image_dir, project_id)
        newfolder(self.project_dir)

    def capture_image(self, resize=True, size=[1920, 1080]):
        shot_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        image_path = os.path.join(self.project_dir, shot_time + ".jpg")
        if self.cam == 'pi':
            raspistill("--output", image_path)
            sleep(5)
        elif self.cam == 'dl':
            check_call(['./switch_wlan.sh', 'dl'])
            sleep(5)
            check_call(['./dl_capture.sh', image_path])
            sleep(5)
            check_call(['./switch_wlan.sh', 'router'])
            sleep(5)
        else:
            return False
        if resize == True:
            resize_and_crop(image_path, image_path, size)

    def create_json_from_images(self):
        glob_folder = os.path.join(self.project_dir, "*." + "jpg")
        image_data = os.path.join(self.project_dir, 'images.json')
        images = []
        for image_path in sorted(glob.glob(glob_folder)):
            image_file = os.path.basename(image_path)
            images.append(image_file)
        with open(image_data, "w") as f:
            json.dump(images, f)
    
    def add_json_to_js(self):
        check_call(['./json_to_js.sh', self.project_id])
