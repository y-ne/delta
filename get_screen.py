import ctypes
from PIL import ImageGrab
import timeit

# Get screen size
user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

# Capture screenshot with benchmark
start = timeit.default_timer()
img = ImageGrab.grab(bbox=(0, 0, width, height))
img.save("simple_screenshot.png")
end = timeit.default_timer()

screenshot_time = (end - start) * 1000  # milliseconds

print(f"Screenshot saved as simple_screenshot.png ({width}x{height}) in {screenshot_time:.2f} ms")