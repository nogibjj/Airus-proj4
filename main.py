from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello FastAPI With Continuous Delivery ECR"}

@app.get('/index')
def index():
    return 'Hello world!'


if __name__ == "__main__":

    uvicorn.run(app, port=8080, host="0.0.0.0")