
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
from image_transformation import Rotation
from system_interaction import file_interaction
from cv2.typing import MatLike
from components import directoryselector
class RotateTab(QWidget):

    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('ROTATE'))
        self.rotate_backend = Rotation()
        self.directory_selector = directoryselector.DirectorySelector(self.rotate_backend.get_all_rotations())
        main_layout.addWidget(self.directory_selector)
        self.submitButton = QPushButton("rotate images")
        self.submitButton.clicked.connect(self.rotate_image)
        main_layout.addWidget(self.submitButton)
        main_layout.addStretch(5)
        self.setLayout(main_layout)


    def rotate_image(self):
        
        directory = self.directory_selector.get_input_directory()
        if directory:
            selected_blurs = self.directory_selector.get_augmentation_list()
            blurred_images = self.rotate_backend.apply_selected_rotation_on_multiple_images(directory, selected_blurs)
            print("rotate image type")
            output_directory = self.directory_selector.get_output_directory()
            print(output_directory)

            if output_directory:
                file_interaction().save_multiple_images(output_directory, blurred_images, 'rotate')

    
