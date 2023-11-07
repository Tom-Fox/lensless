# main.py
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label # 译者注：这里是从kivy.uix.label包中导入Label控件，这里都注意开头字母要大写

class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.rows = 3
        self.add_widget(Label(text='TIME MACHINE'))


        self.add_widget(Label(text='choose your time'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.add_widget(Button(text='RESET'))
        self.add_widget(Button(text='OK'))

class TimeMachine(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    TimeMachine().run()