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

fn parse_bus(bus_table:&str) -> Vec<(i64, i64)> {
    let bus_raw = bus_table.split(",");
    let mut buses: Vec<(i64, i64)> = vec![];
    let mut counter = 0;
    for i in bus_raw {
        if i != "x" {
            let bus: i64 = i.parse().unwrap();
            buses.push((bus, counter));
        }
        counter += 1;
    }
    buses.sort_by(|a,b|b.0.cmp(&a.0));
    buses
}

pub fn run() {
    let input = read_input("input13.txt");
    //let input = read_input("input13 copy.txt");
    let buses = parse_bus(&input[1]);
    let mut counter = -buses[0].1;
    loop {
        let mut is_the_one = true;
        for bus in &buses {
            if ((counter+bus.1) % bus.0) != 0 {
                is_the_one = false;
                break;
            } 
        }
        if is_the_one {
            println!("Svaret är: {}", counter);
        break;
        }
        counter += &buses[0].0;
    }  
}