from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from components import directoryselector
from system_interaction import file_interaction
from image_transformation import Blur 
class BlurTab(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('blur'))
        self.directory_selector = directoryselector.DirectorySelector()
        main_layout.addWidget(self.directory_selector)
        main_layout.addStretch(5)
        self.setLayout(main_layout)
    
    def blur_images(self):
        directory = self.directory_selector.get_input_directory()
        if directory:
            blurred_images = Blur().apply_selected_blurs_on_multiple_images(directory, selected_blurs = ['gaussian_blur','median_blur','bilateral_filter'])
