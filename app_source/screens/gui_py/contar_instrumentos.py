from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

kv = Builder.load_file('contar_instrumentos.kv')


class ContarInstrumentosTela(Screen):
    def build(self):
        return kv
