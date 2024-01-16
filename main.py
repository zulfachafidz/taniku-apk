
from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.screens import *
from kivy.core.text import LabelBase


class WindowManager(ScreenManager):
    pass


class Backend(MDApp):
    CLASSES = {
        'Welcome': 'screens.welcome'
    }
    AUTORELOADER_PATHS = [
        ('.', {'recursive': True})
    ]
    KV_FILES = [
        'kv/welcome.kv'
    ]

    def build_app(self):
        self.wm = WindowManager()
        screens = [
            Welcome(name="welcome"),
            Login(name="login"),
            Signup(name="signup"),
            HomePage(name="home_page")
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm


if __name__ == '__main__':
    LabelBase.register(
        name="Mpoppins", fn_regular="assets/font/poppins-medium.ttf")
    LabelBase.register(
        name="Bpoppins", fn_regular="assets/font/poppins-semibold.ttf")
    Backend().run()
