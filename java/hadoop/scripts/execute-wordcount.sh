#!/usr/bin/env bash

# Execute word count application
sudo -u hdfs hadoop jar wc.jar WordCount /user/hdfs/input/input.txt /user/hdfs/output01

# Show result
sudo -u hdfs hadoop fs -ls /user/hdfs/output01
sudo -u hdfs hadoop fs -cat /user/hdfs/output01/part-r-*
