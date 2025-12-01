use std::{env, fs};
fn main() {
    let args: Vec<String> = env::args().collect();
    let is_test: bool = args.contains(&"test".to_string());

    let input = read_input(is_test);
    println!("--- Day 1: Part 1 ---");
    let result1 = p1(&input);
    println!("Part 1 Result: {}", result1);
    println!("--- Day 1: Part 2 ---");
    let result2 = p2(&input);
    println!("Part 2 Result: {}", result2);
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

fn p1(input: &str) -> i32 {
    let mut total = 50;
    let mut count = 0;
    for line in input.lines() {
        let head: String = line.chars().take(1).collect();
        let tail: i32 = line[1..].parse().unwrap_or(0);
        let delta: i32 = if head == "R" { tail } else { -tail };

        total += delta;
        total = total.rem_euclid(100);

        if total == 0 {
            count += 1;
        }
    }
    count
}

fn p2(input: &str) -> i32 {
    let mut curr: i32 = 50;
    let mut count: i32 = 0;

    for line in input.lines() {
        let direction: String = line.chars().take(1).collect();
        let step_size: i32 = line[1..].parse().unwrap();

        let next: i32 = curr
            + if direction == "R" {
                step_size
            } else {
                -step_size
            };

        let offset: i32 = if direction == "R" { 0 } else { 1 }; // Handle shifting left
        let curr_mod: i32 = (curr - offset).div_euclid(100);
        let next_mod: i32 = (next - offset).div_euclid(100);

        let diff: i32 = (next_mod - curr_mod).abs();

        curr = next;
        count += diff;
    }
    count
}
