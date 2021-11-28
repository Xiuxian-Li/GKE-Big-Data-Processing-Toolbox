FROM python:latest
COPY . /usr/src/project
WORKDIR /usr/src/project
CMD ["python3","service_direct.py.py"]