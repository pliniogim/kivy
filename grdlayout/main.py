from kivy.app import App
from Custom_Layouts import BgGridLayout
from Custom_Layouts import BgBoxLayout
from grdlayout.Custom_Layouts import BgAnchorLayout


class Interface4(BgAnchorLayout):
    pass


class Interface3(BgBoxLayout):
    def shuffle(self):
        text_list = list()
        count = 8
        children = self.ids.gridlayout.children
        for child in reversed(children):
            text_list.append(child.text)

        for r in range(3, 0, -1):
            for j in range(r-1, r+2*3, 3):
                children[count].text = text_list[j]
                count -= 1

        print(text_list)


class Interface2(BgBoxLayout):
    pass


class Interface(BgGridLayout):
    pass


class BgGridApp(App):
    pass


BgGridApp().run()
