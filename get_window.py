import pyautogui
import pywinctl
import time
from pynput.mouse import Controller

start = time.time()

# Step 1: Find the RuneLite window
windows = pywinctl.getWindowsWithTitle("RuneLite - 5 Your Username")
if windows:
    win = windows[0]
    x, y = win.left, win.top
    w, h = win.width, win.height

    print(f"Found: {win.title}")
    print(f"Top-left: ({x}, {y})")
    print(f"Size: {w}x{h}")

    # Step 2: Move mouse there (optional)
    mouse = Controller()
    mouse.position = (x, y)

    # Step 3: Screenshot that window region
    screenshot = pyautogui.screenshot(region=(x, y, w, h))
    screenshot.save("runelite_capture.png")
    print("Screenshot saved as runelite_capture.png")

else:
    print("RuneLite window not found.")

print(f"Took {time.time() - start:.4f} seconds")
