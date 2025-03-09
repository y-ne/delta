import ctypes
import timeit

user32 = ctypes.windll.user32
GetCursorPos = user32.GetCursorPos
point = (ctypes.c_long * 2)()

GetCursorPos(point)
cursor_x, cursor_y = point[0], point[1]

execution_time = timeit.timeit(lambda: GetCursorPos(point), number=10000) / 10000 * 1_000_000

print(f"Cursor position: ({cursor_x}, {cursor_y})")
print(f"Average time taken: {execution_time:.6f} µs")
