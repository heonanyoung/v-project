#프로그램 세팅
# python -m pip install --upgrade pip wheel setuptools 
# python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
# python -m pip install kivy.deps.gstreamer
# python –m pip install kivy 
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


class PageLayout(PageLayout): #페이지 구분
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            print(filename[0])
        except:
            pass

class Upper_bar(BoxLayout): #상단바
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
