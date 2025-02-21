from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import asyncio

app = FastAPI()

# Define request body model
class FallDetectionRequest(BaseModel):
    fall_detection: bool

# Global variable to store the status
status = False

@app.post("/fallDetection/")
async def fall_detection_api(data: FallDetectionRequest, background_tasks: BackgroundTasks):
    global status
    if data.fall_detection:
        status = True
        # Schedule a task to reset the status after 10 seconds
        background_tasks.add_task(reset_status)
        return {"message": "Fall detected!", "status": "Alert"}
    else:
        return {"message": "No fall detected", "status": "Safe"}

@app.get("/status/")
async def get_status():
    global status
    return {"status": status}

async def reset_status():
    await asyncio.sleep(10)
    global status
    status = False

# Run the server using: uvicorn main:app --reload