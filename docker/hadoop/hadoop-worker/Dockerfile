FROM bde2020/hadoop-base:2.0.0-hadoop3.2.1-java8

HEALTHCHECK CMD curl -f http://localhost:9864/ || exit 1

ENV CLUSTER_NAME=project-toolbox
ENV HDFS_CONF_dfs_datanode_data_dir=file:///hadoop/dfs/data

ENV CORE_CONF_fs_defaultFS=hdfs://namenode:9000
ENV CORE_CONF_hadoop_http_staticuser_user=root
ENV CORE_CONF_hadoop_proxyuser_hue_hosts=*
ENV CORE_CONF_hadoop_proxyuser_hue_groups=*
ENV CORE_CONF_io_compression_codecs=org.apache.hadoop.io.compress.SnappyCodec

ENV HDFS_CONF_dfs_permissions_enabled=false
ENV HDFS_CONF_dfs_webhdfs_enabled=true
ENV HDFS_CONF_dfs_namenode_datanode_registration_ip___hostname___check=false

RUN mkdir -p /hadoop/dfs/data
VOLUME /hadoop/dfs/data

EXPOSE 9864