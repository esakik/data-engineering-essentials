#!/usr/bin/env bash

# Create input file
echo "apple lemon apple lemon lemon grape" > input.txt

# Put input file
sudo -u hdfs hadoop fs -mkdir -p /user/hdfs/input
sudo -u hdfs hadoop fs -put input.txt /user/hdfs/input

# Execute word count application
sudo -u hdfs hadoop jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount /user/hdfs/input/input.txt /user/hdfs/output

# Show result
sudo -u hdfs hadoop fs -ls /user/hdfs/output
sudo -u hdfs hadoop fs -cat /user/hdfs/output/part-r-00000