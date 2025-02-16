from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

def apply_glow_effect(widget, color="#1B3A57", blur_radius=50):
    """Applies a glow effect to a given widget."""
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(blur_radius)
    shadow.setColor(QColor(color))
    shadow.setOffset(0, 0)  # No shadow displacement
    widget.setGraphicsEffect(shadow)
