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
''')

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
