from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget
from components import directoryselector
from system_interaction import file_interaction
from image_transformation import Pooling

class PoolingTab(QWidget):
    
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('POOLING'))
        self.pooling_backend = Pooling()
        self.directory_selector = directoryselector.DirectorySelector(self.pooling_backend.get_all_pooling())
        main_layout.addWidget(self.directory_selector)
        self.submitButton = QPushButton("Pooling images")
        self.submitButton.clicked.connect(self.pool_images)
        main_layout.addWidget(self.submitButton)
        main_layout.addStretch(5)
        self.setLayout(main_layout)

    
    def pool_images(self):
        directory = self.directory_selector.get_input_directory()
        if directory:
            selected_pooling = self.directory_selector.get_augmentation_list()
            pooled_images = self.pooling_backend.apply_selected_pooling_on_multiple_images(directory, selected_pooling)
            print("pool image type")
            print(type(pooled_images[0]))
            output_directory = self.directory_selector.get_output_directory()
            print(output_directory)

            if output_directory:
                file_interaction().save_multiple_images(output_directory, pooled_images, 'pool')
