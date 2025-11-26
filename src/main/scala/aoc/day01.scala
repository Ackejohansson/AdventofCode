package aoc

object Day01:
  def main(args: Array[String]): Unit =
    println("Hello from Scala! We are ready for Day 1.")

    val rawInput = os.read(os.pwd / "inputs" / "day01.txt")
    val lines = rawInput.linesIterator.toList

    lines.take(5).foreach(println)
