from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

KV = """
<MainScreenManager>:
    ScreenOne:
    ScreenTwo:
    ScreenThree:

<ScreenOne>:
    name: "screen_one"
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Welcome to Screen One!"

<ScreenTwo>:
    name: "screen_two"
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Welcome to Screen Two!"

<ScreenThree>:
    name: "screen_three"
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Welcome to Screen Three!"

<NavigationRail>:
    orientation: "vertical"
    size_hint_x: None
    width: "80dp"
    Button:
        text: "Screen 1"
        on_release: app.switch_screen("screen_one")
    Button:
        text: "Screen 2"
        on_release: app.switch_screen("screen_two")
    Button:
        text: "Screen 3"
        on_release: app.switch_screen("screen_three")

BoxLayout:
    orientation: "horizontal"

    NavigationRail:
        id: navigation_rail

    MainScreenManager:
        id: screen_manager
"""

class MainScreenManager(ScreenManager):
    pass

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

class NavigationRail(BoxLayout):
    pass

class NavigationRailApp(App):
    def build(self):
        return Builder.load_string(KV)

    def switch_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name

if __name__ == "__main__":
    NavigationRailApp().run()
