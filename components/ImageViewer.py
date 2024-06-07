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
        self.button = QPushButton("Rotate Image") 
        self.button.clicked.connect(self.rotate_image)
        layout.addWidget(self.button)
        


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

    def rotate_image(self):
        if self.file_name:
            rotated_image = Rotation().rotateByAngle(self.file_name, 90)
            file_saved = self.save_image_component(rotated_image)
            if(file_saved):
                 pixmapx = QPixmap("rotated_image.jpg")
                 pixmapx = pixmapx.scaled(400, 400)
                 #show the image
                 self.label.setPixmap(pixmapx)

            else:
                 error_message = "Error in saving the file"
                 print(error_message)

        else:
            print("Please select an image first")

    def select_output_file_location(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)", options=options)
        return file_name
    
    def save_image_component(self, image: MatLike):
        if self.file_name:
            file_name = self.select_output_file_location()
            if file_name:
                print(file_name)
                file_saved = file_interaction().save_image(file_name, image, "original")
                if(file_saved):
                    return True
                else:
                    return False
        else:
            print("Please select an image first")
