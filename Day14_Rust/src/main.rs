use std::collections::HashMap;
use std::collections::HashSet;
use std::fs;

fn main() {
    println!(
        "Answer to Part 1 test: {}",
        part_1(&read_file("example.txt"))
    );
    println!("Answer to Part 1: {}", part_1(&read_file("input.txt")));
    println!(
        "Answer to Part 2 test: {}",
        part_2(&read_file("example2.txt"))
    );
    println!("Answer to Part 2: {}", part_2(&read_file("input.txt")));
}

fn part_1(input: &str) -> i64 {
    let mut lines = input.lines();
    let mut mask = (i64::MAX, 0);
    let mut x = HashMap::new();
    for line in lines {
        if line.starts_with("mask") {
            mask = parse_mask(line);
            continue;
        }
        let parts = line.split(" = ").collect::<Vec<&str>>();
        let address = parts[0][4..parts[0].len() - 1].parse::<i64>().unwrap();
        let value = parts[1].parse::<i64>().unwrap();
        x.insert(address, (value & mask.0) | mask.1);
        println!("Binary post: {:064b}", x[&address]);
    }
    let mut sum = 0;
    for (_k, v) in x {
        sum += v;
    }
    sum
}

fn part_2(input: &str) -> i64 {
    0
}
fn set_bit(n: i64, pos: i64) -> i64 {
    n | (1 << pos)
}
fn clear_bit(n: i64, pos: i64) -> i64 {
    n & !(1 << pos)
}
fn parse_mask(mask_line: &str) -> (i64, i64) {
    let mut mask_0 = i64::MAX;
    let mut mask_1 = 0;
    let mask = mask_line.split(" = ").collect::<Vec<&str>>()[1];
    for (i, c) in mask.chars().enumerate() {
        match c {
            '0' => mask_0 = clear_bit(mask_0, 35 - i as i64),
            '1' => mask_1 = set_bit(mask_1, 35 - i as i64),
            _ => (),
        }
    }
    println!("Mask 0: {:064b}", mask_0);
    println!("Mask 1: {:064b}", mask_1);
    (mask_0, mask_1)
}

fn read_file(file: &str) -> String {
    fs::read_to_string(file).unwrap().trim().to_string()
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq;

    #[test]
    fn test_p1_ex() {
        assert_eq!(part_1(&read_file("example.txt")), 165);
    }

    #[test]
    fn test_p1() {
        assert_eq!(part_1(&read_file("input.txt")), 6513443633260);
    }

    #[test]
    fn test_p2_ex() {
        assert_eq!(part_2(&read_file("example2.txt")), 208);
    }

    #[test]
    fn test_p2() {
        assert_eq!(part_2(&read_file("input.txt")), 0);
    }
}
