## Docs

## Kivy Lifecycle

It consist of some things

- `__init__`, your app needs to inherit the App class, and setup some variables and properties
- `build()` create the UI (root widget) return widget
- `on_start()` called after build, to setup event listener, animation and background tasks
- `on_pause()`
- `on_resume()`
- `on_stop()`

## Kivy Best Practices Project Structure

Kivy follows the MVC pattern achitecture.

```yaml
my_kivy_app/          # Root project directory
│── main.py           # Entry point of the application
│── myapp.kv          # KV file (UI structure)
│── assets/           # Assets (images, sounds, fonts)
│   ├── images/
│   ├── sounds/
│   ├── fonts/
│── modules/          # Additional modules (optional)
│   ├── screens.py    # Screen management
│   ├── widgets.py    # Custom widgets
│── models/           # Data models (optional)
│   ├── data.py       # Data processing
│── controllers/      # Business logic (optional)
│   ├── events.py     # Event handling
│── README.md         # Documentation
│── requirements.txt  # Dependencies (if any)
```

## How to load KV

There are two ways to load Kv code into your application:

- By name convention:

Kivy looks for a Kv file with the same name as your App class in lowercase, minus `App`f it ends with ‘App’ e.g:

```
MyApp -> my.kv
```

If this file defines a Root Widget it will be attached to the App’s root attribute and used as the base of the application widget tree.

- Builder: You can tell Kivy to directly load a string or a file. If this string or file defines a root widget, it will be returned by the method:

```python
from kivy.lang import Builder

Builder.load_file('path/to/file.kv')
```

or:

```python
Builder.load_string(kv_string)
```

So basically, Kivy is consist of Widget and the Layout is also considered Widgets.

## Rule Context

For creating the file `py` and `kv`, there are two rules that I must to follow

- Root Rule (No bracket <>, must explicitly defined at the top of the Kv files, access using `app` keyword)
- Class Rule (With bracker, can use the `root` keyword to access the logic in python files)

Root rule is something that isn't defined in the python (implicitly defined in kv), it's been handled to the Kv, so we don't need to create the class and return it

```python
class MyApp(App):
    def build(self):
        return Builder.load_file("myapp.kv")

MyApp().run()

---

BoxLayout:  # Root Rule (No `< >`)
    orientation: "vertical"

    Label:
        text: "Hello, Kivy!"

    Button:
        text: "Click Me"
```

Class rule on the other hand use bracket and can be inside either custom widget / layout. it can uses the `root` to access the methods. Oh ya, it also needs to inherit from the `Widget` class. and instantiated manually

```python
class CustomBox(BoxLayout):  # Must instantiate in Python
    pass

class MyApp(App):
    def build(self):
        return CustomBox()  # Needs explicit instantiation

MyApp().run()
```

Example of using Custom class rule inside a main container.

```python
# Custom widget class (linked to `<CustomBox>` rule in KV)
class CustomBox(BoxLayout):
    def update_label(self):
        """Updates the label text when the button is pressed."""
        self.ids.custom_label.text = "Updated by root!"

---

# 🔹 Class Rule: Custom widget definition
<CustomBox>:
    orientation: "vertical"
    padding: 10
    spacing: 10

    Label:
        id: custom_label
        text: "Original Text"  # This label will be updated using `root`

    Button:
        text: "Update Label (root)"
        on_release: root.update_label()  # Calls the method in `CustomBox`
```

## Sample Code

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Define a Custom Layout that inherits from BoxLayout
class CustomBox(BoxLayout):
    def update_label(self):
        """Updates the label text when the button is clicked."""
        self.ids.custom_label.text = "Updated by root!"

class MyApp(App):
    global_text = "Hello from App!"

    def change_global_text(self):
        """Updates the global label text."""
        self.root.ids.global_label.text = "Updated by app!"

    def build(self):
        return Builder.load_file("myapp.kv")

