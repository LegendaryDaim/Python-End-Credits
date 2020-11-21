# This is configuration file. I just try to collect as many useful variables as possible here
# Temporary Flags for testing or for skipping stuff
flag_sheet = True
flag_create_image = True
flag_create_video = True
flag_keep_images_when_done = True

link = 'https://docs.google.com/spreadsheets/d/11wK2-57CVlX4it5LGqW0bSOHbmm8YkvqB2Oyp1zvtnE/edit#gid=0'
speed = 2   # default 3 as in speed of scrolling. Might be pixels per frame. Should be safe integer speeds.

height = 1080
width = 1920

fps = 24    # default 24 important to avoid jitter

spacing = 60  # default 100 spacing between rows

tot_rows = 23

# Calculating total length of composition needed for the length of the sheet
length_frames = int((height + spacing * tot_rows) / speed)  # formula for calculating lenght of the comp

# set font
font_left = "TREBUC" + ".ttf"
font_right = "TREBUC" + ".ttf"
font_center = "TREBUC" + ".ttf"

print("config Loaded")