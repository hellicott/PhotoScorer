import PySimpleGUI as sg

from src.ImageManager import ImageManager

folder = sg.PopupGetFolder(message='Find the folder of images', title='Browse For Folder')
image_manager = ImageManager(folder)

scoring_layout = [
    [sg.Image(filename=image_manager.get_image_path(), key='-IMAGE-', size=(160, 120))],
    [sg.Text(text=image_manager.get_image_title(), key='-TITLE-')],
    [sg.Slider(range=(1, 10), default_value=5, orientation='horizontal', key='-SCORE-')],
    [sg.Button('Hold & Next'), sg.Button('Next')]
]

scoring_window = sg.Window('ImageScorer', scoring_layout)


def reset_for_new_image():
    scoring_window['-IMAGE-'].update(filename=image_manager.get_image_path())
    scoring_window['-TITLE-'].update(filename=image_manager.get_image_title())


while True:
    event, values = scoring_window.read()
    if event == 'Next':
        image_manager.save_score(values['-SCORE-'])
        image_manager.next()
        reset_for_new_image()
    else:
        break
    print('You entered ', values[0])

scoring_window.close()