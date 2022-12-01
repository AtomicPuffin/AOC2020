//First Rust file
use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};
use std::io::Result;

fn read_input(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("Filename error");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn turn(direction: i32, value: i32) -> i32 {
    let mut result = direction + value;
    if result < 0 {
        result += 360
    } else {
        result = result % 360
    }
    result
}

fn main() {
    let input = read_input("input12.txt");
    //let input = vec!["F10", "N3", "F7", "R90", "F11"];
    let mut position = (0,0,90); // X, Y , Direction (0 = N, 90 = E ...)
    for i in input {
        let action = &i[0..1];
        let value: i32 = i[1..].parse().unwrap();
        //println!("{}", i);
        match action {
            "N" => position.0 += value,
            "S" => position.0 -= value,
            "E" => position.1 += value,
            "W" => position.1 -= value,
            "L" => position.2 = turn(position.2, -value),
            "R" => position.2 = turn(position.2, value),
            "F" => match position.2 {
                0 => position.0 += value,
                90 => position.1 += value,
                180 => position.0 -= value,
                270 => position.1 -= value,
                _ => println!("This should not happen degrees")
            }
            _ => println!("This should not happen action")
        }
        //println!("{} {} {}", position.0, position.1, position.2);
    }
    println!("{}", position.0.abs() + position.1.abs());
}