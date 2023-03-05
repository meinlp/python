from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health(arg: str):
    if arg:
        return f'All seems OK {arg}'
    else:
        return 'All seems OK'
