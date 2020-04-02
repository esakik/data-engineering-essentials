#!/usr/bin/env bash

# Execute word count application
sudo -u hdfs hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.16.2.jar \
-input /user/hdfs/input/input.txt -output /user/hdfs/output02 \
-mapper /streaming/python/map.py -reducer /streaming/python/reduce.py

# Show result
sudo -u hdfs hadoop fs -ls /user/hdfs/output02
sudo -u hdfs hadoop fs -cat /user/hdfs/output02/part-*
