from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/blog')
def index(sort: Optional(str)=None, limit=10, published: bool=True): # accepting query parameters
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
def show(id: int): # pass the id in the function
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
def create_blog():
    return {
        'data': 'blog is created'
    }