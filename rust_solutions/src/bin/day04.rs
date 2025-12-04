use std::{collections::HashMap, fs, i32, iter::Inspect};

const DIRECTIONS: [(i32, i32); 8] = [
    (-1, 1),
    (0, 1),
    (1, 1),
    (-1, 0),
    (1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
];

#[derive(Debug, Hash, PartialEq, Eq)]
struct Position {
    i: i32,
    j: i32,
}
impl Position {
    fn paper_neighbors(&self, grid: &HashMap<Position, Tile>) -> i32 {
        DIRECTIONS
            .iter()
            .filter(|(di, dj)| -> bool {
                let neigh = &Position {
                    i: self.i + di,
                    j: self.j + dj,
                };
                grid.get(&neigh) == Some(&Tile::Paper)
            })
            .count() as i32
    }
}

#[derive(Debug, Hash, PartialEq, Eq)]
enum Tile {
    Floor,
    Paper,
}

fn build_grid(input: &str) -> HashMap<Position, Tile> {
    input
        .lines()
        .enumerate()
        .flat_map(|(i, line)| {
            dbg!(line);
            line.chars().enumerate().map(move |(j, char)| {
                (
                    Position {
                        i: i as i32,
                        j: j as i32,
                    },
                    if char == '@' {
                        Tile::Paper
                    } else {
                        Tile::Floor
                    },
                )
            })
        })
        .collect()
}

fn solution(grid: &HashMap<Position, Tile>) -> i32 {
    grid.iter()
        .filter(|(pos, tile)| -> bool { **tile == Tile::Paper && pos.paper_neighbors(&grid) < 4 })
        .inspect(|(pos, tile)| println!("Caught tile:{:?}, pos {:?}", tile, pos))
        .count() as i32
}

fn main() {
    let input: String = fs::read_to_string("../inputs/day04.txt").expect("File not found");
    let grid: HashMap<Position, Tile> = build_grid(&input);
    println!("--- DAY 4 ---");
    let p1 = solution(&grid);
    println!("1: {}", p1);
}
