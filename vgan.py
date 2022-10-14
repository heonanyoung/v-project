import kivy
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Label
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


kivy.require('1.11.1')

fontname = 'NanumBarunGothic.ttf'

class Upper_bar(BoxLayout): #상단바
    pass

class PageLayout(PageLayout):
    pass

class VeganApp(App): #어플이름
    title = "VEGAN PROJECT"
    def build(self):
        return PageLayout()
        
if __name__=='__main__':
    VeganApp().run()


#class MultipleLayout(PageLayout):
#    pass

#class VeganApp(App):
#	def build(self):
#		return MultipleLayout()

#MyApp = VeganApp()

#MyApp.run()