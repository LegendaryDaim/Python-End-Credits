from PIL import Image, ImageDraw, ImageFont
import os
import sys
import config as c

# TODO Make PIL draw pictures

flag_is_right_upper = True

def create_image(text):
    size = c.width, c.height
    # start_pos = 0     # Temporary for 1 frame outputs
    start_pos = c.height

    if os.name == 'nt': # set different font directory depending on Win or Mac
        font_dir = 'C:\Windows\Fonts\\'
    else:
        font_dir = '/Library/Fonts/'

    fnt_left = ImageFont.truetype(f'{font_dir}{c.font_left}', 30)
    fnt_right = ImageFont.truetype(f'{font_dir}{c.font_right}', 36)
    fnt_center = ImageFont.truetype(f'{font_dir}{c.font_center}', 45)

    for frame in range(0, c.length_frames):  # Draws 1 frame for 1 iteration of the loop
        img = Image.new('RGB', (size), color='black')  # Need this to refresh background after each draw

        for num, i in enumerate(text):  # Draws text on scree withing those frames
            text_row = ((text[num]))
            text_0 = ((text[num])[0])
            text_1 = ((text[num])[1])
            text_2 = ((text[num])[2])
            text_3 = ((text[num])[3])
            text_4 = ((text[num])[4])

            progress_bar(frame)     # progress bar in console

            rowflag = func_rowflag(text_row) # returns rowflag

            if rowflag == 2:    # prints middle TITLES
                # print("DRAW ON SCREEN -> " + text_2)
                ImageDraw.Draw(img).text((c.width / 2, start_pos + num * c.spacing - frame * c.speed),
                                         f"{text_2}", align="center", anchor="ma", font=fnt_center, fill=(200, 200, 200))

            if rowflag == 13:   # Prints if ony collum 1 or 3 is full
                ImageDraw.Draw(img).text((c.width / 2 - c.gap, start_pos + num * c.spacing - frame * c.speed),
                                         f"{text_1}", align="right", anchor="ra", font=fnt_left, fill=(200, 200, 200))
                ImageDraw.Draw(img).text((c.width / 2 + c.gap, start_pos + num * c.spacing - frame * c.speed),
                                         f"{text_3}", align="left", anchor="la", font=fnt_right, fill=(225, 225, 225))
                # print("DRAW ON SCREEN - > " + text_1 + " " + text_3)

            if rowflag == 1234:
                ImageDraw.Draw(img).text((c.width / 3 - c.gap, start_pos + num * c.spacing - frame * c.speed),
                                         f"{text_0}", align="right", anchor="ra", font=fnt_left, fill=(200, 200, 200))
                ImageDraw.Draw(img).text((c.width / 3 + c.gap, start_pos + num * c.spacing - frame * c.speed),
                                         f"{text_1}", align="left", anchor="la", font=fnt_right, fill=(225, 225, 225))

                ImageDraw.Draw(img).text((c.width / 3 * 2 - c.gap, start_pos + num * c.spacing - frame * c.speed),
                                         f"{text_3}", align="right", anchor="ra", font=fnt_left, fill=(200, 200, 200))
                ImageDraw.Draw(img).text((c.width / 3 * 2 + c.gap, start_pos + num * c.spacing - frame * c.speed),
                                         f"{text_4}", align="left", anchor="la", font=fnt_right, fill=(225, 225, 225))

            if rowflag == 10:  # Prints if ony collum 0 and 1 is full
                ImageDraw.Draw(img).text((c.width / 2 - c.gap, start_pos + num * c.spacing - frame * c.speed),
                                         f"{text_0}", align="right", anchor="ra", font=fnt_left,
                                         fill=(200, 200, 200))
                ImageDraw.Draw(img).text((c.width / 2 + c.gap, start_pos + num * c.spacing - frame * c.speed),
                                         f"{text_1}", align="left", anchor="la", font=fnt_right,
                                         fill=(225, 225, 225))

               # print("DRAW ON SCREEN - > " + text_1 + " " + text_3)
               # print("DRAW ON SCREEN - > " + text_0 + " " + text_1 + " AND " + text_3 + " " + text_4)

        img.save(f"images/clean{frame:05d}.png")
        # print("--------SAVE IMAGE--------")

def progress_bar(frame):
    progress_bar = int(round(frame / c.length_frames, 2) * 100)
    sys.stdout.write("\rCreating .*png               DONE " + str((progress_bar)) + "%")
    sys.stdout.flush()

def func_rowflag(text_row):
    if not text_row[0] and not text_row[1] and not text_row[2] and not text_row[3] and not text_row[4]:
        return 0
    if text_row[2]:
        return 2
    if text_row[0] and text_row[1] and not text_row[3]:
        return 10
    if text_row[1] and text_row[3] and not text_row[0]:
        return 13
    if text_row[0] and text_row[1] and text_row[3] and text_row[4]:
        return 1234
    else:
        return 9