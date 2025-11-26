lazy val root = project
  .in(file("."))
  .settings(
    name := "aoc-scala-learning",
    version := "0.1.0-SNAPSHOT",

    // We put the version directly here to avoid the "not found" error
    scalaVersion := "3.3.6",
    libraryDependencies ++= Seq(
      "com.lihaoyi" %% "os-lib" % "0.9.3",
      "org.scalatest" %% "scalatest" % "3.2.17" % Test
    )
  )
