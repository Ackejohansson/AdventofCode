package aoc

import zio.{ZIO, ZIOAppDefault, Console}
import zio.stream.{ZStream, ZPipeline}

object Day01 extends ZIOAppDefault {
  private val InputFile = "../inputs/day1.txt"
  private val GridWidth = 100
  private val StartPos = 50

  case class Command(direction: Char, step: Int) {
    def diff: Int = if (direction == 'R') then step else -step
  }

  def parseCommand(line: String): Command = {
    Command(line.head, line.drop(1).toInt)
  }

  val inputStream: ZStream[Any, Throwable, Command] =
    ZStream
      .fromFileName(InputFile)
      .via(ZPipeline.utf8Decode >>> ZPipeline.splitLines)
      .map(parseCommand)
  
  val part1rule: (Int, Int)=> Int = (curr, next) => {
    val nextShift = Math.floorMod(next, GridWidth)
    if (nextShift == 0) then 1 else 0
  }

  val part2rule: (Int, Int) => Int = (curr, next) => {
    val offset = if (next > curr) then 0 else -1

    val currMod = Math.floorDiv(curr + offset, GridWidth)
    val nextMod = Math.floorDiv(next + offset, GridWidth)
    (nextMod - currMod).abs
  }

  def solve(stream: ZStream[Any, Throwable, Command], rule: (Int, Int) => Int): ZIO[Any, Throwable, Int] = {
    stream
      .runFold((StartPos, 0)) { case ((curr, count), cmd) =>
        val next = curr + cmd.diff
        val newCount = rule(curr, next)
        (next, count + newCount)
      }
      .map { case (curr, count) => count }
  }
  override def run: ZIO[Any, Any, Any] = {
    for {
      _ <- Console.printLine("--- DAY ONE START ---")
      p1 <- solve(inputStream, part1rule)
      _ <- Console.printLine(s"Part One solution: $p1")
      p2 <- solve(inputStream, part2rule)
      _ <- Console.printLine(s"Part Two solution: $p2")

    } yield ()
  }
}
