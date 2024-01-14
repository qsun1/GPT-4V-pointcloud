from PIL import Image
import os
from typing import List
from os.path import join

def merge_images(folders: List[str], target_folder: str, image_name: str):
    """
    Merge images with the same name from different folders into a single image.

    :param folders: List of folder names containing the images.
    :param target_folder: Name of the target folder to save the merged image.
    :param image_name: The common name of the images to be merged.
    """
    # Ensure the target folder exists
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    images = []
    # Load images
    for folder in folders:
        file_path = os.path.join(folder, image_name)
        if os.path.exists(file_path):
            images.append(Image.open(file_path))

    # Check if any images were loaded
    if not images:
        print("No images found with the name '{}' in the provided folders.".format(image_name))
        return

    # Assuming all images are of the same size
    total_width = sum(image.size[0] for image in images)
    max_height = max(image.size[1] for image in images)

    # Create a new blank image with the correct size
    merged_image = Image.new('RGB', (total_width, max_height))

    # Merge images
    x_offset = 0
    for image in images:
        merged_image.paste(image, (x_offset, 0))
        x_offset += image.size[0]

    # Save the merged image
    merged_image.save(os.path.join(target_folder, image_name))

    print("Merged image saved in '{}' folder as '{}'".format(target_folder, image_name))

# Example usage:
base_dir = './images/modelnet10/render_gray'
# merge_list = ['gray-view1', 'gray-view2', 'gray-view3', '1', '2', '6']
# targe_dir = '6-images'

merge_list = ['gray-view1', 'gray-view2', 'gray-view3', '1', '2', '3', '4', '5', '6', '7']
targe_dir = '10-images'

merge_list = [join(base_dir, d) for d in merge_list]
targe_dir = join(base_dir, targe_dir)


for i in range(50):
    merge_images(merge_list, targe_dir, f"{i}.png")
# This will merge "image.jpg" from "folder1", "folder2", and "folder3" into "target_folder"
