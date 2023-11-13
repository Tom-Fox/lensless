from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle,Color
  
class AnchorLayoutWidget(AnchorLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
  
        with self.canvas:
            # Color(1,1,1,1)
            self.rect=Rectangle(pos=self.pos,size=self.size)
            self.bind(pos=self.update_rect,size=self.update_rect)
  
        #嵌套第一个布局
        anchor_first=AnchorLayout(anchor_x='center',anchor_y='top')
        #添加按钮
        anchor_first.add_widget(Button(text='hello',size_hint=[.3,.2],background_color=[0,1,1,1]))
        anchor_first.add_widget(Button(text='hello1',size_hint=[.3,.2],background_color=[1,0,1,1]))
  
        #嵌套第二个布局
        anchor_second=AnchorLayout(anchor_x='center',anchor_y='bottom')
        #添加按钮
        anchor_second.add_widget(Button(text='RESET',size_hint=[.2,.2]))
        anchor_second.add_widget(Button(text='OK',size_hint=[.4,.1]))
  
        #添加到父布局中
        self.add_widget(anchor_first)
        self.add_widget(anchor_second)
  
    def update_rect(self,*args):
        #设置背景尺寸
        self.rect.pos=self.pos
        self.rect.size=self.size
  
class AnchorApp(App):
    def build(self):
        return AnchorLayoutWidget()
  
if __name__ =='__main__':
    AnchorApp().run()