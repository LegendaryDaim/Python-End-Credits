# This is configuration file. I just try to collect as many useful variables as possible here
# Temporary Flags for testing or for skipping stuff
flag_sheet = True
flag_create_image = True
flag_create_video = True
flag_delete_images_when_done = False  # Removes *.png images after video is done
flag_verbose = False

link = 'https://docs.google.com/spreadsheets/d/11wK2-57CVlX4it5LGqW0bSOHbmm8YkvqB2Oyp1zvtnE/edit#gid=0'
speed = 2   # default 3 as in speed of scrolling. Might be pixels per frame. Should be safe integer speeds.

height = 1080
width = 1920

fps = 24    # default 24 important to avoid jitter

spacing = 60  # default 100 spacing between rows

tot_rows = 23

gap = 50

# Calculating total length of composition needed for the length of the sheet
length_frames = int((height + spacing * tot_rows) / speed)  # formula for calculating length of the comp

# length_frames = 1 # if you only want 1 frame

# set font
font_left = "TREBUC" + ".ttf"
font_right = "TREBUC" + ".ttf"
font_center = "TREBUC" + ".ttf"

print("config Loaded")
