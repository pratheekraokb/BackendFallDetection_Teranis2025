from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define request body model
class FallDetectionRequest(BaseModel):
    fall_detection: bool

@app.post("/fallDetection/")
async def fall_detection_api(data: FallDetectionRequest):
    if data.fall_detection:
        return {"message": "Fall detected!", "status": "Alert"}
    else:
        return {"message": "No fall detected", "status": "Safe"}

# Run the server using: uvicorn main:app --reload
