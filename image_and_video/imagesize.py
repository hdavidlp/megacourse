import cv2
import os

base_dir = 'sample_images/'
output_dir = 'output_images/'

def get_name_ext(file_selected):
    dot_position = file_selected.find(".")
    return file_selected[:dot_position], file_selected[(len(file_selected)-dot_position-1)*-1:]

all_discovery_files = os.listdir(base_dir)

for file_Name in all_discovery_files:
    name, ext = get_name_ext(file_Name)
    selected_img = cv2.imread(base_dir + "/" + file_Name,1)
    resized_image = cv2.resize(selected_img, (100,100))
    cv2.imwrite(output_dir+"/"+ "th" + file_Name, resized_image)


