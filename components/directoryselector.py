# a pyqt widget that allows the user to select a directory that has several images and these images will then be all be rotated by 90 degrees and saved to another directory which will also be selected by a widget

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtCore import Qt

class DirectorySelector(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.lbl = QLabel("Select the directory that contains the images")
        self.vbox.addWidget(self.lbl)

        self.btn = QPushButton("Select Directory")
        self.btn.clicked.connect(self.get_directory)
        self.vbox.addWidget(self.btn)

        self.lbl2 = QLabel("Select the directory to save the rotated images")
        self.vbox.addWidget(self.lbl2)

        self.btn2 = QPushButton("Select Directory")
        self.btn2.clicked.connect(self.get_directory)
        self.vbox.addWidget(self.btn2)

        self.show()

    def get_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        print(directory)
