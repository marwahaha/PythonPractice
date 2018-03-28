import subprocess


image_name = input("Give directory of the image: ")
subprocess.call(["sudo", "mkdir", "/mnt/temp_image_mount"])
subprocess.call(["sudo", "mount", "-o", "ro", image_name, "/mnt/temp_image_mount"])