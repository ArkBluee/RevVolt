from PyQt6.QtGui import QFont

# Fonts
PRIMARY_FONT = QFont("Montserrat", 35, QFont.Weight.Bold)
SUB_FONT = QFont("Montserrat", 18)
BUTTON_FONT = QFont("Montserrat", 16)

# Color Palette
PRIMARY_COLOR = "#1B3A57"  # Navy Blue
SECONDARY_COLOR = "#D9D9D9"  # Light Gray
BACKGROUND_COLOR = "#F5F5F5"  # White Gray
TEXT_COLOR = "#333333"  # Dark Gray
ACCENT_COLOR = "#A0A0A0"  # Metallic Gray

# Stylesheets
STYLESHEET = {
    "window": f"background-color: {BACKGROUND_COLOR};",
    
    # Labels
    "primary_label": f"""
        QLabel {{
            color: {PRIMARY_COLOR};
            font-size: 35px;
            font-weight: bold;
            text-align: center;
        }}
    """,
    "sub_label": f"""
        QLabel {{
            color: {TEXT_COLOR};
            font-size: 18px;
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
            transition: 0.3s;
        }}
        QPushButton:hover {{
            background-color: {ACCENT_COLOR};
        }}
    """,
    
    "charging_button": f"""
        QPushButton {{
            background-color: {SECONDARY_COLOR};
            color: {TEXT_COLOR};
            font-weight: bold;
            border-radius: 10px;
            padding: 15px;
            font-size: 18px;
        }}
        QPushButton:hover {{
            background-color: {ACCENT_COLOR};
        }}
    """,
    
    "start_button": f"""
    QPushButton {{
        background-color: {PRIMARY_COLOR};
        color: white;
        font-weight: bold;
        font-size: 24px;
        border-radius: 100px;  /* Circular shape */
        padding: 10px;
        width: 200px;
        height: 200px;
        border: 5px solid white; /* Adds an outer border */
    }}
    QPushButton:hover {{
        background-color: {ACCENT_COLOR};
    }}
""",



    # Input Fields
    "input_field": f"""
        QLineEdit {{
            background-color: {ACCENT_COLOR};
            color: {TEXT_COLOR};
            border: 2px solid {PRIMARY_COLOR};
            border-radius: 10px;
            padding: 5px;
            font-size: 16px;
        }}
    """,

    # Header
    "header": f"""
        QLabel {{
            color: {PRIMARY_COLOR};
            font-size: 32px;
            font-weight: bold;
        }}
    """,

    # Frames
    "frame": f"background-color: {ACCENT_COLOR}; border-radius: 10px; padding: 10px;",

    # Progress Bar
    "progress_bar": f"""
        QProgressBar {{
            border-radius: 10px;
            background-color: {ACCENT_COLOR};
            height: 20px;
            text-align: center;
        }}
        QProgressBar::chunk {{
            background-color: {PRIMARY_COLOR};
            border-radius: 10px;
        }}
    """,
}

