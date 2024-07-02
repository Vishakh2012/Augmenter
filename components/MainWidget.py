from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout
from components import SidePanel, WorkPanel
from components.Tabs import RotateTab
from components.Tabs import BlurTab
from components.Tabs import PoolingTab
class MainWidget(QWidget):
    """
    This class takes multiple arguments and adds them to the current layout.
    """
    def __init__(self, left_widget=SidePanel, right_widget=WorkPanel):
        super().__init__()
        self.left_widget = left_widget
        self.right_widget = right_widget
        self.init_ui()
        
    def init_ui(self):
        self.init_widgets()
        self.setup_layout()

    def init_widgets(self):
        """
        Initialize widgets used in the main layout.
        """
        self.work_panel = self.right_widget(RotateTab(), BlurTab(), PoolingTab())
        
        self.btn1 = QPushButton("Rotation", self)
        self.btn2 = QPushButton("Blur", self)
        self.btn3 = QPushButton("Pooling", self)
        self.btn4 = QPushButton("Contrast", self)

        self.btn1.clicked.connect(self.selectRotationTab)
        self.btn2.clicked.connect(self.selectBlurTab)
        self.btn3.clicked.connect(self.selectPoolingTab)

        
        self.side_panel = self.left_widget(self.btn1, self.btn2, self.btn3, self.btn4)

    def setup_layout(self):
        """
        Set up the main layout of the widget.
        """
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.side_panel)
        main_layout.addWidget(self.work_panel)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)

        self.setLayout(main_layout)

    def change_page(self, index):
        """
        Change the page in the right panel.
        """
        self.work_panel.setCurrentIndex(index)

    def selectRotationTab(self):
        self.change_page(0)

    def selectBlurTab(self):
        self.change_page(1)

    def selectPoolingTab(self):
        self.change_page(2)
    
