FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["service_direct.py"]
ENTRYPOINT ["python3"]