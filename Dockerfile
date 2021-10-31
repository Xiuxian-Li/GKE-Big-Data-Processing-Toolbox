FROM ubuntu
MAINTAINER Xiuxian Li
RUN apt-get update
RUN apt-get install -y python3
ADD service_direct.py /app/service_direct.py
CMD ["/app/service_direct.py"]
ENTRYPOINT ["python3"]