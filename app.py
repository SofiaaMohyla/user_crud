from fastapi import FastAPI

from database import Base, engine
from router import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
