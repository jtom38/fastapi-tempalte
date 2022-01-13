from fastapi import FastAPI

app = FastAPI(
    title="APPNAME",
    description="APPDESCRIPTION",
    version="0.0.1"
)

app.include_router()
app.include_router()

@app.on_event('startup')
def startupEvent() -> None:
    pass


@app.on_event('shutdown')
def shutdownEvent() -> None:
    pass