import pyautogui
import time

# Inventory area percentages and dimensions
inventory_top_left_x_percent = 0.722
inventory_top_left_y_percent = 0.443
inventory_bottom_right_x_percent = 0.935
inventory_bottom_right_y_percent = 0.886
rows, cols = 7, 4

# Calculate inventory slot positions once
inventory_slots = {}
slot_width_percent = (inventory_bottom_right_x_percent - inventory_top_left_x_percent) / cols
slot_height_percent = (inventory_bottom_right_y_percent - inventory_top_left_y_percent) / rows

for row in range(rows):
    for col in range(cols):
        slot_num = row * cols + col
        slot_center_x_percent = inventory_top_left_x_percent + (col * slot_width_percent) + (slot_width_percent / 2)
        slot_center_y_percent = inventory_top_left_y_percent + (row * slot_height_percent) + (slot_height_percent / 2)
        inventory_slots[slot_num] = (slot_center_x_percent, slot_center_y_percent)

def get_inventory_coords(slot_num):
    runelite = pyautogui.getWindowsWithTitle("RuneLite")[0]
    x_percent, y_percent = inventory_slots[slot_num]
    x = runelite.left + int(runelite.width * x_percent)
    y = runelite.top + int(runelite.height * y_percent)
    return x, y

# Find RuneLite window and bring it to focus first
runelite_windows = pyautogui.getWindowsWithTitle("RuneLite")
if runelite_windows:
    runelite = runelite_windows[0]
    runelite.activate()  # This brings the window to the foreground and gives it focus
    time.sleep(0.5)  # Wait for the window to gain focus

    # Example: Shift+click on slot 1
    x, y = get_inventory_coords(1)
    pyautogui.moveTo(x, y, duration=0.5)  # Slow down the mouse movement

    time.sleep(0.2)  # Small pause before clicking

    # Using pyautogui for shift+click
    pyautogui.keyDown('shift')
    time.sleep(0.1)
    pyautogui.click(x, y)
    time.sleep(0.1)
    pyautogui.keyUp('shift')

    time.sleep(0.3)  # Pause after the whole action
else:
    print("RuneLite window not found")