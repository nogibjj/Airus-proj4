from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()


class Wiki(BaseModel):
    name: str


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello FastAPI With Continuous Delivery ECR"}




if __name__ == "__main__":

    uvicorn.run(app, port=8080, host="0.0.0.0")