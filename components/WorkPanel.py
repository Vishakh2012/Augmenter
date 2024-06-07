from PyQt5.QtWidgets import QTabWidget, QWidget

class WorkPanel(QTabWidget):
    
    def __init__(self, *tabs):
        super().__init__()
        self.tabBar()
        for tab in tabs:
            self.addTab(tab, '')

        self.setCurrentIndex(0)
        self.setStyleSheet(''' QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')
        
