# 카메라 모듈 구현

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

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
import time

Builder.load_string('''
<PageLayout>:
    BoxLayout: #첫번째 페이지
        orientation:'vertical'
    
        Upper_bar:
            size_hint: (1, 0.1)
            canvas.before:
                Color:
                    rgba: 98 / 255, 255 / 255, 114 / 255, 1

                Rectangle:
                    pos: self.pos
                    size: self.size

        Image:
            source: 'veganfood.png'
            size_hint: (1, 0.8)
            #size: self.texture_size
        
        BoxLayout:
            orientation:'horizontal'
            size_hint: (1, 0.3)
            Label:
                font_name: 'NanumBarunGothic.ttf'
                text:
                    '<< 화면을 옆으로 넘겨보세요'

        BoxLayout:
            orientation:'horizontal'
            padding: [30, 20]
            size_hint: (1, 0.2)

            Button:
                text: 'Help'
                size_hint:(0.2, 1)
                on_press: Factory.HelpPop().open()
        
    BoxLayout: #두번째 페이지
        orientation: 'vertical'

        canvas:
            Color: 
                rgba: 0, 0, 0, 1
            Rectangle:
                pos: self.pos
                size: self.size

        Upper_bar:
            size_hint: (1, 0.1)
            canvas.before:
                Color:
                    rgba: 98 / 255, 255 / 255, 114 / 255, 1

                Rectangle:
                    pos: self.pos
                    size: self.size
        
        BoxLayout:
            size_hint: (1, 0.8)
            Label:
                text: 'Vegan'
                color : 1, 1, 0, 1
                
        BoxLayout:
            orientation: 'horizontal'
            padding: [50, 20]
            size_hint: (1, 0.2)
            
            Button:
                size_hint: (0.3, 1)
                text:'reset'


            Button:
                size_hint: (0.3, 1)
                text: 'search'
        
#-------------------------------------------------------
<Upper_bar>:
    BoxLayout:

       

<HelpPop@Popup>:
    size_hint: 1, 1
    title: 'Help'
    auto_dismiss: False #팝업창 외부를 선택해도 창이 닫히지 않음
    BoxLayout:
        orientation:'vertical'
        Label:
            font_name: 'NanumBarunGothic.ttf'
            text:
                '비건 프로젝트에 오신걸 환영합니다. \n위 프로그램은 사용자가 원하는 제품의 비건유무를 판별합니다.'
        Button:
            text:'Close'
            on_press:
                root.dismiss()
            size_hint_y : None
            height: '40dp'
            
<MadePop@Popup>:
    size_hint: 1, 1
    title: 'Made'
    auto_dismiss: False #팝업창 외부를 선택해도 창이 닫히지 않음
    BoxLayout:
        orientation:'vertical'
        Label:
            text:
                'made by hanyang~~~'
        Button:
            text:'Close'
            on_press:
                root.dismiss()
            size_hint_y : None
            height: '40dp'

<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        font_name: 'NanumBarunGothic.ttf'
        text: '사진찍기'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        font_name: 'NanumBarunGothic.ttf'
        text: '촬영'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()

<PageLayout>:
    BoxLayout: #첫번째 페이지
        orientation:'vertical'
    
        Upper_bar:
            size_hint: (1, 0.1)
            canvas.before:
                Color:
                    rgba: 98 / 255, 255 / 255, 114 / 255, 1

                Rectangle:
                    pos: self.pos
                    size: self.size

        Image:
            source: 'veganfood.png'
            size_hint: (1, 0.8)
            #size: self.texture_size
        
        BoxLayout:
            orientation:'horizontal'
            size_hint: (1, 0.3)
            Label:
                font_name: 'NanumBarunGothic.ttf'
                text:
                    '<< 화면을 옆으로 넘겨보세요'

        BoxLayout:
            orientation:'horizontal'
            padding: [30, 20]
            size_hint: (1, 0.2)

            Button:
                font_name: 'NanumBarunGothic.ttf'
                text: '촬영'
                size_hint_y: None
                height: '48dp'

            Button:
                text: 'Help'
                size_hint:(0.2, 1)
                on_press: Factory.HelpPop().open()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        촬영한 이미지파일은 IMG_촬영일시.png 로 저장.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class Camera(App):

    def build(self):
        return CameraClick()

class VeganApp(App): #어플이름
    title = "VEGAN PROJECT"
    def build(self):
        return PageLayout()

VeganApp().run()

'''---------------------------------------------------------------------'''
