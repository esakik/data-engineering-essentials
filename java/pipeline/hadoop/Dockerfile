FROM centos:centos7

RUN yum -y update
RUN yum -y install sudo

# インストール：JDK
RUN yum -y install java-1.8.0-openjdk java-1.8.0-openjdk-devel

# 環境変数の設定（コンパイルの際に必要）
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk
ENV PATH $PATH:$JAVA_HOME/bin
# tools.jar：javac コンパイラを含む
ENV HADOOP_CLASSPATH $JAVA_HOME/lib/tools.jar

# インストール：CDH 5 パッケージ
## CDH 5 をインストールするためには yum リポジトリの登録が必要らしい
RUN rpm --import http://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/RPM-GPG-KEY-cloudera
RUN rpm -ivh http://archive.cloudera.com/cdh5/one-click-install/redhat/6/x86_64/cloudera-cdh-5-0.x86_64.rpm
## 疑似分散モードの設定と YARN を提供するパッケージをインストール
RUN yum -y install hadoop-conf-pseudo

ADD main main
RUN chmod +x -R main

WORKDIR main

# コマンド実行後もコンテナを起動させ続ける
CMD ["tail", "-f", "/dev/null"]
