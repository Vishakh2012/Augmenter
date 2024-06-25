# a pyqt widget that allows the user to select a directory that has several images and these images will then be all be  by 90 degrees and saved to another directory which will also be selected by a widget

from PyQt5.QtWidgets import QCheckBox, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtCore import Qt

class DirectorySelector(QWidget):
    def __init__(self, augmentation_list: list):
        '''
        arguments : augmentation_list : list of string listing all augmentations applied
        '''
        super().__init__()
        self.file_name = None
        self.augmentation_list = augmentation_list
        self.checkboxes = []
        self.initUI()
        
    def initUI(self):
        vbox = QVBoxLayout()

        
        self.btn = QPushButton("Select Directory with initial dataset")
        vbox.addWidget(self.btn)
        self.btn.clicked.connect(self.open_input_dialog_box)

        for augmentation in self.augmentation_list:
            #get unique checkbox  for each augmentation
            checkbox = QCheckBox(augmentation)
            checkbox.stateChanged.connect( self.checkbox_list_updated)
            vbox.addWidget(checkbox)
        
        self.btn2 = QPushButton("Select Directory for augmented images")
        self.btn2.clicked.connect(self.open_output_dialog_box)
        vbox.addWidget(self.btn2)
        self.setLayout(vbox)


    def open_input_dialog_box(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        
        if directory:
            self.input_directory = directory
   

    def open_output_dialog_box(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        
        if directory:
            self.output_directory = directory


    def get_input_directory(self):
        return self.input_directory

    
    def get_output_directory(self):
        return self.output_directory
    
    def checkbox_list_updated(self):
        sender = self.sender()
        if not isinstance(sender, QCheckBox):
            return  # Exit if sender is not a QCheckBox
        
        augmentation = sender.text()

        if sender.isChecked():
            if augmentation not in self.checkboxes:
                self.checkboxes.append(augmentation)
        else:
            if augmentation in self.checkboxes:
                self.checkboxes.remove(augmentation)
        
        print("Checked augmentations:", self.checkboxes)

    def get_augmentation_list(self):
        return self.checkboxes
