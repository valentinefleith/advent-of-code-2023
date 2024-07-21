use std::{
    env, fs,
    io::{prelude::*, BufReader},
};

enum Color {
    Red = 12,
    Green = 13,
    Blue = 14,
}

#[derive(Debug)]
struct Round {
    red: i32,
    green: i32,
    blue: i32,
}

#[derive(Debug)]
struct Game {
    id: i32,
    sets: Vec<Round>,
}

//impl Game {
//    fn is_valid(&self) -> bool {
//        for set in self.sets {
//
//        }
//    }
//}


//fn round_constructor

fn game_constructor(raw_rounds: Vec<&str>) -> Vec<Vec<Vec<&str>>> {
    let game: Vec<Vec<Vec<&str>>> = raw_rounds
        .iter()
        .map(|rounds| {
            rounds
                .split(",")
                .map(|c| c.trim().split(" ").collect())
                .collect()
        })
        .collect();
    println!("{:?}", game);
    game
}

fn build_game_list(lines: Vec<String>) {
    let games: Vec<Vec<&str>> = lines
        .iter()
        .filter_map(|game| game.split(":").nth(1))
        .map(|round| round.split(";").collect())
        .collect();
    let games_list: Vec<Vec<Vec<Vec<&str>>>> = games
        .iter()
        .map(|game| game_constructor(game.to_vec()))
        .collect();
    //println!("{:?}", games);
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
}
