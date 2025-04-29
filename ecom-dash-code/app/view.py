
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.properties import StringProperty

class MainWindow(BoxLayout):
    username = StringProperty("Samuel M")
    avatar = StringProperty("assets/imgs/avatar.jpg")
    def __init__(self, **kw):
        super().__init__(**kw)

class NavTab(ToggleButtonBehavior, BoxLayout):
    text = StringProperty("")
    icon = StringProperty("")
    icon_active = StringProperty("")
    screen_name = StringProperty("scrn_sales")  # Add screen_name property
    def __init__(self, **kw):
        super().__init__(**kw)

    def switch_screen(self, *args):
        # Switch the ScreenManager's current screen to the screen_name
        app = self.get_app()
        if app:
            app.root.ids.scrn_mngr.current = self.screen_name

    def get_app(self):
        from kivy.app import App
        return App.get_running_app()
