import pyperclip
import keyboard

def paste_from_clip(c, key):
   
   paste_data = c.req_data(key)
   pyperclip.copy(paste_data)
   keyboard.press_and_release('ctrl+v')
