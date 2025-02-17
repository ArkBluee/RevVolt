from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton
from PyQt6.QtCore import Qt, QTimer
from styles.styles import STYLESHEET  

class ChargingStatus(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.charging_label = QLabel("Charging in Progress...")
        self.charging_label.setStyleSheet(STYLESHEET["primary_label"])  # Initial style
        layout.addWidget(self.charging_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.subtext_label = QLabel("Please wait while your e-trike is charging")
        self.subtext_label.setStyleSheet(STYLESHEET["sub_label"])
        layout.addWidget(self.subtext_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet(STYLESHEET["progress_bar"])
        layout.addWidget(self.progress_bar)

        self.time_remaining = QLabel("Estimated Time: 00:00")
        self.time_remaining.setStyleSheet(STYLESHEET["sub_label"])
        layout.addWidget(self.time_remaining, alignment=Qt.AlignmentFlag.AlignCenter)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet(STYLESHEET["back_button"])
        self.cancel_button.clicked.connect(self.cancel_charging)
        layout.addWidget(self.cancel_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000)  # Update every second
        self.seconds_elapsed = 0

    def update_progress(self):
        current_value = self.progress_bar.value()
        if current_value < 100:
            self.progress_bar.setValue(current_value + 5)  # Increase by 5%
            self.seconds_elapsed += 5
            remaining_time = max(0, (100 - current_value) * 3)
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            self.time_remaining.setText(f"Estimated Time: {minutes:02d}:{seconds:02d}")
        else:
            self.charging_label.setText("Charging Complete!")
            self.timer.stop()

    def cancel_charging(self):
        """Handle cancel button click"""
        self.timer.stop()
        self.progress_bar.setValue(0)
        self.charging_label.setText("Charging Canceled")
        self.charging_label.setStyleSheet(STYLESHEET["charging_label_canceled"])  # Red text
        self.time_remaining.setText("Estimated Time: --:--")

        # Option 1: Return to the previous screen (if you know the index)
        # self.stacked_widget.setCurrentIndex(0)  # Example: Go back to index 0

        # Option 2:  Return to a specific screen by its instance (more robust)
        # Assuming you have a reference to the previous screen (e.g., in main.py)
        # self.stacked_widget.setCurrentWidget(self.previous_screen) # If you have self.previous_screen

        # Option 3: Emit a signal to notify the parent/main window to switch screens
        # This is the most flexible approach
        # if hasattr(self, "canceled"): # Check if the signal is connected
        #     self.canceled.emit() # Emit the signal