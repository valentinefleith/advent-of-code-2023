use std::{
    env, fs,
    io::{prelude::*, BufReader},
};

fn get_sum_of_last_digits(lines: Vec<String>) -> u32 {
    let mut all_digits: Vec<u32> = Vec::new();
    for line in lines {
        let digits: Vec<u32> = line.chars().flat_map(|char| char.to_digit(10)).collect();
        all_digits.push(digits[0] * 10 + digits[digits.len() - 1]);
    }
    let mut result = 0;
    for nb in all_digits {
        result += nb;
    }
    result
    //println!("{:?}", all_digits.iter().sum());
}

fn get_lines(filename: String) -> Vec<String> {
    let file = fs::File::open(filename).expect("No such file.");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|line| line.expect("Could not parse line."))
        .collect()
}

fn main() {
    let input_path: String = env::args().nth(1).expect("Argument required.");
    let lines = get_lines(input_path);
    //get_sum_of_last_digits(lines);
    println!("{}", get_sum_of_last_digits(lines));
}
