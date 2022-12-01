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

fn turn(wpt: (i32, i32), value: i32) -> (i32, i32) {
    let mut new = (0,0);
    match value {
        90 | -270 => new = (-wpt.1, wpt.0),
        -90 | 270 => new = (wpt.1, -wpt.0),
        180 | -180 => new = (-wpt.0, -wpt.1),
        _ => println!("This should not happen degrees")
    }
    new
}

fn main() {
    let input = read_input("input12.txt");
    //let input = vec!["F10", "N3", "F7", "R90", "F11"];
    let mut position = (0,0);
    let mut waypoint = (1, 10);
    //for i in input.iter() {
    for i in input {
        let action = &i[0..1];
        let value: i32 = i[1..].parse().unwrap();
        println!("Instruction {}", i);
        match action {
            "N" => waypoint.0 += value,
            "S" => waypoint.0 -= value,
            "E" => waypoint.1 += value,
            "W" => waypoint.1 -= value,
            "L" => waypoint = turn(waypoint, -value),
            "R" => waypoint = turn(waypoint, value),
            "F" => position = (position.0 + waypoint.0 * value, position.1 + waypoint.1 * value),
            _ => println!("This should not happen action")
        }
        println!("Waypoint {} {}", waypoint.0, waypoint.1);
        println!("Position {} {}", position.0, position.1);
    }
    println!("{}", position.0.abs() + position.1.abs());
}