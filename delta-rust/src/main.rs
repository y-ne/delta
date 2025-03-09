use windows::{
    Win32::Foundation::POINT,
    Win32::UI::WindowsAndMessaging::GetCursorPos,
};

fn get_cursor_position() -> Option<(i32, i32)> {
    let mut point = POINT { x: 0, y: 0 };
    
    unsafe {
        if GetCursorPos(&mut point).as_bool() {
            Some((point.x, point.y))
        } else {
            None
        }
    }
}

fn main() {
    match get_cursor_position() {
        Some((x, y)) => println!("Cursor Position: ({}, {})", x, y),
        None => eprintln!("Failed to get cursor position!"),
    }
}
