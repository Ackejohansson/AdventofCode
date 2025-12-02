use std::fs;

fn read_input() -> String {
    let input_file = "../inputs/day02_test.csv";
    fs::read_to_string(&input_file).unwrap()
}
fn parse_lines(input: &str) -> String {
    let lines = input.split(",");
    for line in lines {
        let (min, max) = line.split("-");
        println!("MIN: {}, max: {}", min, max)
    }

    "10fa".to_string()
}
struct DataRange {
    min: i64,
    max: i64,
}
fn parse_chunk(chunk: &str) -> DataRange {
    let (min, max) = chunk.split_once("-").expect("Bad format: missing dash");
    let min_i: i64 = min.parse().expect("Expected int");
    let max_i: i64 = max.parse().expect("Expected int");

    DataRange {
        min: min_i,
        max: max_i,
    }
}

fn p1(input: &str) -> i64 {
    for line in input.lines() {
        println!("{}\n", line);
        let pair = line.split(",");
    }
    10
}

fn main() {
    let input: String = read_input();
    let ranges = input.split(",").map(parse_chunk);
    let parsed = parse_lines(&input);
    println!("--- Day 1: Part 1 ---");
    let result1 = p1(&input);
    println!("1: {}", result1);
    println!("--- Day 1: Part 2 ---");
}
