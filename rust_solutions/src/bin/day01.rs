use std::error::Error;
use std::{env, fs};

fn main() {
    println!("PART 1 solution:");
    let args: Vec<String> = env::args().collect();
    let is_test: bool = args.contains(&"test".to_string());

    let input = read_input(is_test);
    println!("--- Day 1: Part 1 ---");
    let result1 = p1(input);
    println!("Part 1 Result: {}", result1);
}

fn read_input(is_test: bool) -> String {
    let day = "day1";

    let filename = format!(
        "../inputs/{}{}.txt",
        day,
        if is_test { "_test" } else { "" }
    );

    fs::read_to_string(&filename).unwrap()
}
fn p1(input: String) -> i32 {
    let mut total = 50;
    let mut count = 0;
    for line in input.lines() {
        let head: String = line.chars().take(1).collect();
        let tail: i32 = line[1..].parse().unwrap_or(0);
        let delta: i32 = if head == "R" { tail } else { -tail };

        dbg!(head);
        dbg!(tail);

        total += delta;
        total = total.rem_euclid(100);

        if total == 0 {
            count += 1;
        }
    }
    dbg!(count)
}
