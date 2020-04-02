#!/usr/bin/env bash

# Compile WordCount.java
hadoop com.sun.tools.javac.Main WordCount.java

# Make jar
jar cf wc.jar WordCount*.class
