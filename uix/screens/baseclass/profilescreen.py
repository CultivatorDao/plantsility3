from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFlatButton
import requests

import os

from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout

with open(os.path.join(os.getcwd(), 'uix', 'screens', 'kv', 'profilescreen.kv'), encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class ProfileScreen(MDBottomNavigationItem):

    body = ObjectProperty()

    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        self.test()

    def test(self):
        # canvas = MDBoxLayout()
        # for i in range(4):
        #     name = MDLabel(text="sos")
        #     content = MDLabel(text="sass")
        #     canvas.add_widget(name)
        #     canvas.add_widget(content)
        # self.add_widget(canvas)
        print(self.children)


class InfoLine(MDBoxLayout):

    def change_content(self):
        pass


class LightButton(MDFlatButton):

    def light_on(self):
        url = "http:/192.168.4.1:80/light"
        try:
            requests.get(url)
        except Exception:
            print("error")
