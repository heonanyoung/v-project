#키비화면쪽 추가부분
<pictureScreen>:
    BoxLayout:
            orientation: 'horizontal'
            Image:
                id: my_image
                source: ""

            FileChooserIconView:
                id : filechooser
                on_selection: my_widget.selected(filechooser.selection)




#파이썬 추가부분
class pictureScreen(Screen):
    #파일 불러오는 작업
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            print(filename[0])
        except:
            pass