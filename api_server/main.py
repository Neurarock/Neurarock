from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from auth import verify_api_key
from meshy_client import generate_meshy_3d

app = FastAPI()

class GenerateRequest(BaseModel):
    model: str
    prompt: str

@app.post("/generate_3d_model")
async def generate_3d_model(req: GenerateRequest, x_api_key: str = Header(...)):
    if not verify_api_key(x_api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")

    if req.model != "meshy":
        raise HTTPException(status_code=400, detail="Unsupported model")

    model_url = await generate_meshy_3d(req.prompt)
    return {"model_url": model_url}
