use std::fs;
use std::str::FromStr;
struct DataRange {
    min: i64,
    max: i64,
}
impl FromStr for DataRange {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (min_str, max_str) = s.split_once("-").ok_or("Bad format: missing dash")?;
        Ok(DataRange {
            min: min_str.parse().map_err(|_| "Invalid Min")?,
            max: max_str.parse().map_err(|_| "Invalid Max")?,
        })
    }
}

fn read_input() -> String {
    fs::read_to_string("../inputs/day02_test.csv")
        .expect("❌ CRITICAL ERROR: Could not find input file!")
}

fn filter1(number: i64) -> bool {
    let nr_str: String = number.to_string();
    if nr_str.len() % 2 != 0 {
        return false;
    };
    let (left, right) = nr_str.split_at(nr_str.len() / 2);
    left == right
}

fn filter2(number: i64) -> bool {
    let nr_str = number.to_string();
    let len = nr_str.len();

    for num in 1..=len / 2 {
        if nr_str.len() % num != 0 {
            continue;
        }

        let slice = &nr_str[..num];
        if slice.repeat(len / num) == nr_str {
            return true;
        }
    }
    false
}

fn solution(input: &[DataRange], filter: fn(i64) -> bool) -> i64 {
    let mut sum: i64 = 0;
    for dr in input {
        for number in dr.min..=dr.max {
            if filter(number) {
                sum += number;
            }
        }
    }
    sum
}

fn main() {
    let input: String = read_input();
    let ranges: Vec<DataRange> = input.split(",").filter_map(|s| s.parse().ok()).collect();

    println!("--- Day 1: Part 1 ---");
    println!("1: {}", solution(&ranges, filter1));

    println!("\n--- Day 1: Part 2 ---");
    println!("2: {}", solution(&ranges, filter2));
}
