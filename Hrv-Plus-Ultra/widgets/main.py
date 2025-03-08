from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.uix.switch import Switch
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string('''
<CustomButton>:
    size_hint: None, None
    size: 150, 50
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]
    background_color: 0.2, 0.6, 1, 1
    font_size: '16sp'
    background_normal: ''
    background_down: ''
    on_press: root.on_click()

<OverlayContainer>:
    orientation: 'vertical'
    size_hint: None, None
    size: 300, 200
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.5
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: "Overlay Container"
        size_hint_y: None
        height: 40

<CustomTextInput>:
    size_hint: None, None
    size: 200, 50
    font_size: '16sp'
    multiline: False
    padding: [10, 10]
    background_normal: ''
    background_color: 1, 1, 1, 1
    foreground_color: 0, 0, 0, 1

<RoundedCard>:
    size_hint: None, None
    size: 250, 150
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]

# <IconButton>:
#     size_hint: None, None
#     size: 60, 60
#     background_normal: ''
#     background_color: 0.2, 0.6, 1, 1
#     on_press: root.on_click()
#     Image:
#         source: root.icon
#         center_x: root.center_x
#         center_y: root.center_y

<StatusIndicator>:
    size_hint: None, None
    size: 150, 50
    Label:
        id: status_label
        text: "Status: Normal"
        color: 0, 1, 0, 1

<ProgressBarWidget>:
    size_hint: None, None
    size: 200, 30

<LiveDataLabel>:
    size_hint: None, None
    size: 150, 50
    Label:
        id: data_label
        text: "Data: 0"

<ToggleSwitch>:
    size_hint: None, None
    size: 100, 50
    Switch:
        id: toggle_switch

<GraphContainer>:
    size_hint: None, None
    size: 300, 200
    Label:
        text: "Graph Placeholder"
''')

class CustomButton(Button):
    def __init__(self, text="Jawa", **kwargs):
        super().__init__(text=text, **kwargs)
    
    def on_click(self):
        print(f"{self.text} button clicked!")

class OverlayContainer(BoxLayout):
    pass

class CustomTextInput(TextInput):
    pass

class RoundedCard(BoxLayout):
    pass

from kivy.properties import StringProperty
# class IconButton(Button):
#     icon = StringProperty("")
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
    
#     def on_click(self):
        # print(        f"Icon button with {self.icon} clicked!")

class StatusIndicator(BoxLayout):
    def update_status(self, status):
        color_map = {
            'Normal': (0, 1, 0, 1),
            'Alert': (1, 0.5, 0, 1),
            'Critical': (1, 0, 0, 1)
        }
        self.ids.status_label.text = f"Status: {status}"
        self.ids.status_label.color = color_map.get(status, (1, 1, 1, 1))

class ProgressBarWidget(ProgressBar):
    def update_progress(self, value):
        self.value = value

class LiveDataLabel(BoxLayout):
    def update_data(self, data):
        self.ids.data_label.text = f"Data: {data}"

class ToggleSwitch(Switch):
    def is_active(self):
        return self.active

class GraphContainer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = 0
        # Clock.schedule_interval(self.update_graph, 1)

    # def update_graph(self, dt):
    #     self.counter += 1
    #     self.ids.graph_placeholder.text = f"Graph updated: {self.counter}"
