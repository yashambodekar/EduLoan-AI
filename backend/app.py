from fastapi import FastAPI

from routes.predict_routes import (
    router as predict_router
)

from routes.emi_routes import (
    router as emi_router
)

app = FastAPI()

app.include_router(
    predict_router
)
app.include_router(
    emi_router
)


@app.get("/")
def home():

    return {
        "message":
        "EduLoan AI Running"
    }