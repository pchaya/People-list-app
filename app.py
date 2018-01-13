# Prathyoosha Chaya, OSURC Rover Club Software Team Mastery Challenge Python Lv. 2
# Oct 13, 2017
# This program read's the user's name from a GUI and puts it into a file.

import sys
from peopleList import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QGridLayout, QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.createWindow()         # setting up and showing window upon object creation

    # Creates application appearance and button functionality. Called upon the construction of a new window.
    def createWindow(self):
        # creating buttons, parent is of window class
        # set up a grid to display labels, buttons, and text input areas
        grid = QGridLayout()
        grid.setSpacing(10)

        # creating load button
        loadButton = QPushButton('Load and display "' + myList.name + '" members from file', self)
        loadButton.clicked.connect(self.loadGroup)
        loadButton.resize(loadButton.sizeHint())
        grid.addWidget(loadButton, 0, 0)

        # space to add more people to group
        addLabel = QLabel('List name(s) to add (seperate with only newline):')
        self.addEdit = QTextEdit()

        grid.addWidget(addLabel, 1, 0)
        grid.addWidget(self.addEdit, 2, 0, 3, 0)

        # creating save button
        saveButton = QPushButton('Save added member(s) and Quit', self)
        saveButton.clicked.connect(self.saveChanges)
        saveButton.resize(saveButton.sizeHint())
        grid.addWidget(saveButton, 5, 0)

        # creating quit button
        quitButton = QPushButton('Quit without saving', self)
        quitButton.clicked.connect(QCoreApplication.instance().quit)
        quitButton.resize(quitButton.sizeHint())
        grid.addWidget(quitButton, 6, 0)

        # create view
        self.setLayout(grid) 
        
        # setting window appearance, then showing window
        self.resize(1000, 800)
        self.move(200, 100)
        self.setWindowTitle('People List')
        self.setWindowIcon(QIcon('icon.png'))
        self.show()

    # This function writes names of the members to be added to the list, from the text entry box
    def saveChanges(self):
        toSave = self.addEdit.toPlainText().split('\n')
        myList.addList(toSave)
        QCoreApplication.quit()

    # This function allows the user to load the names of current members from the file
    def loadGroup(self):
        groupMembers = QMessageBox()
        groupMembers.setWindowTitle("Group members")
        groupMembers.setText(myList.display())
        
        groupMembers.setStandardButtons(QMessageBox.Close)
        groupMembers.exec_()

# creating widget and displaying
if __name__ == '__main__':
    myList = PeopleList()           # create a new group
    app = QApplication(sys.argv)    # creating application object
    window = Window()               # initializing/creating window
    sys.exit(app.exec_())


