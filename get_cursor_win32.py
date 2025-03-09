import ctypes
import timeit

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

user32 = ctypes.WinDLL('user32', use_last_error=False)
GetCursorPos = user32.GetCursorPos
cursor = POINT()

def get_cursor_pos():
    GetCursorPos(ctypes.byref(cursor))
    return cursor.x, cursor.y

execution_time = timeit.timeit(get_cursor_pos, number=10000) / 10000 * 1_000_000
cursor_x, cursor_y = get_cursor_pos()

print(type(cursor_x))  # <class 'int'>
print(type(cursor_y))  # <class 'int'>
print(f"Cursor position: ({cursor_x}, {cursor_y})")
print(f"Average time taken: {execution_time:.6f} µs")
