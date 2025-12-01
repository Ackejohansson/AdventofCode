ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "3.3.4" // Or your preferred Scala 3 version

lazy val root = (project in file("."))
  .settings(
    name := "aoc-2025",

    // We define the version here to ensure all modules match
    libraryDependencies ++= {
      val zioVersion = "2.1.14" // Use the latest stable version
      Seq(
        "dev.zio" %% "zio" % zioVersion,
        "dev.zio" %% "zio-streams" % zioVersion
      )
    }
  )
