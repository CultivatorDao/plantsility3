from kivy.lang import Builder

import os

from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.card import MDCard

with open(os.path.join(os.getcwd(), 'uix', 'screens', 'kv', 'homescreen.kv'), encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class HomeScreen(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.displayed = []  # for mapping plants
        self.plants = []    # all plants
        # add lists for other categories

    def fill_content(self):

        contentbox = Square()
        for name in self.plants:
            contentbox.content.name.text = name
            self.mainwidget.content.content.scrollbody.content.add_widget(contentbox)

    def on_enter(self, *args):
        self.fill_content()


class SortBar(MDBoxLayout):

    def reset_buttons(self):
        self.rec_icon.change_color()
        self.off_icon.change_color()
        self.in_icon.change_color()
        self.out_icon.change_color()
        self.exo_icon.change_color()
        print(self.rec_icon.text)

    def check(self):
        print("Check parent")


class SortIcon(MDFillRoundFlatIconButton):
    states = {"Recommend": True,
              "Office": False,
              "Indoor": False,
              "Outdoor": False,
              "Exotic": False}

    def change_color(self):
        self.md_bg_color = (230/255, 255/255, 214/255, 1)
        self.text_color = "black"

    def set_active(self):
        self.md_bg_color = (116/255, 197/255, 144/255, 1)
        self.text_color = "white"

    def check(self):
        # self.states = self.states.fromkeys(self.states, False)
        # self.states[self.name] = True
        # return self.states
        print('check')


class Square(MDCard):

    pass