from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.widget import Widget


# Task class represents a single task
class Task(BoxLayout):
    text = StringProperty("")
    completed = BooleanProperty(False)

    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 40

        self.checkbox = CheckBox()
        self.checkbox.bind(active=self.on_checkbox_active)

        self.label = Label(text=self.text, size_hint_x=0.8)
        self.remove_button = Button(text="Remove", size_hint_x=0.2, on_press=self.remove_task)

        self.add_widget(self.checkbox)
        self.add_widget(self.label)
        self.add_widget(self.remove_button)

    def on_checkbox_active(self, instance, value):
        """Handle checkbox toggle, marking the task as completed or not."""
        self.completed = value
        if self.completed:
            self.label.color = (0.5, 0.5, 0.5, 1)  # Gray out text when completed
        else:
            self.label.color = (1, 1, 1, 1)  # Restore original color when incomplete

    def remove_task(self, instance):
        """Remove task from the parent layout."""
        self.parent.remove_widget(self)


# Main App class to manage the list of tasks
class TodoApp(App):
    def build(self):
        self.tasks = []

        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.scroll_view = ScrollView(size_hint=(1, None), size=(400, 300))
        self.scroll_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))

        self.scroll_view.add_widget(self.scroll_layout)
        self.root.add_widget(self.scroll_view)

        self.text_input = TextInput(size_hint=(1, None), height=40, multiline=False)
        self.add_button = Button(text="Add Task", size_hint=(1, None), height=50, on_press=self.add_task)
        self.remove_button = Button(text="Remove Completed Tasks", size_hint=(1, None), height=50, on_press=self.remove_completed)

        self.root.add_widget(self.text_input)
        self.root.add_widget(self.add_button)
        self.root.add_widget(self.remove_button)

        return self.root

    def add_task(self, instance):
        """Add a new task to the list."""
        task_text = self.text_input.text
        if task_text:
            task = Task(text=task_text)
            self.scroll_layout.add_widget(task)
            self.text_input.text = ""  # Clear the input field

    def remove_completed(self, instance):
        """Remove all completed tasks."""
        for task in self.scroll_layout.children[:]:
            if isinstance(task, Task) and task.completed:
                self.scroll_layout.remove_widget(task)


if __name__ == "__main__":
    TodoApp().run()
