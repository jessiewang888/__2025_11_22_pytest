# backend.py
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 允許所有跨域請求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有來源
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有方法（GET, POST, PUT, DELETE 等）
    allow_headers=["*"],  # 允許所有 headers
)

class SubmitRequest(BaseModel):
    name: str = ""

@app.post("/api/greet")
async def api_submit(data: SubmitRequest):
    return {"message": f"Hello, {data.name}!"}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
