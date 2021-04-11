import PySimpleGUI as sg
import webbrowser

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
naverUrl = 'https://en.dict.naver.com/#/search?range=all&query='
class Window:

    def __init__(self, text, x, y):
        sg.theme("Dark")
        self.text = text
        column_to_be_centered = [[sg.Text(text, font="BatangChe 18", enable_events=True)]]
        layout = [[sg.Column(column_to_be_centered, element_justification='center')]]
        self.window = sg.Window("Korean Lookup", layout, location=(x, y), finalize=True, element_justification='c', icon="Images/papago.ico")
        self.window.bring_to_front()
        self.window.set_min_size((300, 50))

    def run(self, korean):
        while True:
            event, values = self.window.read()
            if event == self.text:
                webbrowser.get(chrome_path).open(naverUrl+korean) # if we click on the text, will take us to naver.
                break
            if event == sg.WIN_CLOSED:
                break
        self.window.close()
    def close(self):
        self.window.close()
