# Multi Clipboard

A Python-based multi-clipboard manager that allows you to store and paste multiple clipboard contents using **function keys**.

---

## Features

- **Copy**: Press `Ctrl + F1…F12` to copy the current clipboard content into the corresponding slot.  
- **Paste**: Press `Shift + F1…F12` to paste the content from the corresponding slot.  
- **Exit**: Press `Esc` to quit the application.  
  - ⚡ This key combination can be easily changed in the code (see below).

---

## How It Works

1. Run the script `run.py`. This will automatically:
   - Install all required dependencies (if not already installed)
   - Set up the multi-clipboard functionality  
2. Use the hotkeys:
   - `Ctrl + Fn` → Copy current clipboard to that slot  
   - `Shift + Fn` → Paste content from that slot  
3. Press `Shift + Esc` (or your configured exit combo) to quit.

> **Note**: The `Fn` key on laptops is hardware-level, so you don’t need to bind it in the code — just press the physical Fn key if required to access F1–F12.

---

## Configuration

To change the exit key or any hotkeys, edit the variables at the top of `run.py`:

```python
# Example in run.py
EXIT_HOTKEY = "esc"       # change to another key combination if needed
