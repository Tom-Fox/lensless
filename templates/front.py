import PySimpleGUI as sg
import models
import gene
import GPS
import Direction
from PIL import Image

sg.theme('DarkAmber')   # Add a touch of color

time = 2023
title = sg.Text(text='Time machine', font=('Arial Bold', 20),key='-TITLE-', expand_x=True,justification='center')
chooseBar = sg.Slider(range=(2050,1950), default_value=time, resolution=1, orientation='v', key='-SL-')

#gImgUrl ='D:\OneDrive - The University of Tokyo\projects\lensless\img\\akamon.jpg'

#gImg = gene.getGenePic()
gImg = 'img\\akamonn2_720.png'

reset = sg.Button('RESET',key='-RESET-', size=6)
save = sg.Button('OK',key='-OK-', size=6)
back = sg.Button('BACK',key='-BACK-', size=6,visible=False)

get_time = time
input = models.Input()
#input.gps = '35.710835661046396, 139.7603010534206'
#input.direction = [90.0,90.0] 
img = sg.Image(size = (30, 30), key = "-GENEIMG-")
#layout
index=[
        [title],
        [sg.Text(text = 'Choose your time',key='-TEXT-'), chooseBar,img],
        [reset, save,back]
]

layout1 = [
    [sg.VPush()],
    [sg.Push(), sg.Column(index,element_justification='c'), sg.Push()],
    [sg.VPush()]
]

showPage = [
    [title],
    [sg.Text('Choose your time'), img],
    [back]
]
'''
layout2 = [
    [sg.VPush()],
    [sg.Push(), sg.Column(showPage,element_justification='c'), sg.Push()],
    [sg.VPush()]
]
'''

#create a window
#Python GUI: name of window
window=sg.Window('Window Title',layout1,
                 size=(600,250)
                 )

def getTime():
    return get_time

'''
def ChangePage():
    window=sg.Window('Window Title',layout2,
                 size=(600,250)
                 )
    window["-GENEIMG-"].update(gImgUrl)
'''

def ChangePicSize(gImg):
    
    # 打开一个jpg图像文件，注意是当前路径:
    im = Image.open(gImg)
    # 获得图像尺寸:
    w, h = im.size
    print('Original image size: %sx%s' % (w, h))
    # 缩放到50%:
    im.thumbnail((w//4, h//4))
    print('Resize image to: %sx%s' % (w//4, h//4))
    # 把缩放后的图像用jpeg格式保存:
    im.save('img\\akamonn_resize.png', 'png') 
    print('Reset size!')
    return 'img\\akamonn_resize.png'

# Event Loop to process "events" and get the "values" of the inputs
while True:

    event, values = window.read() #read of window, two return value:1.event 2.value
 
    if event == "-OK-":
        get_time = int(values['-SL-'])
        input.time = getTime()
        input.gps = GPS.getGPS()
        input.direction = Direction.getDirection()
        input.pic = rawPic.getRawPic(input.gps, input.direction)
        print(input.gps)
        print('button OK pressed')
        print(input.getInput())
        window.FindElement('-TITLE-').Update(visible=False)
        window.FindElement('-TEXT-').Update(visible=False)
        window.FindElement('-SL-').Update(visible=False)
        window["-GENEIMG-"].update(ChangePicSize(gImg))
        window.FindElement('-GENEIMG-').Update(visible=True)
        window.FindElement('-RESET-').Update(visible=False)
        window.FindElement('-OK-').Update(visible=False)
        window.FindElement('-BACK-').Update(visible=True)

    if event == "-RESET-":
        window["-SL-"].update(value=time)
        print('button RESET pressed')

    if event == "-BACK-":
        window.FindElement('-TITLE-').Update(visible=True)
        window["-SL-"].update(value=time)
        window.FindElement('-TEXT-').Update(visible=True)
        window.FindElement('-SL-').Update(visible=True)
        window.FindElement('-GENEIMG-').Update(visible=False)
        window.FindElement('-RESET-').Update(visible=True)
        window.FindElement('-OK-').Update(visible=True)
        window.FindElement('-BACK-').Update(visible=False)
        
        print('button BACK pressed')

    if event==None:
        break

window.close()