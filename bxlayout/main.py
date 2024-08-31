from kivy.app import App
from grdlayout.Custom_Layouts import BgBoxLayout


class Interface(BgBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BlayoutApp(App):
    pass


BlayoutApp().run()
