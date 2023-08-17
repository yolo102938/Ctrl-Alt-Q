import keyboard
import pyperclip
import ctypes
import pyautogui
import time

def double_click_current_position():
    x, y = pyautogui.position()
    pyautogui.tripleClick(x, y)
    
def convert_text(text):
    conversion_dict = {
        'q': '/',
        'w': '\'',
        'e': '\u05E7',
        'r': '\u05E8',
        't': '\u05D0',
        'y': '\u05D8',
        'u': '\u05D5',
        'i': '\u05DF',
        'o': '\u05DD',
        'p': '\u05E4',
        'a': '\u05E9',
        's': '\u05D3',
        'd': '\u05D2',
        'f': '\u05DB',
        'g': '\u05E2',
        'h': '\u05D9',
        'j': '\u05D7',
        'k': '\u05DC',
        'l': '\u05DA',
        'z': '\u05D6',
        'x': '\u05E1',
        'c': '\u05D1',
        'v': '\u05D4',
        'b': '\u05E0',
        'n': '\u05DE',
        'm': '\u05E6',
        ';': '\u05E3',
        ',': '\u05EA',
        '.': '\u05E5',
        ' ': ' ',
        '/': '.'
    }
    
    converted_text = ''
    for char in text:
        if char.lower() in conversion_dict:
            converted_text += conversion_dict[char.lower()]
        else:
            converted_text += char
    return converted_text

def convert_selected_text():
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.1)
    selected_text = pyperclip.paste()
    converted_text = convert_text(selected_text)
    pyperclip.copy(converted_text)
    keyboard.press_and_release('ctrl+v')  # Paste the converted text

time.sleep(0.2)
double_click_current_position()
time.sleep(0.3)
convert_selected_text()