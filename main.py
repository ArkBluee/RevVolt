from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from screens import HomeScreen
from screens import ChargingOptionsScreen
from screens import ChargingScreen

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
        self.stacked_widget.addWidget(ChargingScreen(self.stacked_widget))


# Run the App
if __name__ == "__main__":
    app = QApplication([])
    window = RevVoltApp()
    window.show()
    app.exec()