from kivy.lang import Builder

import os

from kivymd.uix.bottomnavigation import MDBottomNavigationItem

with open(os.path.join(os.getcwd(), 'uix', 'screens', 'kv', 'scannerscreen.kv'), encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class ScannerScreen(MDBottomNavigationItem):

    def on_enter(self, *args):
        print("CHeck")
