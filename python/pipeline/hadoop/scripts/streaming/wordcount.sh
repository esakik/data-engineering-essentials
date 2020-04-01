#!/usr/bin/env bash

# Create input file
echo "apple lemon apple lemon lemon grape" > input.txt

# Put input file
sudo -u hdfs hadoop fs -mkdir -p /user/hdfs/streaming/input
sudo -u hdfs hadoop fs -put input.txt /user/hdfs/streaming/input

sudo chmod o+x -R /scripts/streaming/python/

# Execute word count application
sudo -u hdfs hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.16.2.jar \
-input /user/hdfs/streaming/input/input.txt -output /user/hdfs/streaming/output \
-mapper /scripts/streaming/python/map.py -reducer /scripts/streaming/python/reduce.py

# Show result
sudo -u hdfs hadoop fs -ls /user/hdfs/streaming/output
sudo -u hdfs hadoop fs -cat /user/hdfs/streaming/output/part-00000