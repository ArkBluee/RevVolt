from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import QGraphicsDropShadowEffect

# Fonts
PRIMARY_FONT = QFont("Montserrat", 45, QFont.Weight.Bold)
SUB_FONT = QFont("Montserrat", 18)
BUTTON_FONT = QFont("Montserrat", 19, QFont.Weight.Bold)
PRIMARY_BUTTON_FONT = QFont("Montserrat", 30, QFont.Weight.Bold)
START_BUTTON_FONT = QFont("Montserrat", 27, QFont.Weight.Bold)

# Color Palette
PRIMARY_COLOR = "#336699"  # Navy Blue
SECONDARY_COLOR = "#D9D9D9"  # Light Gray
BACKGROUND_COLOR = "black"  # Black background
TEXT_COLOR = "#FFFFFF"  # White text
ACCENT_COLOR = "#A0A0A0"  # Metallic Gray
MAIN_BUTTON_COLOR = "rgba(0, 0, 0, 0.5)"  # Semi-transparent black

# Specific colors for voltage and price text
VOLTAGE_COLOR = "#FFFFFF"  # White for voltage
PRICE_COLOR = "#FFD700"  # Gold/Yellow for price

# Stylesheets
STYLESHEET = {
    "window": f"background-color: {BACKGROUND_COLOR};",

    # Labels
    "primary_label": f"""
        QLabel {{
            color: {PRIMARY_COLOR};
            font-size: 45px; /* Fixed font size */
            font-weight: bold;
            text-align: center;
        }}
    """,
    "sub_label": f"""
        QLabel {{
            color: {TEXT_COLOR};
            font-size: 18px; /* Fixed font size */
            text-align: center;
        }}
    """,
    "option_label": f"""
        QLabel {{
            color: {PRIMARY_COLOR};
            font-size: 18px; /* Fixed font size */
            text-align: center;
        }}
    """,

    # Buttons
    "button": f"""
        QPushButton {{
            background-color: {SECONDARY_COLOR};
            color: {TEXT_COLOR};
            font-weight: bold;
            border-radius: 12px;
            padding: 12px;
        }}
    """,

    "back_button": f"""
        QPushButton {{
            background-color: #AAAAAA;
            color: {TEXT_COLOR};
            font-weight: bold;
            border-radius: 12px;
            padding: 12px;
            border: 1px solid #999999;
        }}
    """,

    # Charging Option Button (60V & 48V)
    "charging_button": f"""
        QPushButton {{
            background-color: {MAIN_BUTTON_COLOR};
            color: {TEXT_COLOR};
            font-weight: bold;
            border-radius: 20px;
            padding: 15px;
            font-size: 18px;
            width: 320px;
            height: 280px;
            border: 5px solid white;
            box-shadow: 0 0 10px {PRIMARY_COLOR};
            text-align: center;
        }}
        QPushButton:pressed {{
            background-color: {ACCENT_COLOR};
            box-shadow: 0 0 30px {PRIMARY_COLOR};
            border: 5px solid {PRIMARY_COLOR};
        }}
        QPushButton QLabel {{
            background-color: transparent;
        }}
    """,

    "time_option_button": f"""
        QPushButton {{
            background-color: {MAIN_BUTTON_COLOR};
            color: {TEXT_COLOR};
            font-weight: bold;
            border-radius: 15px;
            padding: 5px; 
            width: 100px;
            height: 80px;  
            border: 3px solid white;
            box-shadow: 0 0 10px {PRIMARY_COLOR};
            text-align: center;
            margin-top: 10px;
        }}
        QPushButton:pressed {{
            background-color: {ACCENT_COLOR};
            box-shadow: 0 0 20px {PRIMARY_COLOR};
            border: 3px solid {PRIMARY_COLOR};
        }}
        QPushButton QLabel {{
            background-color: transparent;
        }}
    """,


    # Start Button
    "start_button": f"""
        QPushButton {{
            background-color: {MAIN_BUTTON_COLOR};
            color: white;
            border-radius: 100px;
            width: 200px;
            height: 200px;
            border: 5px solid white;
            box-shadow: 0 0 10px {PRIMARY_COLOR};
        }}
        QPushButton:pressed {{
            background-color: {ACCENT_COLOR};
            border: 5px solid {PRIMARY_COLOR};
        }}
    """,

    # Labels
    "charging_label": f"""
        QLabel {{
            background-color: transparent;
            font-weight: bold;
            text-align: center;
        }}
        QLabel#voltage {{
            font-size: 28px;
            color: {VOLTAGE_COLOR};
        }}
        QLabel#price {{
            font-size: 24px;
            color: {PRICE_COLOR};
        }}
    """,

    "progress_bar": """
        QProgressBar {
            border-radius: 10px;
            background-color: #D9D9D9;
            height: 20px;
            text-align: center;
        }
        QProgressBar::chunk {
            background-color: #1B3A57;
            border-radius: 10px;
        }
    """,

    "charging_label_canceled": f"""
        QLabel {{
            color: red;
            font-size: 35px;
            font-weight: bold;
            text-align: center;
        }}
    """,
}

def apply_glow_effect(widget, color="#FFFFFF", blur_radius=20):
    """Applies a glowing effect to the given widget."""
    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(blur_radius)
    effect.setColor(QColor(color))
    effect.setOffset(0, 0)  # No offset, glow effect only
    widget.setGraphicsEffect(effect)