MyApp().run()
```

```kivy
# 🔹 Class Rule: Custom layout with a button that updates the label
<CustomBox>:
    orientation: "vertical"
    padding: 10
    spacing: 10

    Label:
        id: custom_label
        text: "Original Text"

    BoxLayout:  # Sub-child layout
        orientation: "horizontal"
        Button:
            text: "Update (root)"
            on_release: root.update_label()  # Calls function in `CustomBox`
        Button:
            text: "Access Global (app)"
            on_release: app.change_global_text()  # Calls function in `MyApp`

# 🔹 Root Rule: Defines the main UI structure
BoxLayout:
    orientation: "vertical"
    padding: 20
    spacing: 10

    Label:
        id: global_label
        text: app.global_text  # Accessing a variable from `MyApp`

    Button:
        text: "Update Global Label (app)"
        on_release: app.change_global_text()  # Calls a global function in `MyApp`

    CustomBox:  # Custom widget instance
```

## Event and Properties

In Kivy, events are how widgets communicate and respond to user interactions (e.g., button clicks, text input, touch gestures). Event binding is the mechanism that links an event (like on_press) to a function that handles the event.

- Types of event
- Touch Event (on_touch_down, on_touch_up, on_pressed)
- Widget-based event (button for on_press, on_release)
- Custom event for Custom Widget

For properties, you can use setter / getter mechanism out of that.

```python
<MyWidget>:
    my_text: "Hello, Kivy!"
    Label:
        text: my_text  # Automatically updates when `my_text` changes

---

## Modify in the Python
self.my_text = "New text!"  # Updates UI instantly
```

You can use the `self` keyword to update the value in kv files.

```python
class MyWidget(BoxLayout):
    my_button = ObjectProperty()  # Default: None

    def change_text(self):
        if self.my_button:
            self.my_button.text = "Clicked!"  # Updates Button text

---

<MyWidget>:
    my_button: my_btn  # Reference from KV

    Button:
        id: my_btn  # Linked to my_button
        text: "Press Me"
        on_press: root.change_text()
```

## Graphics

In Kivy, it uses the OpenGL and Canvas API to render.

Every widget has a canvas, where you can draw primitives (like rectangles, lines, images, etc.).

Kivy has 3 main canvas sections:

- canvas.before → Executes before the widget’s main rendering.
- canvas → Executes during normal rendering (default).
- canvas.after → Executes after the widget’s rendering (on top).

✅ Use canvas.before for backgrounds.
✅ Use canvas.after for overlays / effects.
✅ Use self.canvas in Python for dynamic shapes.

🔹 Graphics Instructions in Kivy
Kivy's graphics system is divided into two types of instructions:

- Context Instructions → Modify the rendering state (e.g., color, transformation).
- Vertex Instructions → Define what gets drawn (e.g., rectangles, lines, shapes).

![alt text](assets\image-context-instruction.png)

```
<MyWidget>:
    canvas:
        Color:
            rgba: 1, 0, 0, 1  # Red color
        Rotate:
            angle: 45
            origin: self.center
```

![alt text](assets\image-vertex-instruction.png)

```
<MyWidget>:
    canvas:
        Color:
            rgba: 1, 0, 0, 1  # Red
        Rotate:
            angle: 30
            origin: self.center
        Rectangle:
            pos: self.pos
            size: self.size
```

## FAQ

- RoundedEdges on Button
  This is a tricky one. As far as I am concern Widgets are always rectangles. But we can change the background and put a couple of images for the normal and down states using the background_normal and background_down properties respectively. Also you will need to understand the border property.
- Yes, that's correct. In Kivy, when you set parameters in the KV file, they are used to set the properties of the widget, not to pass arguments to the **init** function. The properties defined in the class (such as StringProperty, NumericProperty, etc.) are automatically managed by Kivy's property system.
- When you set a property in the KV file, Kivy automatically updates the corresponding property in the class instance. This means that the parameters in the KV file are used to set the properties, not to pass arguments to the **init** function.
