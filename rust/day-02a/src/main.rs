use std::{
    env, fs,
    io::{prelude::*, BufReader},
};

//enum Color {
//Red = 12,
//Green = 13,
//Blue = 14,
//}

#[derive(Debug)]
struct Round {
    red: i32,
    green: i32,
    blue: i32,
}

#[derive(Debug)]
struct Game {
    id: u32,
    sets: Vec<Round>,
}

//impl Game {
//    fn is_valid(&self) -> bool {
//        for set in self.sets {
//
//        }
//    }
//}

fn round_constructor(round_data: &str) -> Round {
    let mut red = 0;
    let mut green = 0;
    let mut blue = 0;
    for reveal in round_data.split(',') {
        let colors: Vec<&str> = reveal.split_whitespace().collect();
        let nb: i32 = colors[0].parse().expect("Could not parse nb of cubes.");
        let color = colors[1];
        match color {
            "red" => red += nb,
            "green" => green += nb,
            "blue" => blue += nb,
            _ => continue,
        }
    }
    Round { red, green, blue }
}

fn game_constructor(game_summaries: Vec<String>) -> Game {
    println!("{:?}", game_summaries);
    let id: u32 = game_summaries[0]
        .trim()
        .chars()
        .last()
        .unwrap()
        .to_digit(10)
        .expect("Could not parse game ID.");
    let sets: Vec<Round> = game_summaries[1]
        .trim()
        .split(';')
        .map(|round| round_constructor(round))
        .collect();
    Game { id, sets }
}


fn build_game_list(lines: Vec<String>) -> Vec<Game> {
    lines
        .iter()
        .map(|line| game_constructor(line.split(':').map(String::from).collect()))
        .collect()
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
    let games = build_game_list(lines);
    println!("{:?}", games);
}
