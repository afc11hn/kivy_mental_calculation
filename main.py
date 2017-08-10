from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.properties import StringProperty
from random import randint
import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


class Trainer(BoxLayout):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(Trainer, self).__init__(**kwargs)
        self.new_exercise()

    def check(self, input):
        try:
            input = int(input)
        except ValueError:
            popup = ValueErrorPopup(auto_dismiss=False)
            popup.open()
        if isinstance(input, int):
            try:
                solution = eval(self.text)
            except Exception:
                self.text = "Error"

            if solution == input:
                self.new_exercise()
            else:
                popup = TAPopup(auto_dismiss=False)
                popup.open()
            self.display.text = ""

    def new_exercise(self):
        n1 = randint(1, 100)
        n2 = randint(1, 100)
        self.text = str(n1) + "+" + str(n2)

class ValueErrorPopup(Popup):
    pass
class TAPopup(Popup):
    pass

class MathApp(App):
    def build(self):
        self.load_kv("main.kv")
        return Trainer()


if __name__ == "__main__":
    MathApp().run()
