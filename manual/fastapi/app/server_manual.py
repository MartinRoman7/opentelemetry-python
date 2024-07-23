from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (BatchSpanProcessor, ConsoleSpanExporter)

app = FastAPI()

# Setup OpenTelemetry Tracer
resource = Resource(attributes={
    "service.name": "my-fastapi-service-with-manual-instrumentation"
})

tracer_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer_provider)

# Setup Console exporter
console_exporter = ConsoleSpanExporter()
span_processor = BatchSpanProcessor(console_exporter)
tracer_provider.add_span_processor(span_processor)

FastAPIInstrumentor.instrument_app(app, tracer_provider=tracer_provider)

@app.get("/message")
async def get_message():
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("get_message_span"):
        return {"message": "Hello, this is your message with Manual Instrumentation using Opentelemetry!"}
