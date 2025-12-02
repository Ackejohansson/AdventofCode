package aoc

import zio.{ZIOAppDefault, ZIO, Console}
import zio.stream.ZStream
import zio.stream.ZPipeline
import zio.stream.ZStreamProvideMacro

object Day02 extends ZIOAppDefault {
  private val InputFile = "../inputs/day02.csv"

  def parseInput(row: String): (Long, Long) = {
    row.split("-") match {
      case Array(start, end) => (start.toLong, end.toLong)
      case _                 => throw new RuntimeException(s"BAD INPUT")
    }
  }
  def filterDuplicates(number: Long): Boolean = {
    val numberStr = number.toString
    if (numberStr.length % 2 != 0) return false
    val splitIndex = numberStr.length / 2
    val nr = numberStr.splitAt(splitIndex)
    nr(0) == nr(1)
  }

  val inputStream = ZStream
    .fromFileName(InputFile)
    .via(ZPipeline.utf8Decode >>> ZPipeline.splitLines)
    .mapConcat(line => line.split(","))
    .map(parseInput)
    .flatMap { case (start, end) =>
      ZStream.iterate(start)(_ + 1L).takeWhile(_ <= end)
    }
    .filter(filterDuplicates)

  override def run = {
    for {
      _ <- Console.printLine("--- DAY 2 Start ---")
      p1 <- inputStream.tap(line => ZIO.debug(s"Line: $line")).runSum
      _ <- Console.printLine(s"Solution: $p1")
    } yield ()
  }
}
