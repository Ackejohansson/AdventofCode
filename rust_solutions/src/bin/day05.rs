use std::{fs, ops::RangeInclusive};

fn p1(ranges: &Vec<RangeInclusive<i64>>, num: &str) -> usize {
    num.lines()
        .map(|num_str| {
            let num: i64 = num_str.parse().expect("Num not a number");
            num
        })
        .filter(|&num| ranges.iter().any(|range| range.contains(&num)))
        .count()
}

fn p2(mut ranges: Vec<RangeInclusive<i64>>) -> i64 {
    ranges.sort_by_key(|k| *k.start());

    let mut iter = ranges.into_iter();
    let first = match iter.next() {
        Some(r) => r,
        None => return 0,
    };

    let mut total = first.end() - first.start() + 1;
    let mut last_idx = *first.end();

    for range in iter {
        if range.start() <= &last_idx {
            if range.end() > &last_idx {
                total += range.end() - last_idx;
                last_idx = *range.end();
            }
        } else {
            total += range.end() - range.start() + 1;
            last_idx = *range.end();
        }
    }
    return total;
}

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

    println!("--- Day 05 ---");
    let result1 = p1(&ranges, num);
    println!("Result 1: {}", result1);

    let result2 = p2(ranges);
    println!("Result 2: {}", result2);
}
