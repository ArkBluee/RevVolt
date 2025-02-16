from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from home_screen import HomeScreen
from charging_options import ChargingOptionsScreen


class RevVoltApp(QMainWindow):
    """ Main Application Class """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("RevVolt Charging Station")
        self.setFixedSize(800, 480)  # Fixed resolution, no maximize

        # Stacked Widget for switching screens
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Add Screens to StackedWidget
        self.stacked_widget.addWidget(HomeScreen(self.stacked_widget))
        self.stacked_widget.addWidget(ChargingOptionsScreen(self.stacked_widget))


# Run the App
if __name__ == "__main__":
    app = QApplication([])
    window = RevVoltApp()
    window.show()
    app.exec()