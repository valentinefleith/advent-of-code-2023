use regex::Regex;
use std::{
    env, fs,
    io::{prelude::*, BufReader},
};

const NUMBERS: [&str; 9] = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];

fn get_digits_in_line(line: String) -> Vec<u32> {
    let numbers_pattern = r"(?:zero|one|two|three|four|five|six|seven|eight|nine)";
    let regexpr = Regex::new(numbers_pattern).unwrap();
    let with_digits = regexpr.replace_all(&line, |caps: &regex::Captures| {
        let words = &caps[0];
        let index = NUMBERS.iter().position(|&w| w == words).unwrap() + 1;
        index.to_string()
    });
    let with_digits = with_digits.into_owned();
    with_digits
        .chars()
        .flat_map(|char| char.to_digit(10))
        .collect()
}

fn get_sum_of_last_digits(lines: Vec<String>) -> u32 {
    let mut all_digits: Vec<u32> = Vec::new();
    for line in lines {
        let digits: Vec<u32> = get_digits_in_line(line);
        all_digits.push(digits.first().expect("Error.") * 10 + digits.last().expect("Error."));
    }
    println!("{:?}", all_digits);
    all_digits.iter().sum()
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
    println!("{}", get_sum_of_last_digits(lines));
}
