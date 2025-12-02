package aoc

import zio.{ZIOAppDefault, ZIO, Console}
import zio.stream.ZStream
import zio.stream.ZPipeline
import java.io.InputStream

object Day02 extends ZIOAppDefault {
  private val InputFile = "../inputs/day02.csv"

  def parseInput(row: String): (Long, Long) = {
    row.split("-") match {
      case Array(start, end) => (start.toLong, end.toLong)
      case _                 => throw new RuntimeException(s"BAD INPUT")
    }
  }

  val task1Filter: Long => Boolean = number => {
    val numberStr = number.toString
    numberStr.length % 2 == 0 && {
      val (left, right) = numberStr.splitAt(numberStr.length / 2)
      left == right
    }
  }

  val task2Filter: Long => Boolean = (number) => {
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

  def toIds(
      stream: ZStream[Any, Throwable, String]
  ): ZStream[Any, Throwable, Long] = {
    stream
      .mapConcat(line => line.split(","))
      .map(parseInput)
      .flatMap { case (start, end) =>
        ZStream.iterate(start)(_ + 1L).takeWhile(_ <= end)
      }
  }

  def solve(
      stream: ZStream[Any, Throwable, Long],
      rule: Long => Boolean
  ): ZIO[Any, Throwable, Long] = {
    stream.filter(rule).runSum
  }
  override def run = {
    val idStream = toIds(inputStream)

    for {
      _ <- Console.printLine("--- DAY 2 Start ---")

      p1 <- solve(idStream, task1Filter)
      _ <- Console.printLine(s"First: $p1")

      p2 <- solve(idStream, task2Filter)
      _ <- Console.printLine(s"Second: $p2")
    } yield ()
  }
}
