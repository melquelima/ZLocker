from app import app

@app.context_processor
def inject_getattr():
    return dict(getattr=getattr)

@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)