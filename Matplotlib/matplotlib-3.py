from kivy.utils import platform
from kivy.config import Config

#avoid conflict between mouse provider and touch (very important with touch device)
#no need for android platform
if platform != 'android':
    Config.set('input', 'mouse', 'mouse,disable_on_activity')
else:
    #for android, we remove mouse input to not get extra touch 
    Config.remove_option('input', 'mouse')

from kivy.lang import Builder
from kivy.app import App
import kivy_matplotlib_widget  #register all widgets to kivy register

#generate figure
import matplotlib.pyplot as plt
fig, ax1 = plt.subplots(1, 1)
line1, = ax1.plot([0,1,2,3,4], [1,2,8,9,4],label='line1')
line2, = ax1.plot([2,8,10,15], [15,0,2,4],label='line2')
fig.subplots_adjust(left=0.13,top=0.96,right=0.93,bottom=0.2)

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
            #update axis during pan/zoom
            fast_draw:False
'''


class Test(App):
    lines = []

    def build(self):  
        self.screen=Builder.load_string(KV)
        return self.screen

    def on_start(self, *args):
        self.screen.figure_wgt.figure = fig

        #register lines instance if need to be update
        self.lines.append(line1)
        self.lines.append(line2)

        self.screen.figure_wgt.register_lines(self.lines)

    def set_touch_mode(self,mode):
        self.screen.figure_wgt.touch_mode=mode

    def home(self):
        self.screen.figure_wgt.home()

Test().run()