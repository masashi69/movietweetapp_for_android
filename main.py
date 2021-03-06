from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.uix.button import Button
#from kivy.uix.widget import Widget
from kivy.config import Config
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import src.gettw

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

    def gettitle(self):
        self.text = ''
        #if self.ids.getyear.text != '':
        #    self.text += self.ids.getyear.text
        if self.ids.getyear.text != '':
            src.gettw.args.year = int(self.ids.getyear.text)

        for movie in src.gettw.main():
            self.text += ' '.join([str(movie['posted_date']), movie['title'], '\n'])

        #with open('movietext.txt', 'r') as f:
        #   self.text = f.read()

        self.ids.movie_o.text = self.text
        return self.ids.movie_o.text

    pass

class Postmenu_detail(Screen):
    pass

class Getmenu_detail(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('my.kv')

class MovieinfoApp(App):
    def build(self):

        return kv

if __name__ == '__main__':
    MovieinfoApp().run()
