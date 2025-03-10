use windows::{
    Win32::Foundation::POINT,
    Win32::UI::WindowsAndMessaging::GetCursorPos,
};
use std::time::Instant;

fn get_cursor_position() -> Option<(i32, i32)> {
    let mut point = POINT { x: 0, y: 0 };
    unsafe {
        GetCursorPos(&mut point).ok()?;
    }
    Some((point.x, point.y))
}

fn main() {
    // Benchmark configuration
    let runs = 100_000;

    let start = Instant::now();
    for _ in 0..runs {
        let _ = get_cursor_position();
    }
    let duration = start.elapsed();

    let avg_duration = duration.as_nanos() as f64 / runs as f64;

    // Display results
    if let Some((x, y)) = get_cursor_position() {
        println!("Cursor Position: ({}, {})", x, y);
    } else {
        println!("Failed to get cursor position.");
    }

    println!("Total time for {} calls: {:.3?}", runs, duration);
    println!("Average time per call: {:.2} ns", avg_duration);
}
