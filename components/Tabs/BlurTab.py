from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from components import directoryselector
from system_interaction import file_interaction
from image_transformation import Blur 
class BlurTab(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('blur'))
        self.blur_backend = Blur()
        self.directory_selector = directoryselector.DirectorySelector(self.blur_backend.get_all_blurs())
        main_layout.addWidget(self.directory_selector)
        main_layout.addStretch(5)
        self.setLayout(main_layout)

    
    def blur_images(self):
        directory = self.directory_selector.get_input_directory()
        if directory:
            selected_blurs = self.directory_selector.get_selected_augmentations()
            blurred_images = self.blur_backend.apply_selected_blurs_on_multiple_images(directory, selected_blurs)
            output_directory = self.directory_selector.get_output_directory()

            if output_directory:
                file_interaction().save_multiple_images(output_directory, blurred_images, 'blur')
