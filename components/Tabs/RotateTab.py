
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class RotateTab(QWidget):

    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('ROTATION'))
        main_layout.addStretch(5)
        self.setLayout(main_layout)


    
