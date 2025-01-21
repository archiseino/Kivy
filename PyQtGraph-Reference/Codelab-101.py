## Using QtGraph and Qt Designer to create a simple GUI

from PyQt5 import QtWidgets
import pyqtgraph as pg

## Initialize application
app = QtWidgets.QApplication([])

## Define a top-level widget to hold everything
window = QtWidgets.QWidget()
window.setWindowTitle('Simple GUI')

## Create a plot widget
btn = QtWidgets.QPushButton('Press me!')
text = QtWidgets.QLineEdit('Enter some text')
listWidget = QtWidgets.QListWidget()
plot = pg.PlotWidget()

## Create a layout and add widgets size and position
layout = QtWidgets.QGridLayout()
window.setLayout(layout)

## Add widgets to the layout for proper positions
layout.addWidget(btn, 0, 0) # Button goes in upper-left
layout.addWidget(text, 1, 0) # Text box goes in middle-lefft
layout.addWidget(listWidget, 2, 0) # List widget goes in bottom-left
layout.addWidget(plot, 0, 1, 3, 1) # Plot goes on right side, spanning all three rows

## Show the window
window.show()

## Start 'event loop'
app.exec_()

