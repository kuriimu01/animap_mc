import time
import pyautogui

def send_minecraft_commands(map_id, z_coord):
    time.sleep(1)
    
    # Ice block command
    pyautogui.press('/')  
    pyautogui.write(f'setblock ~ ~-1 ~{z_coord} minecraft:packed_ice') 
    pyautogui.press('enter') 
    time.sleep(0.1)

    # Spruce stairs facing east and another one, facing west 
    pyautogui.press('/')  # Open chat again
    pyautogui.write(f'setblock ~1 ~-1 ~{z_coord} minecraft:spruce_stairs[facing=east]')  
    pyautogui.press('enter')
    time.sleep(0.1)
    
    pyautogui.press('/')  # Open chat again
    pyautogui.write(f'setblock ~-1 ~-1 ~{z_coord} minecraft:spruce_stairs[facing=west]') 
    pyautogui.press('enter')
    time.sleep(0.1)

    # Wool blocks commands
    pyautogui.press('/') 
    pyautogui.write(f'setblock ~-2 ~ ~{z_coord} minecraft:white_wool')  
    pyautogui.press('enter')
    time.sleep(0.1)

    pyautogui.press('/')  
    pyautogui.write(f'setblock ~2 ~ ~{z_coord} minecraft:white_wool') 
    pyautogui.press('enter')
    time.sleep(0.1)

    pyautogui.press('/') 
    pyautogui.write(f'setblock ~2 ~1 ~{z_coord} minecraft:white_wool') 
    pyautogui.press('enter')
    time.sleep(0.1)

    # Item frame with map summon command
    pyautogui.press('/')
    pyautogui.write(f'summon minecraft:item_frame ~1 ~1 ~{z_coord} {{Facing:4, Item:{{id:"minecraft:filled_map",Count:1b,tag:{{map:{map_id}}}}}}}')
    pyautogui.press('enter')
    time.sleep(0.1)

def main():
    map_id = 0
    z_coord = 0

    # Put your last frame id here
    while map_id <= 1406:
        
        
        send_minecraft_commands(map_id, z_coord)

        # Increment map_id and z_coord for the next cycle
        map_id += 1
        z_coord += 1
        print(f"Cycle {map_id} completed.")
        time.sleep(0.1)
    print("Program finished.")

if __name__ == "__main__":
    main()
