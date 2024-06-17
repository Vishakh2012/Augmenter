from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from components import directoryselector

class BlurTab(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('blur'))
        self.directory_selector = directoryselector.DirectorySelector()
        main_layout.addWidget(self.directory_selector)
        self.setLayout(main_layout)
