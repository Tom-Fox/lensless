from kivy.app import App
from kivy.base import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('static/test.kv')
class rootwi(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return rootwi()


if __name__ == '__main__':
    MyApp().run()