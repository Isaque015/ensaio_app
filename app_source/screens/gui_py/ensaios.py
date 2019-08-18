from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

kv = Builder.load_file('ensaios.kv')


class Ensaios(Screen):
    def build(self):
        return kv
