FROM bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8
ENV HDFS_CONF_dfs_datanode_data_dir=file:///hadoop/dfs/data
RUN mkdir -p /hadoop/dfs/data
VOLUME /hadoop/dfs/data
EXPOSE 9864