## Layouting in PyQt
from qtpy.QtWidgets import QApplication, QPushButton, QVBoxLayout, QGridLayout, QHBoxLayout, QWidget, QLabel 

## Initialize application
app = QApplication([])

## Create a label and button
label = QLabel('Hello, world!')
button = QPushButton('Say hello')

# ## Create a vertical layout
# layout = QVBoxLayout()
# layout.addWidget(label)
# layout.addWidget(button)

## Create a horizontal layout
# layout = QHBoxLayout()
# layout.addWidget(label)
# layout.addWidget(button)

## Create a Grid Layout
# label1 = QLabel('Label 1')
# label2 = QLabel('Label 2')
# label3 = QLabel('Label 3')
# button = QPushButton('Press me!')

# layout = QGridLayout()
# layout.addWidget(label1, 0, 0)
# layout.addWidget(label2, 0, 1)
# layout.addWidget(label3, 1, 0)
# layout.addWidget(button, 1, 1)

## Create a nested layout
## Setup individual widgets
label1 = QLabel('Label 1')
label2 = QLabel('Label 2')
button = QPushButton('Press me!')

## Combine label 2 and button in a horizontal layout
bottom_widget = QWidget()
bottom_layout = QHBoxLayout()
bottom_layout.addWidget(label2)
bottom_layout.addWidget(button)
bottom_widget.setLayout(bottom_layout)

## Combien bottom widget and label 1 in a vertical layout
widget = QWidget()
layout = QVBoxLayout()
layout.addWidget(label1)
layout.addWidget(bottom_widget)
widget.setLayout(layout)

## Create a window and set the layout
window = QWidget()
window.setLayout(layout)
window.show()

## Start 'event loop'
app.exec_()