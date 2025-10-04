import keyboard

while True:
    try:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
            
            for i in range(1,13):
                if(keyboard.is_pressed(f'f{i}')):
                    print(f"COPPY TRIGGERED ON SLOT {i}")
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('v'):
            for i in range(1,13):
                if(keyboard.is_pressed(f'f{i}')):
                    print(f"PASTE TRIGGERED FROM SLOT {i}")
    except Exception as e:
        print(f"An error occurred: {e}")