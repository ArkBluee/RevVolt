from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton
from PyQt6.QtCore import Qt, QTimer
from styles import STYLESHEET  # Import styles

class ChargingScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        # Main Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Charging Label
        self.charging_label = QLabel("Charging in Progress...")
        self.charging_label.setStyleSheet(STYLESHEET["primary_label"])
        layout.addWidget(self.charging_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Charging Subtext
        self.subtext_label = QLabel("Please wait while your e-trike is charging")
        self.subtext_label.setStyleSheet(STYLESHEET["sub_label"])
        layout.addWidget(self.subtext_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Modern Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet(STYLESHEET["progress_bar"])
        layout.addWidget(self.progress_bar)

        # Estimated Time Label
        self.time_remaining = QLabel("Estimated Time: 00:00")
        self.time_remaining.setStyleSheet(STYLESHEET["sub_label"])
        layout.addWidget(self.time_remaining, alignment=Qt.AlignmentFlag.AlignCenter)

        # Cancel Button
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet(STYLESHEET["charging_button"])
        self.cancel_button.clicked.connect(self.cancel_charging)
        layout.addWidget(self.cancel_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

        # Timer for progress simulation
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000)  # Update every second
        self.seconds_elapsed = 0

    def update_progress(self):
        """Simulate charging progress with time estimate"""
        current_value = self.progress_bar.value()
        if current_value < 100:
            self.progress_bar.setValue(current_value + 5)  # Increase by 5%
            self.seconds_elapsed += 5  # Simulate time elapsed
            remaining_time = max(0, (100 - current_value) * 3)  # Estimated total charge time
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            self.time_remaining.setText(f"Estimated Time: {minutes:02d}:{seconds:02d}")
        else:
            self.charging_label.setText("Charging Complete!")
            self.timer.stop()

    #temporary
    def cancel_charging(self):
        """Handle cancel button click"""
        self.timer.stop()
        self.progress_bar.setValue(0)
        self.charging_label.setText("Charging Canceled")
        self.time_remaining.setText("Estimated Time: --:--")
        # Optionally, return to the main screen
        # self.stacked_widget.setCurrentIndex(PREVIOUS_SCREEN_INDEX)
