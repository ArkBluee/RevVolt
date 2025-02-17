from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor

def apply_glow_effect(widget, color="#008080", blur_radius=200):
    """Applies a static glow effect to a given widget."""
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(blur_radius)
    shadow.setColor(QColor(color))
    shadow.setOffset(0, 0)  # No shadow displacement
    widget.setGraphicsEffect(shadow)

