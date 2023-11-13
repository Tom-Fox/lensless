from kivy.app import App   #导入kivy的app类，它是所有kivy应用的基类
from kivy.uix.button import Button #引入控件
from kivy.uix.floatlayout import FloatLayout  #引入布局
from kivy.graphics import Rectangle,Color
  
class FloatLayoutApp(App):  #继承app类
    def build(self):  #实现app类的build（）方法
        def update_rect(layout,*args):
            #设置背景尺寸，可忽略
            layout.rect.pos=layout.pos
            layout.rect.size=layout.size
  
        float_layout=FloatLayout()
  
        #设置背景颜色（可忽略）
        with float_layout.canvas:
            Color(1,1,1,1)
            float_layout.rect=Rectangle(pos=float_layout.pos,size=float_layout.size)
            float_layout.bind(pos=update_rect,size=update_rect)
  
        #在布局内的【300，200】处添加一个尺寸为0.3，0.2的按钮
        button=Button(text='FloatLayout',size_hint=(.3,.2),pos=(0,0))
        #这里的pos参数不会因窗口改变而改变位置，这个是固定位置，要随窗口变化而动态变化的要用pos_hint
  
        #将按钮添加到布局内
        float_layout.add_widget(button)
        #返回布局
        return float_layout
  
if __name__=='__main__':  #程序入口
        FloatLayoutApp().run() #启动应用程序