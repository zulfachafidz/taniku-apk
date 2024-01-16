from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Signup(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/signup.kv")
        super().__init__(**kw)