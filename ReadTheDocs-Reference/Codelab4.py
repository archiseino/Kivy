## Dynamically Updating Widgets
from qtpy.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

## Initialize application
app = QApplication([])

## Create label and button
label = QLabel('0')

def say_hello():
    label.setText('Hello, world!')

## Create a button and connect to 'say_hello'
button = QPushButton('Say hello')
button.clicked.connect(say_hello)

## Create layout and add widgets
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

## Apply layout to a window
window = QWidget()
window.setLayout(layout)
window.show()

## Start 'event loop'
app.exec_()
