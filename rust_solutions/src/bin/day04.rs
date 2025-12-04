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

#[derive(Debug, Hash, PartialEq, Eq, Clone, Copy)]
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

fn part_one(grid: &HashMap<Position, Tile>) -> i32 {
    grid.iter()
        .filter(|(pos, tile)| -> bool { **tile == Tile::Paper && pos.paper_neighbors(&grid) < 4 })
        .inspect(|(pos, tile)| println!("Caught tile:{:?}, pos {:?}", tile, pos))
        .count() as i32
}
fn part_two(grid: &mut HashMap<Position, Tile>) -> i32 {
    let mut total_removed = 0;
    loop {
        let to_remove: Vec<Position> = grid
            .iter()
            .filter(|(pos, tile)| **tile == Tile::Paper && pos.paper_neighbors(&grid) < 4)
            .map(|(pos, _)| *pos)
            .collect();
        if to_remove.is_empty() {
            break;
        }
        total_removed += to_remove.len();

        to_remove.iter().for_each(|pos| {
            grid.remove(&pos);
        });
    }
    total_removed as i32
}
fn main() {
    let input: String = fs::read_to_string("../inputs/day04.txt").expect("File not found");
    let mut grid: HashMap<Position, Tile> = build_grid(&input);
    println!("--- DAY 4 ---");
    let p1 = part_one(&grid);
    println!("1: {}", p1);

    let p2 = part_two(&mut grid);
    println!("2: {}", p2)
}
