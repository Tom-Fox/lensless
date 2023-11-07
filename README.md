对于一个web项目，往往我们会遵循 mvc:
model [模型，当用户在页面上点击了一个按钮，控制器通过模型将数据存入对应的数据库]
view [视图，展示的页面]
controller [控制器，如果用户点击了视图中的按钮，那么就相当于触发了一个事件，就会通过控制器，系统就需要决定把这个事件交给谁去处理]

对于Python的项目，我们会遵循 mtv:
model [模型]
template [模板，比如网页，html]
view [视图，类
似于web的控制器，起控制作用，里面写的就是我们的python代码]

移植环境：
pip install -r requirements.txt

在输入模块这部分，我们也遵循了同样的思路。输入模块，是一段代码，用于针对各种输入设备提供支持，比如苹果公司的Trackpad触摸板，TUIO多点触摸设备，或者是鼠标模拟器等等。如果你需要对某一种新的输入设备添加支持，只需要提供一个新的类，用这个类来读取输入设备的数据，然后传递给Kivy基本事件，就可以了。