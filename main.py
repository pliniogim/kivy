from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# prioriza a definição em aplicativo


class Interface(BoxLayout):

    # definindo os elementos dentro da classe
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = Button(text="Clique-me",
                     size_hint=(0.5, 0.5),
                     pos_hint={"center_x": 0.5, "center_y": 0.5},
                     )
        btn.bind(on_press=self.button_press)
        self.add_widget(btn)

    @staticmethod
    def button_press(self):
        print(self.text)
        print(self.size)

    @staticmethod
    def focus():
        print("Focused!")

    @staticmethod
    def printing_message():
        print("Hello clicked!")


class FirstApp(App):

    @staticmethod
    def printing_message():
        print("Hello clicked!")

    def build(self):
        layout = FloatLayout()
        label = Label(text="Este é um label",
                      font_size="32sp",
                      color=(0.5, 0.5, 1, 1),
                      size_hint=(0.3, 0.3),
                      pos=(300, 200)
                      )

        text_input = TextInput(size_hint=(0.3, 0.3), pos=(200, 400))

        layout.add_widget(text_input)
        layout.add_widget(label)

        return layout


FirstApp().run()
