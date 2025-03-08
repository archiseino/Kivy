from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
import kivy.properties as props

kv = """
<ShadowBox>:
    BoxLayout:
        id: main
        orientation: root.orientation
        canvas.before:
            Color:
                rgba: root.bcolor
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: root.radius

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

<GraphContainer>:
    size_hint: None, None
    size: 300, 200
    Label:
        text: "Graph Placeholder"
"""

Builder.load_string(kv)

class RoundedCard(BoxLayout):
    pass

class ShadowBox(ButtonBehavior, BoxLayout):
    radius = props.ListProperty([1])
    bcolor = props.ColorProperty([1,1,1,1])

    def __init__(self, *args, **kwargs):
        super(ShadowBox, self).__init__(*args, **kwargs)

    def on_padding(self, inst, value):
        self.padding = 0
        self.ids.main.padding = value

    def on_spacing(self, inst, value):
        self.spacing = 0
        self.ids.main.spacing = value

    def add_widget(self, widget, index=0):
        if len(self.children) == 0:
            super().add_widget(widget, index=index)
        else:
            self.ids.main.add_widget(widget, index=index)

    def remove_widget(self, widget):
        self.ids.main.remove_widget(widget)

    def clear_widgets(self):
        self.ids.main.clear_widgets()

class OverlayContainer(BoxLayout):
    pass

class GraphContainer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = 0
        # Clock.schedule_interval(self.update_graph, 1)

    # def update_graph(self, dt):
    #     self.counter += 1
    #     self.ids.graph_placeholder.text = f"Graph updated: {self.counter}"
