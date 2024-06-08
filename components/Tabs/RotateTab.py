
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
from image_transformation import Rotation
from system_interaction import file_interaction
from cv2.typing import MatLike
from components import ImageSelector

class RotateTab(QWidget):

    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('ROTATION'))
        self.image_selector = ImageSelector()
        main_layout.addWidget(self.image_selector)
        main_layout.addStretch(5)
        self.button = QPushButton("Rotate")
        self.button.clicked.connect(self.rotate_image)
        main_layout.addWidget(self.button)
        self.setLayout(main_layout)
        


    def rotate_image(self):
        if self.image_selector.getFileName():
            rotated_image = Rotation().rotateByAngle(self.image_selector.getFileName(), 90)
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
        if self.image_selector.getFileName():
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

    
