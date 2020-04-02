#!/usr/bin/env bash

# Create input file
echo "apple lemon apple lemon lemon grape" > input.txt

# Put input file to hdfs
sudo -u hdfs hadoop fs -mkdir -p /user/hdfs/input
sudo -u hdfs hadoop fs -put input.txt /user/hdfs/input
