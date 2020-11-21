import fetching_sheets as fs
import create_image
import make_video
import sys
import os
import config as c

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from form import Ui_CreditsRoll

title_sheet = ""

# todo commend for console if I forget pyuic5 -x form.ui -o form.py

# UI WINDOW
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_CreditsRoll()
        self.ui.setupUi(self.main_win)

        # Connect signal to slots. Button Activates Functions
        self.ui.name_of_sheet.setText(title_sheet)

        # Run Button that runs the whole process
        self.ui.RunButton.clicked.connect(self.run_button)

        # input and button that gets sheet data
        self.ui.pushButton.clicked.connect(self.button_click)
        self.ui.lineEdit.setText(c.link)

        # Resolution button and text.
        self.ui.width_line.setText(str(c.width))
        self.ui.height_line.setText(str(c.height))

        # fps line
        self.ui.fps_line.setText(str(c.fps))

        # total lenght
        self.ui.lenght_line.setText(str(c.length_frames))

        # END of connect signal to slots

    def show(self):
        self.main_win.show()

    # Code to Run and functions goes here

    def button_click(self): # Save link variable
        c.link = self.ui.lineEdit.text()
        print (c.link)
        main_text, title_sheet = fs.get_sheet()
        self.ui.name_of_sheet.setText(title_sheet)

    def run_button(self):
        # Sets whatever res you put into the res boxes.
        width = self.ui.width_line.text()
        height = self.ui.height_line.text()
        c.width = int(width)
        c.height = int(height)

        # For the fps
        fps = self.ui.fps_line.text()
        c.fps = int(fps)

        # Print using this lenght
        lenght = self.ui.lenght_line.text()
        c.length_frames = int(lenght)

        main_text, title_sheet = fs.get_sheet()  # get sheet data and title
        if c.flag_create_image:
            create_image.create_image(main_text)  # Creates an png Image using string
        if c.flag_create_video:
            make_video.make_video()  # # way of getting png into a movie sequece. Can me done on FFmpeg
        if not c.flag_keep_images_when_done:  # delete images
            os.listdir('images')
            for i in os.listdir('images'):
                os.remove(f"images/{i}")

# End of Code to run

# Main look or whatever
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

# Todo Save list_of_list in a txt file and only fetch information once per run.