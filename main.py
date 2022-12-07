from kivymd.app import MDApp

from uix.screens.baseclass.mainscreen import MainScreen

from kivy.core.window import Window
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (390, 844)


class Plantsility(MDApp):

    def __init__(self, **kwargs):
        super(Plantsility, self).__init__(**kwargs)
        self.mainScreen = MainScreen()

    def build(self):
        return self.mainScreen

    def on_start(self):
        pass


Plantsility().run()
