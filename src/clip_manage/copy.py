import pyperclip

def copy_from_clip(c, key):
   c.add_data(key, pyperclip.paste())