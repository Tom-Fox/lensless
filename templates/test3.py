import PySimpleGUI as sg

layout = [
    [sg.Text('Click to add a row inside the frame'), sg.B('+', key='-B1-')],
    [sg.Column([[sg.T('A New Input Line1')]], key='-COL1-', scrollable=True, vertical_scroll_only=True, size=(500, 200))],
    [sg.Input(key='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
    [sg.Button('Clear'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout, finalize=True)
i = 0
while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-B1-':
        window.extend_layout(window['-COL1-'], [[sg.T('A New Input Line'), sg.I(key=f'-IN-{i}-')]])
        i += 1
        window['-COL1-'].contents_changed()

    if event == "Clear":
        window['-COL1-'].update([])


window.close()