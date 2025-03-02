from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout
from PyQt6.QtCore import Qt

from styles.styles import STYLESHEET, BUTTON_FONT

class InsertCoinScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()

        # Title Label
        title_label = QLabel("Insert Coin")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet(STYLESHEET["primary_label"])
        layout.addWidget(title_label)

        # Instruction Label
        instruction_label = QLabel("Please insert coins to begin charging.")
        instruction_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instruction_label.setStyleSheet(STYLESHEET["sub_label"])
        layout.addWidget(instruction_label)

        # Coin Counter Display
        self.coin_count = 0
        self.coin_label = QLabel(f"Coins Inserted: {self.coin_count}")
        self.coin_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.coin_label.setStyleSheet(STYLESHEET["sub_label"])
        layout.addWidget(self.coin_label)

        # Proceed Button
        self.proceed_button = QPushButton("Proceed")
        self.proceed_button.setFont(BUTTON_FONT)
        self.proceed_button.setStyleSheet(STYLESHEET["button"])
        self.proceed_button.clicked.connect(self.proceed_to_next_screen)
        self.proceed_button.setEnabled(True)  # Disable initially
        layout.addWidget(self.proceed_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Adjust layout spacing and margins
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)
        self.setLayout(layout)

    def add_coin(self, value):  # This function is no longer used
        pass  # Just pass, since no buttons to add coins

    def proceed_to_next_screen(self):
        """Navigate to the next screen."""
        # You can add logic here if you want to check for a minimum amount, etc.
        self.stacked_widget.setCurrentIndex(4)  # Just proceed directly
        # You might want to consider disabling the proceed button here if you
        # want the user to go through the insert coin screen again.
        self.proceed_button.setEnabled(True) # Disable for the next visit