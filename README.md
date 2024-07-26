# OpenTelemetry Collector Core Distro

This distribution contains all the components from the [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector) repository and a small selection of components tied to open source projects from the [OpenTelemetry Collector Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib) repository.

This distribution is considered "classic" and is no longer accepting new components outside of components from the Core repo.

## Components

The full list of components is available in the [manifest](manifest.yaml)

### Rules for Component Inclusion

Since Core is a "classic" distribution its components are strictly limited to what currently exists in its [manifest](manifest.yaml) and any future components in Core.
No other components from Contrib should be added.

## Commands

### Docker Network 
```
docker network create opentelemetry-network
```

### Manual Application
```
cd manual/fastapi
docker build -t fastapi-manual . -f Dockerfile --no-cache
docker run -it -d --name fastapi-manual -p 8000:8000 --network opentelemetry-network fastapi-manual
```

### Automatic Application - Without Collector
```
cd automatic/fastapi
docker build -t fastapi-automatic . -f Dockerfile --no-cache
docker run -it -d --name fastapi-automatic -p 8001:8001 --network opentelemetry-network fastapi-automatic
```

### Automatic Application - With Collector
```
cd automatic/fastapi
docker build -t fastapi-automatic-collector . -f Dockerfile_collector --no-cache
docker run -it -d --add-host localhost:<collector IP> --name fastapi-automatic-collector -p 8002:8002 --network opentelemetry-network fastapi-automatic-collector
```

| Note: To get the Collector IP you can inspect the container: `docker inspect <Container ID>`
### OTLP Collector
```
cd collector
docker run -it -d -p 4317:4317 --network opentelemetry-network \
    --name otel-collector \
    -v otel-collector-config.yaml:/etc/otel-collector-config.yaml \
    otel/opentelemetry-collector:latest \
    --config=/etc/otel-collector-config.yaml
```
