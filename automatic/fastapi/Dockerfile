FROM ubuntu:22.04

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3.6 python3-pip

RUN pip install -r requirements.txt
RUN opentelemetry-bootstrap -a install

COPY . .

EXPOSE 8001

# Set environment variables for OpenTelemetry to use the ConsoleSpanExporter
ENV OTEL_TRACES_EXPORTER=console
ENV OTEL_RESOURCE_ATTRIBUTES=service.name=my-fastapi-service-with-automatic-instrumentation

CMD ["opentelemetry-instrument", "uvicorn", "app.server_automatic:app", "--host", "0.0.0.0", "--port", "8001"]
