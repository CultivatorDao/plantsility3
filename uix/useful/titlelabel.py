import os

from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.uix.label import MDLabel

with open(os.path.join(os.getcwd(), "uix", "screens", "kv", "useful_kv", "titlelabel.kv"), encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class TitleLabel(MDLabel):
    pass
