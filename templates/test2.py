import PySimpleGUI as sg

def make_window1():
    layout = [[sg.Text('Window 1'), ],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(20, 1), key='-OUTPUT-')],
              [sg.Button('Launch 2'), sg.Button('Output')]]

    return sg.Window('Window 1', layout,size=(600,250), finalize=True)

def make_window2():
    layout = [[sg.Text('Window 2')],
               [sg.Button('Exit')]]

    return sg.Window('Window 2', layout,size=(600,250), finalize=True)

def main():
    window2 = None
    window1 = make_window1()

    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED and window == window1:
            break

        if window == window1:
            window1['-OUTPUT-'].update(values['-IN-'])

        if event == 'Launch 2' and not window2:
            window1.hide()
            window2 = make_window2()

        if window == window2 and (event in (sg.WIN_CLOSED, 'Exit')):
            window2.close()
            window2 = None
            window1.un_hide()
    window1.close()

if __name__ == '__main__':
    main()
