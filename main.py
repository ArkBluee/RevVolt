import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow
from screens import HomeScreen  # Import HomeScreen class
from screens import ChargingOptionsScreen  # Import ChargingOptionsScreen class
from screens import TimeOptionScreen  # Import TimeOptionScreen class
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

        # Initialize screens in the correct order
        self.home_screen = HomeScreen(self.stacked_widget)
        self.charging_options_screen = ChargingOptionsScreen(self.stacked_widget)
        self.time_option_screen = TimeOptionScreen(self.stacked_widget, 0)  # Temporary 0 for now
        self.insert_coin_screen = InsertCoinScreen(self.stacked_widget)
        self.charging_status = ChargingStatus(self.stacked_widget)

        # Add the screens to QStackedWidget in the correct order
        self.stacked_widget.addWidget(self.home_screen)              # Index 0
        self.stacked_widget.addWidget(self.charging_options_screen)  # Index 1
        self.stacked_widget.addWidget(self.time_option_screen)       # Index 2
        insert_coin_index = self.stacked_widget.addWidget(self.insert_coin_screen)  # ✅ Get correct index
        self.stacked_widget.addWidget(self.charging_status)          # Index 4

        # Now update time_option_screen with the correct insert_coin_index
        self.time_option_screen.insert_coin_index = insert_coin_index

        # Set the stacked widget as the central widget
        self.setCentralWidget(self.stacked_widget)

        # Set the window title and sizes
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
