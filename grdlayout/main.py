from kivy.app import App
from Custom_Layouts import BgGridLayout
from Custom_Layouts import BgBoxLayout


class Interface3(BgBoxLayout):
    def shuffle(self):
        print("shuffling")


class Interface2(BgBoxLayout):
    pass


class Interface(BgGridLayout):
    pass


class BgGridApp(App):
    pass


BgGridApp().run()
