import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen, QFont

class SemicircleGauge(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = 50
        self._max = 100

    def setValue(self, value):
        self._value = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.rect()
        size = min(rect.width(), rect.height())
        radius = size / 2 - 10

        # Draw background semicircle
        painter.setBrush(Qt.NoBrush)
        painter.setPen(QPen(QColor(224, 224, 224), 10))
        painter.drawArc(rect.center().x() - radius, rect.center().y() - radius, radius * 2, radius * 2, 180 * 16, -180 * 16)

        # Determine color based on value
        if self._value < 33:
            color = QColor(0, 255, 0)  # Green
        elif self._value < 66:
            color = QColor(255, 255, 0)  # Yellow
        else:
            color = QColor(255, 0, 0)  # Red

        # Draw progress arc
        painter.setPen(QPen(color, 10))
        span_angle = int(180 * (self._value / self._max)) * 16
        painter.drawArc(rect.center().x() - radius, rect.center().y() - radius, radius * 2, radius * 2, 180 * 16, -span_angle)

        # Draw text
        painter.setPen(QPen(QColor(0, 0, 0), 2))
        painter.setFont(QFont("Arial", 16, QFont.Bold))
        text = f"{self._value} kg"
        text_rect = painter.fontMetrics().boundingRect(text)
        text_rect.moveCenter(rect.center())
        painter.drawText(text_rect, Qt.AlignCenter, text)

        painter.end()

class WeightGauge(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Create and add the semicircle gauge
        self.gauge = SemicircleGauge(self)
        layout.addWidget(self.gauge)

        # Create and add the label
        self.label = QLabel("HI Your Weight is - XXXX", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setWindowTitle('Weight Gauge')
        self.resize(300, 300)

        # Set background color
        self.setStyleSheet("QWidget {background-color: orange;}")  # Light cyan background

        # Simulate updating the weight every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateWeight)
        self.timer.start(1000)

    def updateWeight(self):
        # Generate a random weight for demonstration purposes
        import random
        weight = random.randint(0, 100)

        # Update the label and the gauge
        self.label.setText(f"HI Your Weight is - {weight}")
        self.gauge.setValue(weight)

    def keyPressEvent(self, event):
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeightGauge()
    ex.showFullScreen()  # Make the window full screen
    sys.exit(app.exec_())
