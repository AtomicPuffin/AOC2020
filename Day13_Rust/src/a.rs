//use core::num::dec2flt::parse;
use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};
//use std::io::Result;

fn read_input(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("Filename error");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn parse_bus(bus_table:&str) -> Vec<i32> {
    let bus_raw = bus_table.split(",");
    let mut buses = vec![];
    for i in bus_raw {
        if i != "x" {
            let bus: i32 = i.parse().unwrap();
            buses.push(bus);
        }
    }
    buses
}

pub fn run() {
    let input = read_input("input13.txt");
    let earliest: i32 = input[0].parse().unwrap();
    let buses = parse_bus(&input[1]);
    let mut answer = (i32::MAX,i32::MAX);
    for bus in buses {
        let early = earliest - (earliest % bus) + bus;
        if early < answer.1 {
            answer = (bus, early);
        }
    }
    println!("Svaret är: {}", answer.0 * (answer.1-earliest));
}