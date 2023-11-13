

import PySimpleGUI as sg
import models
import rawPic
import Direction
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