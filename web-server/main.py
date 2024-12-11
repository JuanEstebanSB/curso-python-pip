import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/items/", response_class=HTMLResponse)
@app.get('/')
def  get_list():
    return [1,2,3]


@app.get('/html', response_class=HTMLResponse)
def get_list():
    return """
            <h1> Hola soy Esteban </h1>
            <p></p>
"""


@app.get('/contact')
def get_list():
    return {'name': 'Esteban'}

def run():
    store.get_categories()

if __name__ == '__main__':
    run()

