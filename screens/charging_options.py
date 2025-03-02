# charging_options.py
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtCore import Qt
from styles.styles import PRIMARY_FONT, BUTTON_FONT, STYLESHEET

# Define the glow effect function (using QGraphicsDropShadowEffect)
from PyQt6.QtWidgets import QGraphicsDropShadowEffect

def apply_glow_effect(widget, color, blur_radius):
    effect = QGraphicsDropShadowEffect()
    effect.setColor(QColor(color))
    effect.setBlurRadius(blur_radius)
    effect.setOffset(0, 0)
    widget.setGraphicsEffect(effect)

import os

class ChargingOptionsScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()

        # Title Label
        title_label = QLabel("Select Charging Mode")
        title_label.setStyleSheet(STYLESHEET["primary_label"])
        title_label.setFont(PRIMARY_FONT)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Charging Buttons Layout
        buttons_layout = QHBoxLayout()
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Absolute paths to assets
        assets_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../assets'))
        path_60v = os.path.join(assets_path, '60.png')
        path_48v = os.path.join(assets_path, '48.png')

        # Check if assets folder exists
        if not os.path.exists(assets_path):
            print(f"Warning: Assets folder '{assets_path}' not found!")

        # Create Buttons
        btn_60v = self.charging_option_button("60V/32AH", "₱100 per Hour", path_60v, 2)
        btn_48v = self.charging_option_button("48V/32AH", "₱60 per Hour", path_48v, 2)

        buttons_layout.addWidget(btn_60v)
        buttons_layout.addWidget(btn_48v)
        layout.addLayout(buttons_layout)

        # Add glow effects to buttons
        apply_glow_effect(btn_60v, color="#008080", blur_radius=60)
        apply_glow_effect(btn_48v, color="#ADD8E6", blur_radius=60)  # Different color for 48V

        # Back Button
        back_button = QPushButton("Back")
        back_button.setFont(BUTTON_FONT)
        back_button.setFixedSize(170, 70)
        back_button.setStyleSheet(STYLESHEET["back_button"]) 
        back_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)

        apply_glow_effect(back_button, color="#777777", blur_radius=40)

        # Adjust layout spacing and margins
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)
        self.setLayout(layout)

    def charging_option_button(self, voltage, price, img_path, index):
        button = QPushButton()
        button.setFont(BUTTON_FONT)
        button.setStyleSheet(STYLESHEET["charging_button"])

        button_widget = QWidget()
        button_layout = QVBoxLayout(button_widget)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_widget.setStyleSheet("background-color: transparent;")  

        if os.path.exists(img_path):
            icon_label = QLabel()
            pixmap = QPixmap(img_path).scaled(130, 130, Qt.AspectRatioMode.KeepAspectRatio)
            icon_label.setPixmap(pixmap)
            icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            button_layout.addWidget(icon_label)
        else:
            print(f"Warning: Image '{img_path}' not found!")

        voltage_label = QLabel(voltage)
        voltage_label.setFont(BUTTON_FONT)
        voltage_label.setStyleSheet(STYLESHEET["charging_label"])
        voltage_label.setObjectName("voltage")
        button_layout.addWidget(voltage_label)

        price_label = QLabel(price)
        price_label.setFont(BUTTON_FONT)
        price_label.setStyleSheet(STYLESHEET["charging_label"])
        price_label.setObjectName("price")
        button_layout.addWidget(price_label)

        button.setLayout(button_layout)
        button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(index))

        return button