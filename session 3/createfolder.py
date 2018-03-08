# Our goal now is to write a function that creates a folder inside a base directory with a name,
# but only if that name does not exist.

# To accomplish this, we use the os module once again. We use two main functions, os.path.exists(), and os.mkdir().
# We use os.path.exists() to check whether the directory exists, if it does not, we create it.

import os

def create_folder_if_not_exists(base_dir, dir_name):
    dir_path = os.path.join(base_dir, dir_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

create_folder_if_not_exists('data', 'Friends')