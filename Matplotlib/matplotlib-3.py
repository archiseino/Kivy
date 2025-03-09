from kivy.utils import platform
from kivy.config import Config

# Avoid conflict between mouse provider and touch (very important with touch device)
# No need for android platform
if platform != 'android':
    Config.set('input', 'mouse', 'mouse,disable_on_activity')
else:
    # For android, we remove mouse input to not get extra touch 
    Config.remove_option('input', 'mouse')

from kivy.lang import Builder
from kivy.app import App
from kivy.clock import Clock
import kivy_matplotlib_widget  # Register all widgets to kivy register

# Generate figure
import matplotlib.pyplot as plt
fig, ax1 = plt.subplots(1, 1)
fig.subplots_adjust(left=0.13, top=0.96, right=0.93, bottom=0.2)

KV = '''
Screen
    figure_wgt:figure_wgt
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            size_hint_y:0.2
            Button:
                text:"home"
                on_release:app.home()
            ToggleButton:
                group:'touch_mode'
                state:'down'
                text:"pan" 
                on_press:
                    app.set_touch_mode('pan')
                    self.state='down'
            ToggleButton:
                group:'touch_mode'
                text:"cursor"  
                on_press:
                    app.set_touch_mode('cursor')
                    self.state='down'                
        MatplotFigure:
            id:figure_wgt
            # Update axis during pan/zoom
            fast_draw:False
'''

class Test(App):
    lines = []
    line_index = 0

    def build(self):  
        self.screen = Builder.load_string(KV)
        return self.screen

    def on_start(self, *args):
        self.screen.figure_wgt.figure = fig
        Clock.schedule_interval(self.update_graph, 1)  # Schedule updates every second

    def update_graph(self, dt):
        if self.line_index < 5:
            x = [j for j in range(5)]
            y = [j * (self.line_index + 1) for j in range(5)]
            line, = ax1.plot(x, y, label=f'line{self.line_index + 1}')
            self.lines.append(line)
            self.screen.figure_wgt.register_lines(self.lines)
            self.line_index += 1
            self.screen.figure_wgt.figure.canvas.draw_idle()  # Refresh the figure

    def set_touch_mode(self, mode):
        self.screen.figure_wgt.touch_mode = mode

    def home(self):
        self.screen.figure_wgt.home()

Test().run()