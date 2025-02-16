from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize
from styles import PRIMARY_FONT, BUTTON_FONT, STYLESHEET
import os


class ChargingOptionsScreen(QWidget):
    """ Charging Options Screen """

    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()

        # Title Label
        title_label = QLabel("Select Charging Mode")
        title_label.setFont(PRIMARY_FONT)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Charging Buttons Layout
        buttons_layout = QHBoxLayout()

        # Absolute paths to assets
        assets_path = os.path.join(os.path.dirname(__file__), 'assets')
        path_60v = os.path.join(assets_path, '60.png')
        path_48v = os.path.join(assets_path, '48.png')

        # 60V Button
        btn_60v = QPushButton("60V/32AH\n₱100 per Hour")
        btn_60v.setFont(BUTTON_FONT)
        btn_60v.setStyleSheet(STYLESHEET["charging_button"])
        if os.path.exists(path_60v):
            btn_60v.setIcon(QIcon(QPixmap(path_60v)))
            btn_60v.setIconSize(QSize(100, 100))
        buttons_layout.addWidget(btn_60v)
        btn_60v.clicked.connect(lambda: stacked_widget.setCurrentIndex(2))

        # 48V Button
        btn_48v = QPushButton("48V/32AH\n₱60 per Hour")
        btn_48v.setFont(BUTTON_FONT)
        btn_48v.setStyleSheet(STYLESHEET["charging_button"])
        if os.path.exists(path_48v):
            btn_48v.setIcon(QIcon(QPixmap(path_48v)))
            btn_48v.setIconSize(QSize(100, 100))
        buttons_layout.addWidget(btn_48v)
        btn_48v.clicked.connect(lambda: stacked_widget.setCurrentIndex(2))  # Go to Charging Status

        layout.addLayout(buttons_layout)

        # Back Button
        back_button = QPushButton("Back")
        back_button.setFont(BUTTON_FONT)
        back_button.setFixedSize(150, 50)
        back_button.setStyleSheet(STYLESHEET["button"])
        back_button.clicked.connect(lambda: stacked_widget.setCurrentIndex(0))  # Go back to home
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.setSpacing(15)
        layout.setContentsMargins(40, 40, 40, 40)
        self.setLayout(layout)