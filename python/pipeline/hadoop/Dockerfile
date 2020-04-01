FROM centos:centos7

RUN yum -y update
RUN yum -y install sudo

# インストール：JDK
RUN yum -y install java-1.8.0-openjdk java-1.8.0-openjdk-devel
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk
ENV PATH $PATH:$JAVA_HOME/bin

# インストール：CDH 5 パッケージ
## CDH 5 をインストールするためには yum リポジトリの登録が必要らしい
RUN rpm --import http://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/RPM-GPG-KEY-cloudera
RUN rpm -ivh http://archive.cloudera.com/cdh5/one-click-install/redhat/6/x86_64/cloudera-cdh-5-0.x86_64.rpm
## 疑似分散モードの設定と YARN を提供するパッケージをインストール
RUN sudo yum -y install hadoop-conf-pseudo

# 起動スクリプトなどをコピーする
ADD scripts scripts

# コマンド実行後もコンテナを起動させ続ける
CMD ["tail", "-f", "/dev/null"]