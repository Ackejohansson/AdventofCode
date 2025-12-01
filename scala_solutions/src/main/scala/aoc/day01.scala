package aoc

import zio.{ZIO, ZIOAppDefault, Console}
import zio.stream.{ZStream, ZPipeline}

object Day01 extends ZIOAppDefault {
  private val InputFile = "../inputs/day1.txt"
  // case class InputRow(direction: String, step: Int)

  val inputStream: ZStream[Any, Throwable, String] =
    ZStream
      .fromFileName(InputFile)
      .via(ZPipeline.utf8Decode >>> ZPipeline.splitLines)
      .tap(line => Console.printLine(s"Debug: $line"))

  def part1(
      stream: ZStream[Any, Throwable, String]
  ): ZIO[Any, Throwable, Int] = {
    stream
      .runFold((50, 0)) { case ((curr, count), line) =>
        val direction = line.head
        val step = line.drop(1).toInt

        val diff = if direction == 'R' then step else -step
        val next = curr + diff
        val nextShift = Math.floorMod(next, 100)
        val newCount = if nextShift == 0 then count + 1 else count
        (nextShift, newCount)
      }
      .map { case (curr, count) => count }
  }
  def part2(
      stream: ZStream[Any, Throwable, String]
  ): ZIO[Any, Throwable, Long] = {
    ZIO.succeed(10)
  }
  override def run: ZIO[Any, Any, Any] = {
    for {
      _ <- Console.printLine("--- DAY ONE START ---")
      p1 <- part1(inputStream)
      _ <- Console.printLine(s"Part One solution: $p1")
      p2 <- part2(inputStream)
      _ <- Console.printLine(s"Part Two solution: $p2")

    } yield ()
  }
}
