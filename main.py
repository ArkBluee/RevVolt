import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow
from screens import HomeScreen  # Import HomeScreen class
from screens import ChargingOptionsScreen  # Import ChargingOptionsScreen class
from screens import InsertCoinScreen  # Import InsertCoinScreen class
from screens import ChargingStatus
from styles.styles import STYLESHEET

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QStackedWidget to handle screen transitions
        self.stacked_widget = QStackedWidget()

        # Apply the main window stylesheet
        self.setStyleSheet(STYLESHEET["window"])

        # Add screens to the stacked widget
        self.home_screen = HomeScreen(self.stacked_widget)
        self.charging_options_screen = ChargingOptionsScreen(self.stacked_widget)
        self.insert_coin_screen = InsertCoinScreen(self.stacked_widget)
        self.charging_status = ChargingStatus(self.stacked_widget)

        # Add the screens to the stacked widget by index
        self.stacked_widget.addWidget(self.home_screen)
        self.stacked_widget.addWidget(self.charging_options_screen)
        self.stacked_widget.addWidget(self.insert_coin_screen)
        self.stacked_widget.addWidget(self.charging_status)

        # Set the stacked widget as the central widget of the main window
        self.setCentralWidget(self.stacked_widget)

        # Set the window title and size
        self.setWindowTitle("RevVolt Charging Station")
        self.setGeometry(100, 100, 800, 480)  # Set window size to 800x480 (ideal for Raspberry Pi)

        # Make the window non-resizable
        self.setFixedSize(800, 480)

        # Show the main window
        self.show()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application instance
    window = MainWindow()  # Create the main window
    sys.exit(app.exec())  # Start the application event loop
