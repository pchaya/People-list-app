# Prathyoosha Chaya, OSURC Rover Club Software Team Mastery Challenge 2017
# Python Lv. 2
# This program works with a directory of people.

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.createWindow()

    def createWindow(self):
        self.resize(1000, 800)
        self.move(200, 100)
        self.setWindowTitle('think of a better name')
        self.show()


# creating widget and displaying
if __name__ == '__main__':
    app = QApplication(sys.argv)    # creating application object
    window = Window()               # initializing/creating window
    sys.exit(app.exec_())

