import cv2
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

KV = """
<MainScreenManager>:
    CameraScreen:
    ScreenTwo:
    ScreenThree:

<CameraScreen>:
    name: "screen_one"
    BoxLayout:
        orientation: "vertical"
        Image:
            id: camera_feed
        Button:
            text: "Start Camera"
            on_press: root.start_camera()

<ScreenTwo>:
    name: "screen_two"
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "This is Screen Two!"
        Button:
            text: "Go to Screen Three"
            on_release: app.switch_screen("screen_three")

<ScreenThree>:
    name: "screen_three"
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "This is Screen Three!"
        Button:
            text: "Go to Screen One"
            on_release: app.switch_screen("screen_one")

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

class CameraScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.capture = None
        self.image_widget = None

    def start_camera(self):
        if self.capture is None:
            self.capture = cv2.VideoCapture(0)  # Open default camera
            Clock.schedule_interval(self.update, 1.0 / 30.0)  # Update at 30 FPS

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Convert frame to texture for display
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            buf = frame.tobytes()
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            image_texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
            self.ids.camera_feed.texture = image_texture

    def on_leave(self):
        # Release the camera and unschedule the Clock event when leaving the screen
        if self.capture:
            self.capture.release()
            self.capture = None
        Clock.unschedule(self.update)  # Stop the update method from being called
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
