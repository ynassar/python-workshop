# Here, our goal is to write a function to check whether a given filename is a valid video file.
# To do this, we simply check the extension of the filename. If the extension is a valid video file extension, we return True, else we return False
# The valid video extensions are ['mkv', 'avi', 'mp4']

# To do this, we use the os.path.splittext() function, which returns two things; the file name, and the extension.
# We then use the "in" operator to check whether the extension is a video extension.

def is_video(filename):
    