from git import git_pull, git_change
from capture import Camera

#git_pull()

dl = Camera('dl', 'dl_2021_01_09')
dl.capture_image()
dl.create_json_from_images()
dl.add_json_to_js()

# git_change()
