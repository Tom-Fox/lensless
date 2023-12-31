import PySimpleGUI as sg
import models
import gene
import GPS
import time
import rawPic
import Direction

from PIL import Image, ImageTk, ImageSequence
import tkinter as tk

sg.theme('Black')   # Add a touch of color

#gImgUrl ='D:\OneDrive - The University of Tokyo\projects\lensless\img\\akamon.jpg'
#gImg = gene.getGenePic()

gImg = ''
GifFilename = "img/loading.gif"

reTime = 2023
reStyle = 'pixel'
title = sg.Text(text='TimeMachine', font=('Arial Bold', 30),key='-TITLE-', expand_x=True,justification='center')
chooseBar = sg.Slider(range=(2050,1950), default_value=reTime, resolution=1, orientation='h', key='-SL-')


reset = sg.Button('RESET',key='-RESET-', size=6)
save = sg.Button('OK',key='-OK-', size=6)
back = sg.Button('BACK',key='-BACK-', size=6,visible=False)
loadBar = sg.ProgressBar(100, orientation='h', expand_x=True, size=(20, 20),  key='-PBAR-',visible=False)
#button=Button(text='FloatLayout',size=6)
get_time = reTime
get_style = reStyle
input = models.Input()
#input.gps = '35.710835661046396, 139.7603010534206'
#input.direction = [90.0,90.0] 
img = sg.Image('logo\\span_re.png',key = "-GENEIMG-")
loadNum = sg.Text('20', key='-NUM-', enable_events=True, font=('Arial Bold', 16), justification='center', expand_x=True,visible=False)
#layout
index=[
        [title],
        [sg.Text(text = 'Choose your time',key='-TEXT-')],
        [back],
        [img],
        [loadBar],
        [chooseBar],
        [loadNum],
        [reset, save]
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
                 size=(800,480)
                 )

def getTime():
    return get_time

def getStyle():
    return get_style

def showGIf():

    root = tk.Tk()
    root.geometry("300x300")
    canvas = tk.Canvas(root,width=300, height=300,bg='white')
    canvas.pack()
    im=[]
    im = Image.open('img/loading.gif')
    # GIF图片流的迭代器
    iter = ImageSequence.Iterator(im)
    #frame就是gif的每一帧，转换一下格式就能显示了
    for frame in iter:
        pic=ImageTk.PhotoImage(frame)
        canvas.create_image((100,150), image=pic)
        time.sleep(0.02)
        root.update_idletasks()  #刷新
        root.update()
        root.mainloop()

def ChangePicSize(gImg):
    
    # 打开一个jpg图像文件，注意是当前路径:
    im = Image.open(gImg)
    # 获得图像尺寸:
    w, h = im.size
    print('Original image size: %sx%s' % (w, h))
    # 缩放到50%:
    im.thumbnail((w//2, h//2))
    print('Resize image to: %sx%s' % (w//4, h//4))
    # 把缩放后的图像用jpeg格式保存:
    im.save('image_ai\\akamonn_resize.png', 'png') 
    print('Reset size!')
    return 'image_ai\\akamonn_resize.png'

def step1():
    input.gps = GPS.getGPS()
    input.direction = Direction.getDirection()
    input.pic = rawPic.getRawPic(input.gps, input.direction)

def step2():
    gImg = gene.getGenePic(input.time,input.style)
    print("check this setp tool")
    return gImg

# Event Loop to process "events" and get the "values" of the inputs
while True:

    event, values = window.read(timeout = 10, timeout_key = "-TIMEOUT-") #read of window, two return value:1.event 2.value
 
    if event == "-OK-":
        get_time = int(values['-SL-'])
        
        #print(gImg)
        print('button OK pressed')
        #print(input.getInput())
        window.find_element('-TITLE-').Update(visible=False)
        window.find_element('-TEXT-').Update(visible=False)
        window.find_element('-SL-').Update(visible=False)


        input.style = getStyle()
        input.time = getTime()
        window.find_element('-RESET-').Update(visible=False)
        window.find_element('-OK-').Update(visible=False)
        window.find_element('-BACK-').Update(visible=False)
        window.find_element('-PBAR-').Update(visible=True)
        window.find_element('-NUM-').Update(visible=True)
        for i in range(100):
            window['-PBAR-'].update(current_count=i+1)
            window['-NUM-'].update(f'{i+1}%')
            time.sleep(0.01)  # Adjust this value as needed for your processing time

            if i == 30:  # Start the image generation around halfway
                step1()
            if i == 70:
                gImg = step2()
                time.sleep(0.01)
        
        #if gImg != '':
        print(gImg)
        window.find_element('-BACK-').Update(visible=True)
        window.find_element('-PBAR-').Update(visible=False)
        window.find_element('-NUM-').Update(visible=False)
        window.find_element('-GENEIMG-').Update(visible=True)
        window["-GENEIMG-"].update(ChangePicSize(gImg))
        #window.Refresh()

    if event == "-RESET-":
        window["-SL-"].update(value=reTime)
        print('button RESET pressed')

    if event == "-BACK-":
        #window.find_element('-GENEIMG-').Update(visible=False)
        window["-GENEIMG-"].update('logo\\span_re.png')
        window.find_element('-RESET-').Update(visible=True)
        window.find_element('-OK-').Update(visible=True)
        window.find_element('-TITLE-').Update(visible=True)
        window["-SL-"].update(value=reTime)
        window.find_element('-TEXT-').Update(visible=True)
        window.find_element('-SL-').Update(visible=True)
        
        window.find_element('-BACK-').Update(visible=False)
        #window.Refresh()
        print('button BACK pressed')

    if event==None:
        break

window.close()