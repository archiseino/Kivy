from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

class LoginScreen(Screen):
    def do_login(self):
        username = self.ids.username.text
        password = self.ids.password.text
        # Add your login logic here
        if username == "admin" and password == "admin":
            print("Login successful!")
            self.manager.current = "home"
        else:
            print("Invalid username or password")

class HomeScreen(Screen):
    pass

class MainApp(App):
    def build(self):
        # Load the Kv file
        Builder.load_file("login.kv")
        
        # Create the ScreenManager and add the screens
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        
        return sm

    def switch_screen(self, screen_name):
        self.root.current = screen_name

if __name__ == "__main__":
    MainApp().run()