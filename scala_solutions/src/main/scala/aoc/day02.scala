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

  def task1Filter(number: Long): Boolean = {
    val numberStr = number.toString

    numberStr.length % 2 == 0 && {
      val (left, right) = numberStr.splitAt(numberStr.length / 2)
      left == right
    }
  }

  def task2Filter(number: Long): Boolean = {
    val nrStr = number.toString
    val possibleSplits =
      (1 to nrStr.length / 2).filter(x => nrStr.length % x == 0)

    possibleSplits.exists { k =>
      nrStr.take(k) * (nrStr.length / k) == nrStr
    }
  }

  val inputStream = ZStream
    .fromFileName(InputFile)
    .via(ZPipeline.utf8Decode >>> ZPipeline.splitLines)
    .mapConcat(line => line.split(","))
    .map(parseInput)
    .flatMap { case (start, end) =>
      ZStream.iterate(start)(_ + 1L).takeWhile(_ <= end)
    }
    .filter(task2Filter)

  override def run = {
    for {
      _ <- Console.printLine("--- DAY 2 Start ---")
      p1 <- inputStream.filter(task1Filter).runSum
      _ <- Console.printLine(s"First: $p1")
      p2 <- inputStream.filter(task2Filter).runSum
      _ <- Console.printLine(s"Second: $p2")

    } yield ()
  }
}
