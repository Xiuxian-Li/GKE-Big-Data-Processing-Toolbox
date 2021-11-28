FROM bde2020/hadoop-base:2.0.0-hadoop3.2.1-java8

HEALTHCHECK CMD curl -f http://localhost:9870/ || exit 1

# env for name node
ENV CLUSTER_NAME=project-toolbox
ENV HDFS_CONF_dfs_namenode_name_dir=file:///hadoop/dfs/name

ENV CORE_CONF_fs_defaultFS=hdfs://namenode:9000
ENV CORE_CONF_hadoop_http_staticuser_user=root
ENV CORE_CONF_hadoop_proxyuser_hue_hosts=*
ENV CORE_CONF_hadoop_proxyuser_hue_groups=*
ENV CORE_CONF_io_compression_codecs=org.apache.hadoop.io.compress.SnappyCodec

ENV HDFS_CONF_dfs_permissions_enabled=false
ENV HDFS_CONF_dfs_webhdfs_enabled=true
ENV HDFS_CONF_dfs_namenode_datanode_registration_ip___hostname___check=false

RUN mkdir -p /hadoop/dfs/name
VOLUME /hadoop/dfs/name

EXPOSE 9000

