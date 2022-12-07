import os

from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.list import OneLineListItem
from kivy.properties import ObjectProperty

from uix.screens.baseclass.homescreen import HomeScreen
from uix.screens.baseclass.scannerscreen import ScannerScreen
from uix.screens.baseclass.shopscreen import ShopScreen
from uix.screens.baseclass.profilescreen import ProfileScreen


with open(os.path.join(os.getcwd(), "uix", "screens", "kv", "mainscreen.kv"), encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class MainScreen(MDBottomNavigation):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.homeScreen = HomeScreen()
        self.scannerScreen = ScannerScreen()
        self.shopScreen = ShopScreen()
        self.profileScreen = ProfileScreen()

    def initialize(self):
        print("check")
