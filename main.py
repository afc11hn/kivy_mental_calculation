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
        self.numbers = []
        self.operator = []
        with open('exercise.txt') as f:
            data = f.readlines()
        for i in range(len(data)):
            line = data[i].replace(" ", "")
            cursor = 0
            temp = []
            temp2 = []
            while cursor != -1:
                cursor = line.find('[')
                cursor2 = line.find(']')
                if cursor2 != -1:
                    temp.append(line[cursor + 1:cursor2].split(','))
                    temp2.append(line[cursor2 + 1:line.find('[', cursor2)])
                line = line[cursor2 + 1:]

            self.numbers.append(temp)
            del temp2[-1]
            self.operator.append(temp2)
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
        rand = []
        line_index = randint(0, len(self.numbers) - 1)
        print(line_index)
        for i in self.numbers[line_index]:
            rand.append(randint(int(i[0]), int(i[1])))
        self.text = str(rand[0])
        for i in range(1, len(rand)):
            self.text += self.operator[line_index][i - 1]
            self.text += str(rand[i])


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
