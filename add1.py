#키비 화면 서식 추가
<PictureScreen>:
    id: my_widget
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'

            Image:
                id: my_image
                source: ""

            FileChooserIconView:
                id : filechooser
                on_selection: my_widget.selected(filechooser.selection)
        Button:
            size_hint: 0.3, 0.1
            text: 'Back to menu'
            on_press: root.manager.current = 'main'


class PictureScreen(Screen):
    #파일 불러오는 작업
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            print(filename[0])
        except:
            pass
        