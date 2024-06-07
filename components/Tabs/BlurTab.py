from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class BlurTab(QWidget):
    def __init__(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page1'))

        main = QWidget()
        main.setLayout(main_layout)
