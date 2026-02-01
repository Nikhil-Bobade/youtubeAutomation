from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="YouTube DJ Automation API")

# Home route
@app.get("/")
def home():
    return {"status": "DJ API Running 🔥"}

# IMPORTANT: mount router
app.include_router(router)
