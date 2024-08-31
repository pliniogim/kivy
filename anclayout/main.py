from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from Custom_Layouts import BgAnchorLayout
from anclayout.Custom_Layouts import BgBoxLayout


class Interface2(BgBoxLayout):
    pass


class Interface(BgAnchorLayout):
    pass


class BgAnchorApp(App):
    pass


BgAnchorApp().run()
