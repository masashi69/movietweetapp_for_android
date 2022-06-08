from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.uix.button import Button
#from kivy.uix.widget import Widget
from kivy.config import Config

class Mainmenu(Screen):
    def pressed(self):
        print('pressed')

    def text_out(self):
        txt = self.ids.input.text
        self.ids.textoutput.text = txt
    pass

class Postmenu(Screen):
    pass

class Getmenu(Screen):

    pass

class Postmenu_detail(Screen):
    pass

class Getmenu_detail(Screen):

    def gettitle(self):
        with open('movietext.txt', 'r') as f:
            self.text = f.read()
            return self.text

    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('my.kv')

class MyApp(App):
    def build(self):

        return kv

if __name__ == '__main__':
    MyApp().run()
