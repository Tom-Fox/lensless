import PySimpleGUI as sg
import models
import gene
import GPS
import time
import rawPic
import Direction

# from PIL import Image, ImageTk, ImageSequence
# import tkinter as tk
# from kivy.uix.button import Button #引入控件

# sg.theme('DarkAmber')   # Add a touch of color

# #gImgUrl ='D:\OneDrive - The University of Tokyo\projects\lensless\img\\akamon.jpg'
# #gImg = gene.getGenePic()
# gImg = ''
# GifFilename = "img/loading.gif"

# reTime = 2023
# reStyle = 'pixel'
# title = sg.Text(text='Time machine', font=('Arial Bold', 20),key='-TITLE-', expand_x=True,justification='center')
# chooseBar = sg.Slider(range=(2050,1950), default_value=reTime, resolution=1, orientation='v', key='-SL-')


# reset = sg.Button('RESET',key='-RESET-', size=6)
# save = sg.Button('OK',key='-OK-', size=6)
# back = sg.Button('BACK',key='-BACK-', size=6,visible=False)
# loadBar = sg.ProgressBar(21, orientation='h', expand_x=True, size=(20, 20),  key='-PBAR-',visible=False)
# #button=Button(text='FloatLayout',size=6)
# get_time = reTime
# get_style = reStyle
# input = models.Input()
# #input.gps = '35.710835661046396, 139.7603010534206'
# #input.direction = [90.0,90.0] 
# img = sg.Image(size = (30, 30), key = "-GENEIMG-",visible=False)
# loadNum = sg.Text('20', key='-NUM-', enable_events=True, font=('Arial Bold', 16), justification='center', expand_x=True,visible=False)
# #layout
# index=[
#         [title],
#         [sg.Text(text = 'Choose your time',key='-TEXT-'), chooseBar, loadBar, img],
#         #[button],
#         [loadNum, reset, save,back]
# ]

# layout1 = [
#     [sg.VPush()],
#     [sg.Push(), sg.Column(index,element_justification='c'), sg.Push()],
#     [sg.VPush()]
# ]

# showPage = [
#     [title],
#     [sg.Text('Choose your time'), img],
#     [back]
# ]
# '''
# layout2 = [
#     [sg.VPush()],
#     [sg.Push(), sg.Column(showPage,element_justification='c'), sg.Push()],
#     [sg.VPush()]
# ]
# '''

# #create a window
# #Python GUI: name of window
# window=sg.Window('Window Title',layout1,
#                  size=(600,250)
#                  )

# def getTime():
#     return get_time

# def getStyle():
#     return get_style


# def showGIf():

#     root = tk.Tk()
#     root.geometry("300x300")
#     canvas = tk.Canvas(root,width=300, height=300,bg='white')
#     canvas.pack()
#     im=[]
#     im = Image.open('img/loading.gif')
#     # GIF图片流的迭代器
#     iter = ImageSequence.Iterator(im)
#     #frame就是gif的每一帧，转换一下格式就能显示了
#     for frame in iter:
#         pic=ImageTk.PhotoImage(frame)
#         canvas.create_image((100,150), image=pic)
#         time.sleep(0.02)
#         root.update_idletasks()  #刷新
#         root.update()
#         root.mainloop()

# def showProcessBar():
#     for i in range(5):
#          window['-PBAR-'].update(current_count=5 - i +1)
#          window['-NUM-'].update(str(5 - i+1))
#          time.sleep(1)

# '''
# def ChangePage():
#     window=sg.Window('Window Title',layout2,
#                  size=(600,250)
#                  )
#     window["-GENEIMG-"].update(gImgUrl)
# '''

# def ChangePicSize(gImg):
    
#     # 打开一个jpg图像文件，注意是当前路径:
#     im = Image.open(gImg)
#     # 获得图像尺寸:
#     w, h = im.size
#     print('Original image size: %sx%s' % (w, h))
#     # 缩放到50%:
#     im.thumbnail((w//4, h//4))
#     print('Resize image to: %sx%s' % (w//4, h//4))
#     # 把缩放后的图像用jpeg格式保存:
#     im.save('img\\akamonn_resize.png', 'png') 
#     print('Reset size!')
#     return 'img\\akamonn_resize.png'

# def tool():
#     input.gps = GPS.getGPS()
#     input.direction = Direction.getDirection()
#     input.pic = rawPic.getRawPic(input.gps, input.direction)
#     gImg = gene.getGenePic(input.time,input.style)
#     print("check this setp tool")
#     return gImg

# # Event Loop to process "events" and get the "values" of the inputs
# while True:

#     event, values = window.read(timeout = 10, timeout_key = "-TIMEOUT-") #read of window, two return value:1.event 2.value
 
