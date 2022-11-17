import kivy
import io
kivy.require('2.1.0')

from kivy.core.image import Image as CoreImage
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.graphics import *
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window

from kivy.clock import Clock

import config as conf
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Vi importere alle de bibliotekerne ind og bruger kivy's funktioner

class Background(Widget):# Vi definere en klasse som hedder background som en widget
    def __init__(self, **kwargs): #
        super().__init__(**kwargs)
        with self.canvas.before:
                    Rectangle(source='./billeder/test2.jpg', pos=(0 ,0), size=Window.size)

class FrontPageScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background = Background()


        self.minlabel = Label(text = 'FitNow', size_hint_y= None, font_size='35sp')

        self.knapper = GridLayout(rows=3, size_hint_x=None,size_hint_y=None, width=conf.sc_button_width,height=conf.height-self.minlabel.height)

        self.knap1 = Button(text="Udholdenhedstræning", size_hint_x= None, size_hint_y = None, height=conf.sc_button_height, width=conf.sc_button_width)


        # self.bind(on_press=)
        self.knap2 = Button(text="Styrketræning", size_hint_x= None, size_hint_y = None, height=conf.sc_button_height, width=conf.sc_button_width)
        self.knap3 = Button(text="Yoga", size_hint_x= None, size_hint_y = None, height=conf.sc_button_height, width=conf.sc_button_width)

        self.knapper.add_widget(self.knap1)
        self.knapper.add_widget(self.knap2)
        self.knapper.add_widget(self.knap3)

        self.knapper_centrer = AnchorLayout(anchor_x="center", anchor_y="bottom", size_hint_x=None, size_hint_y=None, height=conf.height, width=conf.width)
        self.knapper_centrer.add_widget(self.knapper)

        # add label and buttons together
        self.main = GridLayout(rows=2, size_hint_x=None, size_hint_y=None, height=conf.height, width=conf.width)
        self.main.add_widget(self.minlabel)
        self.main.add_widget(self.knapper_centrer)

        self.main_centrer = AnchorLayout(anchor_x="center", anchor_y="top")
        self.main_centrer.add_widget(self.background)
        self.main_centrer.add_widget(self.main)


        self.final = BoxLayout(size_hint_x=None,size_hint_y=None, height=conf.height, width=conf.width)

        self.final.add_widget(self.main_centrer)

    def drawIcons(self):
        """self.knap1.canvas.clear()
        with self.knap1.canvas:
            print(self.knap1.pos)
            self.knap1.canvas.add(Rectangle(source='./billeder/test.jpg', pos=(0,0), size=(conf.sc_button_icon_w, conf.sc_button_icon_w)))"""

    def render(self):
        self.drawIcons()

    def update(self, dt):
        self.render()


class TestScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="worked"))

    def update(self,dt):
        self.add_widget(Label(text="s"))
class MyApp(App):
    def build(self):
        Window.size = (conf.width, conf.height)
        sm =ScreenManager()
        sm.add_widget(FrontPageScreen(name="Start"))
        sm.add_widget(TestScreen(name="Slut"))

        #event = Clock.schedule_interval(sm, 1 / 30.)
        return sm


if __name__ == '__main__':
    MyApp().run()
