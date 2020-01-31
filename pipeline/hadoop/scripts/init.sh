#!/usr/bin/env bash

# start hdfs process
sudo -u hdfs hdfs namenode -format
sudo service hadoop-hdfs-namenode start
sudo service hadoop-hdfs-datanode start

sudo service hadoop-hdfs-namenode status
sudo service hadoop-hdfs-datanode status

# create directory for map reduce
sudo -u hdfs hadoop fs -mkdir -p /var/lib/hadoop-hdfs/cache/mapred/mapred/staging
sudo -u hdfs hadoop fs -chmod 1777 /var/lib/hadoop-hdfs/cache/mapred/mapred/staging
sudo -u hdfs hadoop fs -chown -R mapred /var/lib/hadoop-hdfs/cache/mapred

# start map reduce process
sudo service hadoop-0.20-mapreduce-jobtracker start
sudo service hadoop-0.20-mapreduce-tasktracker start

sudo service hadoop-0.20-mapreduce-jobtracker status
sudo service hadoop-0.20-mapreduce-tasktracker status