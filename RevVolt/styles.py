from PyQt6.QtGui import QFont

# Fonts
PRIMARY_FONT = QFont("Montserrat", 35, QFont.Weight.Bold)
SUB_FONT = QFont("Montserrat", 14)
BUTTON_FONT = QFont("Rajdhani", 14)

# Color Palette
PRIMARY_COLOR = "#66FCF1"  # Light Cyan
SECONDARY_COLOR = "#45A29E"  # Teal
BACKGROUND_COLOR = "#0B0C10"  # Dark Background
TEXT_COLOR = "#C5C6C7"  # Light Gray
ACCENT_COLOR = "#1F2833"  # Dark Gray Accent

# Stylesheets
STYLESHEET = {
    "window": "background-color: #0B0C10;",
    "primary_label": "color: #66FCF1; font-size: 24px; font-weight: bold;",
    "sub_label": "color: #C5C6C7; font-size: 18px;",
    "button": """
        QPushButton {
            background-color: #45A29E;
            color: white;
            font-weight: bold;
            border-radius: 15px;
            padding: 10px;
            font-size: 16px;
        }
        QPushButton:hover {
            background-color: #1F2833;
        }
    """,
    "input_field": """
        QLineEdit {
            background-color: #1F2833;
            color: #C5C6C7;
            border: 2px solid #66FCF1;
            border-radius: 10px;
            padding: 5px;
        }
    """,
    "header": """
        QLabel {
            color: #66FCF1;
            font-size: 32px;
            font-weight: bold;
        }
    """,
    "frame": "background-color: #1F2833; border-radius: 10px; padding: 10px;",
}