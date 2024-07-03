# create a pyqt5 application that will open a dialogue box for selecting an image from the system and then display it
from components import ImageSelector, MainWidget, SidePanel, WorkPanel
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QFileDialog, QLabel, QVBoxLayout, QHBoxLayout, QTabWidget

import sys

from components.SidePanel import SidePanel

class mainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Augmenter")
        self.showMaximized()
        #self.image_selector = ImageSelector()
        self.main_widget = MainWidget()
        self.setCentralWidget(self.main_widget)
app = QApplication(sys.argv)

window = mainApp()
window.show()

app.exec_()



