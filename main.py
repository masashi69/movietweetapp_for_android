from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.uix.button import Button
#from kivy.uix.widget import Widget

#class Mainmenu(Screen):
#    pass

#class Postmenu(Screen):
#    pass

#class Getmenu(Screen):
#    pass

class MovieTweet(BoxLayout):

    def pressed(self):
        print('pressed')

    def text_out(self):
        txt = self.ids.input.text
        self.ids.textoutput.text = txt

    pass

class MyApp(App):
    def build(self):
        return MovieTweet()

if __name__ == '__main__':
    MyApp().run()
