from kivy.lang import Builder

import os

from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard

with open(os.path.join(os.getcwd(), 'uix', 'screens', 'kv', 'shopscreen.kv'), encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class ShopScreen(MDBottomNavigationItem):

    plants = ["dfasd", "sadsd"]

    def __init__(self, **kwargs):
        super(ShopScreen, self).__init__(**kwargs)
        self.test()

    def test(self):
        print(self.ids)

    def fill_content(self, widget):
        while self.plants:
            self.plants.pop()
            widget.add_widget(Cell())

    def on_enter(self, *args):
        self.fill_content(self.content_body.body)
        print("hello")


class Cell(MDCard):

    pass