FROM ubuntu:22.04

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3.6 python3-pip

RUN pip3 install --no-cache-dir -r requirements.txt
RUN opentelemetry-bootstrap -a install

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.server_manual:app", "--host", "0.0.0.0", "--port", "8000"]