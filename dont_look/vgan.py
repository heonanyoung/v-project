#프로그램 세팅
# python -m pip install --upgrade pip wheel setuptools 
# python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
# python -m pip install kivy.deps.gstreamer
# python –m pip install kivy 
from unicodedata import name
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
from kivy.uix.camera import Camera
import time

kivy.require('1.11.1')
fontname = 'NanumBarunGothic.ttf'


class PageLayout(PageLayout): #페이지 구분
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            print(filename[0])
        except:
            pass
    
    def camera_clicked(self):
        camera_screen = ScreenManager()
        camera_screen.add_widget(CameraClick(name='camera'))
        return Camera()


class Upper_bar(BoxLayout): #상단바
    pass

class VeganApp(App): #어플이름
    title = "VEGAN PROJECT"  

    def build(self):
        return PageLayout()

#-------카메라 모듈-------------------------------------
class CameraClick(Screen):
    def capture(self):
        '''
        촬영한 이미지파일은 IMG_촬영일시.png 로 저장.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

class Camera(Screen):
    def build(self):
        return CameraClick()

#--------------------------------------------------------
        
if __name__=='__main__':
    VeganApp().run()


#class MultipleLayout(PageLayout):
#    pass

#class VeganApp(App):
#	def build(self):
#		return MultipleLayout()

#MyApp = VeganApp()

#MyApp.run()
