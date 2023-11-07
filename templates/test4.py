import PySimpleGUI as sg

layout = [

[sg.Col([[sg.T('Enter your name:'),sg.In()],[sg.Btn('Ok'), sg.Btn('Exit'),
sg.Btn('Add new row')]],k='col_key')]

]

window = sg.Window('Test', layout)

while True:
    event, values = window.read()
    if event in ('Exit' ,sg.WIN_CLOSED):
        break

    if event == ('Add new row'):
        window.extend_layout(window['col_key'],[[sg.T('Enter your name:', key='new_raw'),(sg.In())]])
        window.extend_layout(window['col_key'],[[sg.Btn('Retreat', key='re')]])

    if event == ('re'):
        window['new_raw'].hide_row()
        window['re'].hide_row()

window.close()