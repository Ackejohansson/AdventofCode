use std::fs;

fn get_input() -> String {
    fs::read_to_string("../inputs/day03.txt").expect("Input not found")
}

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
    sum
}
fn p2(input: &String, num_len: usize) -> i64 {
    // Solve with monolitic stack.
    let mut sum: i64 = 0;
    for line in input.lines() {
        let mut drops_left = line.len() - num_len;
        let mut stack: Vec<u32> = Vec::new();
        let nums: Vec<u32> = line.chars().filter_map(|c| c.to_digit(10)).collect();

        for num in nums {
            while drops_left > 0 && !stack.is_empty() && num > *stack.last().unwrap() {
                stack.pop();
                drops_left -= 1;
            }
            stack.push(num);
        }
        stack.truncate(num_len);
        let new: String = stack.iter().map(|num| num.to_string()).collect();
        println!("Stack: {}", new);
        let num: i64 = new.parse().expect("Bad number");
        sum += num;
    }
    sum
}

fn main() {
    println!("--- DAY 3 ---");
    let input = get_input();
    let p1 = p1(&input);
    println!("Solution 1: {}", p1);
    let p2 = p2(&input, 12);
    println!("Solution 2: {}", p2);
}
