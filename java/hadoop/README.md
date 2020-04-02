# Apache Hadoop
>Learn from [Hadoop徹底入門 第2版 オープンソース分散処理環境の構築](https://www.amazon.co.jp/Hadoop%E5%BE%B9%E5%BA%95%E5%85%A5%E9%96%80-%E7%AC%AC2%E7%89%88-%E3%82%AA%E3%83%BC%E3%83%97%E3%83%B3%E3%82%BD%E3%83%BC%E3%82%B9%E5%88%86%E6%95%A3%E5%87%A6%E7%90%86%E7%92%B0%E5%A2%83%E3%81%AE%E6%A7%8B%E7%AF%89-%E5%A4%AA%E7%94%B0-%E4%B8%80%E6%A8%B9/dp/479812964X/ref=sr_1_1?adgrpid=52706263349&gclid=Cj0KCQiAvc_xBRCYARIsAC5QT9mBAVF-k7HKPnXVgCfSwVbYjraKoQh0zLwJy0fK6Hov2f0msge1i2UaAkXdEALw_wcB&hvadid=338539117825&hvdev=c&hvlocphy=1009265&hvnetw=g&hvqmt=e&hvrand=14163035933253460819&hvtargid=aud-759377471893%3Akwd-335474491915&hydadcr=27263_11561109&jp-ad-ap=0&keywords=pipeline.hadoop%E5%BE%B9%E5%BA%95%E5%85%A5%E9%96%80&qid=1580488552&sr=8-1).

## Hadoop Start-up
```bash
# build docker image
$ make build

# run docker container
$ make run

# start hadoop
[root@xxxxxxxxx /]# ./scripts/start-hadoop.sh
```

## Execute MapReduce Sample
```bash
# compile WordCount.java and make jar
[root@xxxxxxxxx /]# ./scripts/make-jar.sh

# create input for WordCount.java
[root@xxxxxxxxx /]# ./scripts/create-input-text.sh

# execute WordCount.java
[root@xxxxxxxxx /]# ./scripts/execute-wordcount.sh
```
