import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt, QTimer

## Crete a tiemr with QTimer
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mouse and Keyboard Event Demo')
        self.setGeometry(100, 100, 400, 300)
        self.label = QLabel("Timer not begins", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000) # 1000 ms = 1 second

    def update_label(self):
        self.label.setText("Updated at: " + str(QTimer.remainingTime(self.timer)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())