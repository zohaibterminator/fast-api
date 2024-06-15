from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {
        'data': 'blog list'
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
def comments(id):
    return {
        'data': {
            'comments': {
                '1',
                '2'
            }
        }
    }