#     if event == "-OK-":
#         get_time = int(values['-SL-'])
        
#         #print(gImg)
#         print('button OK pressed')
#         #print(input.getInput())
#         window.find_element('-TITLE-').Update(visible=False)
#         window.find_element('-TEXT-').Update(visible=False)
#         window.find_element('-SL-').Update(visible=False)
#         #window.find_element('-GIF-').PopupAnimated(GifFilename)
#         #Image.UpdateAnimation(GifFilename, time_between_frames=50)
#         #window["-GENEIMG-"].update('img\\loading.gif')
        
#         #showGIf()
#         while gImg == '':
#             input.style = getStyle()
#             input.time = getTime()
#             window.find_element('-RESET-').Update(visible=False)
#             window.find_element('-OK-').Update(visible=False)
#             window.find_element('-BACK-').Update(visible=False)
#             window.find_element('-PBAR-').Update(visible=True)
#             window.find_element('-NUM-').Update(visible=True)
#             showProcessBar()         
#             tool()
 
#         print(gImg)
#         window.find_element('-PBAR-').Update(visible=False)
#         window.find_element('-NUM-').Update(visible=False)
#         window.find_element('-GENEIMG-').Update(visible=True)
#         window["-GENEIMG-"].update(ChangePicSize(gImg))
#         #window.FindElement('-GENEIMG-').Update(visible=True)
#         window.find_element('-BACK-').Update(visible=True)

#     if event == "-RESET-":
#         window["-SL-"].update(value=reTime)
#         print('button RESET pressed')

#     if event == "-BACK-":
#         window.find_element('-TITLE-').Update(visible=True)
#         window["-SL-"].update(value=reTime)
#         window.find_element('-TEXT-').Update(visible=True)
#         window.find_element('-SL-').Update(visible=True)
#         window.find_element('-GENEIMG-').Update(visible=False)
#         window.find_element('-RESET-').Update(visible=True)
#         window.find_element('-OK-').Update(visible=True)
#         window.find_element('-BACK-').Update(visible=False)
        
#         print('button BACK pressed')

#     if event==None:
#         break

# window.close()

import PySimpleGUI as sg
import models
import gene
import GPS
import time
from PIL import Image, ImageTk

sg.theme('DarkAmber')

# Initial values and configurations
reTime = 2023
reStyle = 'pixel'
gImg = ''

# GUI layout configurations
title = sg.Text(text='Time machine', font=('Arial Bold', 20), key='-TITLE-', expand_x=True, justification='center')
chooseBar = sg.Slider(range=(2050, 1950), default_value=reTime, resolution=1, orientation='v', key='-SL-')
loadBar = sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PBAR-', visible=False)
img = sg.Image(size=(30, 30), key="-GENEIMG-", visible=False)
loadNum = sg.Text('0%', key='-NUM-', enable_events=True, font=('Arial Bold', 16), justification='center', visible=False)

# Layout
layout = [
    [title],
    [sg.Text(text='Choose your time', key='-TEXT-'), chooseBar, loadBar, img],
    [loadNum, sg.Button('RESET', key='-RESET-'), sg.Button('OK', key='-OK-'), sg.Button('BACK', key='-BACK-', visible=False)]
]

# Create a window
window = sg.Window('Time Machine Application', layout, size=(600, 250))

def tool():
    input.gps = GPS.getGPS()
    input.direction = Direction.getDirection()
    input.pic = rawPic.getRawPic(input.gps, input.direction)
    gImg = gene.getGenePic(input.time,input.style)
    print("check this setp tool")
    return gImg
# Event Loop
while True:
    event, values = window.read(timeout=10)

    if event == sg.WIN_CLOSED:
        break

    if event == "-OK-":
        get_time = int(values['-SL-'])
        input = models.Input()  # Assuming this is defined in your script
        input.style = reStyle
        input.time = get_time

        window['-PBAR-'].update(visible=True)
        window['-NUM-'].update(visible=True)

        for i in range(100):
            window['-PBAR-'].update(current_count=i+1)
            window['-NUM-'].update(f'{i+1}%')
            time.sleep(0.05)  # Adjust this value as needed for your processing time

            if i == 50:  # Start the image generation around halfway
                gImg = tool()

        window['-PBAR-'].update(visible=False)
        window['-NUM-'].update(visible=False)
        window['-GENEIMG-'].update(filename=gImg, visible=True)
        window['-BACK-'].update(visible=True)

    elif event == "-RESET-":
        window['-SL-'].update(value=reTime)

    elif event == "-BACK-":
        window['-GENEIMG-'].update(visible=False)
        window['-BACK-'].update(visible=False)

window.close()

