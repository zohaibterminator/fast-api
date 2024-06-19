from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.get('/blog')
def index(sort: Optional[str]=None, limit=10, published: bool=True): # accepting query parameters
    # only get 10 published blogs
    if published:
        return {
            'data': f'{limit} published blogs from the database'
        }

    return {
        'data': f'{limit} blogs from the database'
    }


@app.get('/blog/unpublished')
def unpublished():
    return {
        'data': 'all unpublished blogs'
    }


# dynamic routing
@app.get('/blog/{id}')
def show(id: int): # pass the id in the function as query parameter
    # fetch blog with id = id
    return {
        'data': id
    }


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {
        'data': {
            'comments': {
                '1',
                '2'
            }
        }
    }


@app.post('/blog')
def create_blog(request: Blog):
    return {
        'data': f'blog is created with title as {request.title}'
    }
    

# optionally, you can change the host and port values
#if __name__ == '__main__':
#    uvicorn.run(app, host='127.0.0.1', port=9000)