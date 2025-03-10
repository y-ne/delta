use screenshots::Screen;
use windows::{Win32::Foundation::POINT, Win32::UI::WindowsAndMessaging::GetCursorPos};
use std::time::Instant;

fn get_cursor_position() -> Option<(i32, i32)> {
    let mut point = POINT { x: 0, y: 0 };
    unsafe {
        GetCursorPos(&mut point).ok()?;
    }
    Some((point.x, point.y))
}

fn capture_fullscreen() -> Option<()> {
    let screen = Screen::from_point(0, 0).ok()?;
    let img = screen.capture().ok()?;
    img.save("screenshot.png").ok()?;
    Some(())
}

fn main() {
    // Benchmark Cursor Position
    let runs_cursor = 100_000;
    let start_cursor = Instant::now();
    for _ in 0..runs_cursor {
        let _ = get_cursor_position();
    }
    let duration_cursor = start_cursor.elapsed();
    let avg_cursor_ns = duration_cursor.as_nanos() as f64 / runs_cursor as f64;

    if let Some((x, y)) = get_cursor_position() {
        println!("Cursor Position: ({}, {})", x, y);
    } else {
        println!("Failed to get cursor position.");
    }

    println!("Cursor position total time for {} calls: {:.3?}", runs_cursor, duration_cursor);
    println!("Average cursor fetch time: {:.2} ns", avg_cursor_ns);

    // Benchmark screenshot (single run, heavier operation)
    let screenshot_start = Instant::now();
    if capture_fullscreen().is_some() {
        let screenshot_duration = screenshot_start.elapsed();
        println!("Screenshot captured successfully in {:.2?}", screenshot_duration);
    } else {
        println!("Failed to capture screenshot.");
    }
}
