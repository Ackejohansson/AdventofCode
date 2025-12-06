use std::{fs, ops::RangeInclusive};

fn main() {
    let input = fs::read_to_string("../inputs/day05.txt").expect("File not found");
    let (range_str, num) = input.split_once("\n\n").unwrap();

    let ranges: Vec<RangeInclusive<i64>> = range_str
        .lines()
        .map(|line| {
            let (lo, hi) = line.split_once("-").expect("No - found.");
            let lo: i64 = lo.parse().expect("Not a number");
            let hi: i64 = hi.parse().expect("Not a number");
            lo..=hi
        })
        .collect();

    let count = num
        .lines()
        .map(|num_str| {
            let num: i64 = num_str.parse().expect("Num not a number");
            num
        })
        .filter(|&num| ranges.iter().any(|range| range.contains(&num)))
        .count();
    dbg!(count);
}
