from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2


class KivyCVApp(App):
    def build(self):
        # Create an Image widget for displaying video frames
        self.img_widget = Image()
        # Open the default webcam
        self.capture = cv2.VideoCapture(0)
        # Schedule the frame update
        Clock.schedule_interval(self.update_frame, 1.0 / 30.0)  # 30 FPS
        return self.img_widget

    def update_frame(self, dt):
        # Capture a frame from the webcam
        ret, frame = self.capture.read()
        if ret:
            # Convert the frame from BGR (OpenCV format) to RGB (Kivy format)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Get the frame dimensions
            h, w, _ = frame.shape
            # Create a texture to display the frame
            texture = Texture.create(size=(w, h), colorfmt="rgb")
            # Flip the texture (to fix mirroring)
            texture.blit_buffer(frame.tobytes(), colorfmt="rgb", bufferfmt="ubyte")
            texture.flip_vertical()
            # Set the texture of the Image widget
            self.img_widget.texture = texture

    def on_stop(self):
        # Release the webcam when the app is closed
        self.capture.release()


if __name__ == "__main__":
    KivyCVApp().run()
