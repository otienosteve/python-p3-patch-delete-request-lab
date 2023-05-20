from fastapi import FastAPI

app = FastAPI()

@app.patch('/partial_update')
def partial_update():
    pass