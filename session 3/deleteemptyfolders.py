# Our task here is to create a python function that deletes all empty directories inside a base directory.

# To do this, we use three main functions from os. The first is os.walk(), which recursively traverses the file directory structure,
# and returns three things at each iteration step, (root, dirs, files).
# The second is os.listdir(), which returns all files and directories in a directory.
# The third is os.rmdir(), which removes an empty directory.

# We need to use os.walk() with topdown = False, to be able to delete empty directories inside empty directories.

# data -> (x -> y->()) c.txt
def cleanup(base_dir):
    for root, dirs, files in os.walk(base_dir, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if len(os.listdir(dir_path)) == 0:
                os.rmdir(dir_path)