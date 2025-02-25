from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
import matplotlib.pyplot as plt
import numpy as np
import kivy_matplotlib_widget

KV = """
BoxLayout:
    orientation: 'vertical'
    figure_wgt: figure_wgt
    
    # Top Section - Camera Feed Placeholder
    BoxLayout:
        size_hint_y: 0.3
        Label:
            text: "[Camera Feed]"
            halign: "center"

    # Middle Section - Health Indicators
    BoxLayout:
        size_hint_y: 0.2
        spacing: 10
        padding: 10
        
        BoxLayout:
            Label:
                text: "Heart Rate: 75 BPM"
                halign: "center"
        
        BoxLayout:
            Label:
                text: "HRV: Pending..."
                halign: "center"
        
        BoxLayout:
            Label:
                text: "Respiration Rate: 16 BPM"
                halign: "center"
        
        BoxLayout:
            Label:
                text: "SpO₂: 98%"
                halign: "center"
    
    # Bottom Section - Graphs
    BoxLayout:
        MatplotFigure:
            id:figure_wgt
"""

class HealthMonitorApp(App):
    def build(self):
        self.root = Builder.load_string(KV)
        self.setup_graph()
        return self.root
    
    def setup_graph(self):
        fig, ax = plt.subplots()
        ax.set_title("BVP Signal")
        ax.set_ylim(0, 1)
        self.x_data = np.linspace(0, 10, 100)
        self.y_data = np.random.rand(100)
        self.line, = ax.plot(self.x_data, self.y_data, 'r')
        
        self.root.ids.figure_wgt.figure = fig
        Clock.schedule_interval(self.update_graph, 1)

    def update_graph(self, dt):
        self.y_data = np.roll(self.y_data, -1)
        self.y_data[-1] = np.random.rand()
        self.line.set_ydata(self.y_data)
        # self.root.ids.graph_container.children[0].draw()

if __name__ == "__main__":
    HealthMonitorApp().run()
