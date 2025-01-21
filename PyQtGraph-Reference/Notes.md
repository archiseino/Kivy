### Notes:

PyQtGraph makes extensive use of Qt for generating nearly all of its visual output and interfaces. Qt’s documentation is very well written and we encourage all pyqtgraph developers to familiarize themselves with it. The purpose of this section is to provide an introduction to programming with Qt (using either PyQt or PySide) for the pyqtgraph developer.

### QWidgets and Layouts

A Qt GUI is almost always composed of a few basic components:

- A window. This is often provided by QMainWindow, but note that all QWidgets can be displayed in their window by simply calling QWidget.show if the widget does not have a parent.
- Multiple QWidget instances such as QPushButton, QLabel, QComboBox, etc.
- QLayout instances (optional, but strongly encouraged) which automatically manage the positioning of widgets to allow the GUI to resize in a usable way.

### Naming Conventions

When reading the documentation, remember that all of Qt’s classes start with the letter ‘Q’, whereas PyQtGraph’s classes do not. When reading through the methods for any class, it is often helpful to see which Qt base classes are used and look through the Qt documentation as well.

> In most cases, classes which end in Widget are subclassed from QWidget and can therefore be used as a GUI element in a Qt window. Classes which end in Item are subclasses of QGraphicsItem and can only be displayed within a QGraphicsView instance, such as GraphicsLayoutWidget or PlotWidget.

### Signal and Slots

For an overview of Qt’s signal and slots mechanism, check out their signals and slots documentation.

When a Signal is emitted, it triggers either other signals that it is connected to, or a Slot. A slot is a method or stand-alone function that is run when a signal that’s connected to it is emitted.

### GraphicsViews and GraphicsItem

PyQtGraph makes extensive usage of Qt’s Graphics View framework. This documentation should be used as a reference if looking for a basis of PyQtGraph’s inner workings.

### Coordinate Systems and Transformations

More information about the coordinate systems in Qt GraphicsView, read through the Graphics View Coordinate System documentation.

To manipulate the shape and position of QGraphicsItem objects, QTransform objects are applied. Sometimes we need to go “backwards” in a transformation, and while QTransform provides an inverted method, PyQtGraph avoids calling that object due to precision issues involving qFuzzyIsNull. Instead, when PyQtGraph needs to invert a QTransform, it uses invertQTransform() which attempts to preserve the full precision.

It should be noted that many of the Qt GraphicsView methods use QTransform.inverted internally, and there is nothing PyQtGraph can do to avoid those calls.
