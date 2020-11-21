from PIL import Image, ImageDraw, ImageFont
import os
import sys
import config as c

# TODO Make PIL draw pictures
flag_is_right_upper = True

def create_image(text):
    size = c.width, c.height
    start_pos = c.height # 500    # 500 is temporary
    progress_bar = ""

    if os.name == 'nt': # set different font directory depending on Win or Mac
        font_dir = 'C:\Windows\Fonts\\'
    else:
        font_dir = '/Library/Fonts/'

    fnt_left = ImageFont.truetype(f'{font_dir}{c.font_left}', 30)
    fnt_right = ImageFont.truetype(f'{font_dir}{c.font_right}', 36)
    fnt_center = ImageFont.truetype(f'{font_dir}{c.font_center}', 45)

    # format text
    for frame in range(0, c.length_frames):
        img = Image.new('RGB', (size), color='black')  # Need this to refresh background
        for num, i in enumerate(text):
            #print(text[num])
            text_name = ((text[num])[0])
            text_lastname = ((text[num])[1])
            text_credits = ((text[num])[2])

            if flag_is_right_upper:
                text_role_one = ((text[num])[3]).upper()
                text_role_two = ((text[num])[4]).upper()
            else:
                text_role_one = ((text[num])[3])
                text_role_two = ((text[num])[4])

            sys.stdout.write("\rCreating .*png               DONE " + str((progress_bar)) + "%")
            sys.stdout.flush()
            progress_bar = int(round(frame / c.length_frames, 2) * 100)

            # Draw test on screen
            draw_left = ImageDraw.Draw(img)
            #draw_left.text((c.width/2-100, start_pos+num*c.spacing-frame*c.speed), f"{text_name} {text_lastname}", align="right", anchor="ra", font=fnt_left, fill=(200, 200, 200))
            draw_left.text((c.width / 2 - 100, start_pos + num * c.spacing - frame * c.speed), f"{text_name} {text_lastname}", align="right", anchor="ra", font=fnt_left, fill=(200, 200, 200))
            draw_mid = ImageDraw.Draw(img)
            draw_mid.text((c.width/2, start_pos+num*c.spacing-frame*c.speed), f"{text_credits}", align="center", anchor="ma", font=fnt_center, fill=(200, 200, 200))
            draw_right = ImageDraw.Draw(img)
            draw_right.text((c.width/2+100, start_pos+num*c.spacing-frame*c.speed), f"{text_role_one} {text_role_two}", align="left", anchor="la", font=fnt_right, fill=(225, 225, 225))

        img.save(f"images/clean{frame:05d}.png")
