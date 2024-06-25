from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget
from components import directoryselector
from system_interaction import file_interaction
from image_transformation import Blur 
class BlurTab(QWidget):
 
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('BLUR'))
        self.blur_backend = Blur()
        self.directory_selector = directoryselector.DirectorySelector(self.blur_backend.get_all_blurs())
        main_layout.addWidget(self.directory_selector)
        self.submitButton = QPushButton("Blur images")
        self.submitButton.clicked.connect(self.blur_images)
        main_layout.addWidget(self.submitButton)
        main_layout.addStretch(5)
        self.setLayout(main_layout)

    
    def blur_images(self):
        directory = self.directory_selector.get_input_directory()
        if directory:
            selected_blurs = self.directory_selector.get_augmentation_list()
            blurred_images = self.blur_backend.apply_selected_blurs_on_multiple_images(directory, selected_blurs)
            print("blur image type")
            print(type(blurred_images[0]))
            output_directory = self.directory_selector.get_output_directory()
            print(output_directory)

            if output_directory:
                file_interaction().save_multiple_images(output_directory, blurred_images, 'blur')
