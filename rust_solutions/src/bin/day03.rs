use std::fs;

fn p1(input: &String) -> u32 {
    let mut sum = 0;
    for line in input.lines() {
        let mut left: u32 = 0;
        let mut right: u32 = 0;
        let max_i = line.len();

        for (i, char) in line.chars().enumerate() {
            let num: u32 = char.to_digit(10).expect("not a digit");
            if num > left && i < max_i - 1 {
                left = num;
                right = 0;
            } else if num > right {
                right = num;
            }
        }
        sum += dbg!(left * 10 + right);
    }
    return sum;
}

fn solve_single_line(line: &str, num_len: usize, stack: &mut Vec<u32>) -> i64 {
    stack.clear();
    let mut drops_left = line.len() - num_len;

    for num in line.chars().filter_map(|c| c.to_digit(10)) {
        while drops_left > 0 && !stack.is_empty() && num > *stack.last().unwrap() {
            stack.pop();
            drops_left -= 1;
        }
        stack.push(num);
    }

    stack.truncate(num_len);
    stack.iter().fold(0, |acc, &num| acc * 10 + num as i64)
}

fn p2(input: &str, num_len: usize) -> i64 {
    let mut stack: Vec<u32> = Vec::with_capacity(num_len);
    input
        .lines()
        .map(|line| solve_single_line(line, num_len, &mut stack))
        .sum()
}

fn main() {
    println!("--- DAY 3 ---");
    let input = fs::read_to_string("../inputs/day03.txt").expect("Input not found");
    let p1 = p1(&input);
    println!("Solution 1: {}", p1);
    let p2 = p2(&input, 12);
    println!("Solution 2: {}", p2);
}
