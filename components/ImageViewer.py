from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from cv2.typing import MatLike
from image_transformation import Rotation
from system_interaction import file_interaction
import cv2
class ImageSelector(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Selector")
        self.file_name = None
        layout = QVBoxLayout()

        self.label = QLabel()
        layout.addWidget(self.label)
        self.button = QPushButton("Select Image")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.select_image)
        self.setLayout(layout)
        layout.addWidget(self.button)
        

    get_file_name = lambda self: self.file_name
    def select_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)", options=options)
        
        if file_name:
            self.file_name = file_name
            pixmap = QPixmap(file_name)
            pixmap = pixmap.scaled(400, 400)
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(False)

        
    
