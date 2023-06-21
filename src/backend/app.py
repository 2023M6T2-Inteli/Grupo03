import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.battery import router as battery_router
from routers.report import router as report_router
from routers.frames import router as frames_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(battery_router)
app.include_router(report_router)
app.include_router(frames_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)