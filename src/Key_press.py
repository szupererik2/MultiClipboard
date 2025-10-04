import keyboard
from clip_manage.clipboard import clip
from clip_manage.copy import copy_from_clip
from clip_manage.paste import paste_from_clip
c = clip()

while True:
    try:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
            for i in range(1,13):
                if(keyboard.is_pressed(f'f{i}')):
                    copy_from_clip(c, i)
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('v'):
            for i in range(1,13):
                if(keyboard.is_pressed(f'f{i}')):
                    paste_from_clip(c, i)
    except Exception as e:
        print(f"An error occurred: {e}")