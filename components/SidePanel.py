from PyQt5.QtWidgets import QVBoxLayout, QWidget


class SidePanel(QWidget):
    """ 
    sidepanel will be called in another module called mainlayout and has buttons to change the 
    right panel panels
    """
    def __init__(self, *buttons):
        super().__init__()
        left_layout = QVBoxLayout()
        for button in buttons:
            left_layout.addWidget(button)

        left_layout.addStretch(5)
        left_layout.setSpacing(20)

        self.setLayout(left_layout)


        
        
