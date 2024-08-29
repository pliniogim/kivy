from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App


class Interface(FloatLayout):
    pass

    # def __init__(self, **kwargs):
    # super().__init__(**kwargs)
    # btn = Button(text="Click me!",
    #              size_hint=(0.5, 0.1),
    #              pos_hint={"center_x": 0.5, "center_y": 0.5})
    # self.label = Label(text="nothing", size_hint=(0.5, 0.1),
    #                    pos_hint={"center_x": 0.5, "center_y": 0.6})
    # self.text_input = TextInput(size_hint=(0.5, 0.1),
    #                             pos_hint={"center_x": 0.5, "center_y": 0.7},
    #                             multiline=False,)
    # self.text_input.bind(on_text_validate=self.display_information)
    # btn.bind(on_press=self.display_information)
    # self.add_widget(self.text_input)
    # self.add_widget(self.label)
    # self.add_widget(btn)

    def display_information(self):
        data = self.ids.textInput.text
        self.ids.label.text = data


class ProjectApp(App):
    pass
    # def build(self):
    #     return Interface()


ProjectApp().run()
