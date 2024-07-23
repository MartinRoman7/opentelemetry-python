FROM ubuntu:22.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3.6 python3-pip

RUN pip install opentelemetry-distro opentelemetry-exporter-otlp 
RUN pip install flask requests
RUN opentelemetry-bootstrap -a install

COPY . .
CMD ["python", "server_manual.py"]