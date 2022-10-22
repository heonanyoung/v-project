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

# 어플 레이아웃 -----------------------
Builder.load_string("""
<MainScreen>:
    BoxLayout:
        orientation:'vertical'
        padding: [0,0,0,60]

        Image:
            source: 'veganfood.png'
            size_hint: (1, 0.8)

    BoxLayout:
        orientation:'horizontal'
        Button:
            size_hint: 0.3, 0.1
            font_name: 'NanumBarunGothic.ttf'
            text: '영양성분표 찍기'
            on_press: root.manager.current = 'camera'
        Button:
            size_hint: 0.3, 0.1
            text: 'help'

<CameraScreen>:
    BoxLayout:
        orientation:'vertical'
        padding: [0,0,0,40]

        Camera:
            id: camera
            resolution: (640, 480)
            play: True

    BoxLayout:
        orientation:'horizontal'
        Button:
            size_hint: 0.3, 0.1
            font_name: 'NanumBarunGothic.ttf'
            text: '촬영'
            on_press: root.capture()
        Button:
            size_hint: 0.3, 0.1
            text: 'Back to menu'
            on_press: root.manager.current = 'main'

""")
#-------------------------------------

class MainScreen(Screen):
    pass

class CameraScreen(Screen):
    # 촬영사진 저장 / 촬영한 이미지파일은 IMG_촬영일시.png 로 저장
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
    pass

class VeganApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CameraScreen(name='camera'))
        return sm
   

if __name__ == '__main__':
    VeganApp().run()
