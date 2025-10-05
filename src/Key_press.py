import keyboard
from clip_manage.clipboard import clip
from clip_manage.copy import copy_from_clip
from clip_manage.paste import paste_from_clip

def detect_key_press():
    c = clip()

    for i in range(1, 13):
        keyboard.add_hotkey(f"ctrl+f{i}", lambda i=i: copy_from_clip(c, i))
        keyboard.add_hotkey(f"shift+f{i}", lambda i=i: paste_from_clip(c, i))

    print("Press ESC to quit")
    keyboard.wait("esc")