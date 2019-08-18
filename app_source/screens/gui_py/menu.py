from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


class GerenciadorTelas(ScreenManager):
    ...


class Menu(App):

    def build(self):
        return GerenciadorTelas()


if __name__ == '__main__':
    Menu().run()
