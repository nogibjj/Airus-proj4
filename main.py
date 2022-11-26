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
    return {'data': f'我是博客首页，显示{limit}篇内容，并且发布状态为{published}，排序顺序是根据{sort}字段'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': '这里是没有发布的博文列表'}

@app.get('/blog/{id}')
def showblog(id: int):
    return {'data': f'这是id为 {id} 的博文'}

@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': f'这是id为{id}的博文评论内容'}

class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool]

@app.post('/blog')
def new_blog(blog: Blog):
    return {'data': f'博文标题：{blog.title},博文内容：{blog.content},博文发表状态：{blog.published}'}


if __name__ == "__main__":

    uvicorn.run(app, port=8080, host="0.0.0.0")