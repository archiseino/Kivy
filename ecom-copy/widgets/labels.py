from kivy.lang import Builder
from kivy.uix.label import Label

Builder.load_string("""
<Text>:
    text_size: self.size
    valign: "middle"
    font_name: app.fonts.subheading # Font name
    shorten_from: "right" # Shorten the text from the right
    shorten: True # Shorten the text
    color: [0,0,0, 1] # Color of the text
    markup: True # Markup is a text formatting language that Kivy uses to format text                    
""")

class Text(Label):
    def __init__(self, **kw):
        super().__init__(**kw)