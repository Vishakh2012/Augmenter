# create a pyqt5 application that will open a dialogue box for selecting an image from the system and then display it
from components import ImageSelector
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QFileDialog, QLabel, QVBoxLayout


class mainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Augmenter")
        self.setGeometry(100, 100, 800, 600)
        self.image_selector = ImageSelector()
        self.setCentralWidget(self.image_selector)
app = QApplication(sys.argv)

window = mainApp()
window.show()

app.exec_()



