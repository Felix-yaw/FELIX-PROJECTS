import PySimpleGUI as sg
import pyttsx3
#NAME: FELIX AZAGLO
# ID :10951571
#COMPUTER ENGINEERING



layout = [[sg.Text('Enter Text to be spoken: '), sg.Input(key='-INPUT-')],
          [sg.Column([[sg.Radio('Male Voice', 'voice', key='-MALE-', default=True), sg.Radio('Female Voice', 'voice', key='-FEMALE-')]], element_justification='c')],
          [sg.Button('Speak'), sg.Button('Exit')]]



window = sg.Window('Text to Speech App', layout)
engine = pyttsx3.init()


def say_text(text, voice_type):
    voices = engine.getProperty('voices')
    if voice_type == 'male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Speak':
        text = values['-INPUT-']
        if values['-MALE-']:
            say_text(text, 'male')
        else:
            say_text(text, 'female')

                    
window.close()
