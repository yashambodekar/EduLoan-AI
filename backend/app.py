from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.predict_routes import (
    router as predict_router
)

from routes.emi_routes import (
    router as emi_router
)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

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