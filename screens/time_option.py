from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from styles.styles import apply_glow_effect, STYLESHEET, PRIMARY_BUTTON_FONT

class TimeOptionScreen(QWidget):
    def __init__(self, stacked_widget, insert_coin_index):
        super().__init__()
        self.stacked_widget = stacked_widget  # Reference to QStackedWidget
        self.insert_coin_index = insert_coin_index  # Index of InsertCoinScreen
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet(STYLESHEET["window"])  # Apply background color
            
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("Select Charging Duration")
        self.label.setStyleSheet(STYLESHEET["primary_label"])  # Apply label style
        layout.addWidget(self.label)
            
        # 1 Hour Button
        self.one_hour_button = QPushButton("1 Hour")
        self.one_hour_button.setFont(PRIMARY_BUTTON_FONT)
        self.one_hour_button.setStyleSheet(STYLESHEET["time_option_button"])  # Apply button style
        apply_glow_effect(self.one_hour_button)
        self.one_hour_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(self.insert_coin_index))
        layout.addWidget(self.one_hour_button)
            
        # 2 Hours Button
        self.two_hours_button = QPushButton("2 Hours")
        self.two_hours_button.setFont(PRIMARY_BUTTON_FONT)
        self.two_hours_button.setStyleSheet(STYLESHEET["time_option_button"])
        apply_glow_effect(self.two_hours_button)
        self.two_hours_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(self.insert_coin_index))
        layout.addWidget(self.two_hours_button)
            
        self.setLayout(layout)
