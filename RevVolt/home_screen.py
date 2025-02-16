from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from styles import STYLESHEET, PRIMARY_FONT, SUB_FONT, BUTTON_FONT


class HomeScreen(QWidget):
    """ Home Screen of the RevVolt Charging Station """

    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()
        
        # Primary Label
        self.primary_label = QLabel("R e v  V o l t")
        self.primary_label.setFont(PRIMARY_FONT)
        self.primary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.primary_label.setStyleSheet(STYLESHEET["primary_label"])
        layout.addWidget(self.primary_label)

        # Sub Label
        self.sub_label = QLabel("FAST CHARGING STATION")
        self.sub_label.setFont(SUB_FONT)
        self.sub_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sub_label.setStyleSheet(STYLESHEET["sub_label"])
        layout.addWidget(self.sub_label)

        # Start Button
        self.start_button = QPushButton("Start")
        self.start_button.setFont(BUTTON_FONT)
        self.start_button.setStyleSheet(STYLESHEET["button"])
        self.start_button.clicked.connect(self.go_to_charging_options)  # Navigate to next screen
        layout.addWidget(self.start_button, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.setSpacing(15)
        layout.setContentsMargins(40, 40, 40, 40)
        self.setLayout(layout)

    def go_to_charging_options(self):
        """ Navigate to Charging Options Screen """
        self.stacked_widget.setCurrentIndex(1)
