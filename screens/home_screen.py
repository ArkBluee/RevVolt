from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt
from styles.styles import STYLESHEET, PRIMARY_FONT, SUB_FONT, START_BUTTON_FONT
from styles.effects import apply_glow_effect  # Import the static glow effect function

class HomeScreen(QWidget):
    """Home Screen of the RevVolt Charging Station"""

    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()

        # Primary Label (RevVolt)
        self.primary_label = QLabel("RevVolt")
        self.primary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.primary_label.setStyleSheet(STYLESHEET["primary_label"])
        layout.addWidget(self.primary_label)

        # Sub Label (Fast Charging Station)
        self.sub_label = QLabel("E-TRIKE CHARGING STATION")
        self.sub_label.setFont(SUB_FONT)
        self.sub_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sub_label.setStyleSheet(STYLESHEET["sub_label"])
        layout.addWidget(self.sub_label)

        # Add a spacer below the labels to separate them from the button
        layout.addItem(QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Start Button (Circular with Static Glow)
        self.start_button = QPushButton("Start")
        self.start_button.setFont(START_BUTTON_FONT)
        self.start_button.setFixedSize(200, 200)  # Circular Size
        self.start_button.setStyleSheet(STYLESHEET["start_button"])
        self.start_button.clicked.connect(self.go_to_charging_options)

        layout.insertWidget(3, self.start_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Apply Static Glow Effect to the start button
        apply_glow_effect(self.start_button, color="#008080", blur_radius=300)

        # Extra stretch below to balance UI
        layout.addStretch()

        layout.setContentsMargins(40, 20, 40, 60)  # Adjust top and bottom margins
        self.setLayout(layout)

    def go_to_charging_options(self):
        """Navigate to Charging Options Screen"""
        self.stacked_widget.setCurrentIndex(1)
