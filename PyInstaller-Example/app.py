# main.py
from kivy.app import App
from kivy.uix.label import Label
from multiprocessing import Process, freeze_support

class MyApp(App):
    def build(self):
        return Label(text='Hello Kivy!')

if __name__ == '__main__':
    freeze_support()
    MyApp().run()