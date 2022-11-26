from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello FastAPI With Continuous Delivery ECR"}

#@app.get('/index')
#def index():
#    return 'Hello world!'

# 博客首页
@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    return {'data': f'blog first page，this is{limit}content，status is {published}，the order is{sort}'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'Here is a list of unpublished blog posts'}

@app.get('/blog/{id}')
def showblog(id: int):
    return {'data': f'This is the id for {id} blog'}

@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': f'This is the id for{id} blog post comments'}

class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool]

@app.post('/blog')
def new_blog(blog: Blog):
    return {'data': f'blog title：{blog.title},blog content：{blog.content},blog status：{blog.published}'}


if __name__ == "__main__":

    uvicorn.run(app, port=8080, host="0.0.0.0")