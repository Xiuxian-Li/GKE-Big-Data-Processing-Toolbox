FROM python:latest

COPY service_direct.py /.

ENTRYPOINT ["/bin/sleep","7200000"]
CMD ["python","service_direct.py.py"]