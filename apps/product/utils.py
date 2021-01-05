import os
import random

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    # hello / .jpg
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(666666, 3888888888)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'{new_filename}/{final_filename}'

