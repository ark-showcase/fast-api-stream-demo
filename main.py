from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

def event_stream():
    # Simulate streaming chunks of data
    for i in range(1, 6):
        yield f"Chunk {i}: Hello from FastAPI stream!\n"
        time.sleep(1)   # Delay simulating long running process

@app.get("/stream")
def stream_response():
    return StreamingResponse(event_stream(), media_type="text/plain")
