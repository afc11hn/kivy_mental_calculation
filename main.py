import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'  # opengl error fix for win10
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from random import randint


class Trainer(BoxLayout):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(Trainer, self).__init__(**kwargs)  # init BoxLayout
        self.new_exercise()  # first exercise

    def check(self, textinput):
        try:
            textinput = int(textinput)
        except ValueError:  # when textinput is NaN
            popup = ValueErrorPopup(auto_dismiss=False)
            popup.open()
        if isinstance(textinput, int):  # test if int(textinput) worked
            try:
                solution = eval(self.text)
            except Exception:
                self.text = "Error"

            if solution == textinput:
                self.new_exercise()
            else:
                popup = TAPopup(auto_dismiss=False)
                popup.open()
            self.display.text = ""

    def new_exercise(self):
        n1 = randint(1, 100)
        n2 = randint(1, 100)
        self.text = str(n1) + "+" + str(n2)
        # TODO new and better exercises. e.g. minus, multiply, divide, square, root or n1 + n2 - n3


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
