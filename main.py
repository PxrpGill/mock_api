from fastapi import FastAPI
from get_tasks import router as tasks_router
from get_projects import router as projects_router
from get_project import router as project_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(tasks_router)
app.include_router(project_router)
app.include_router(projects_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает запросы с любых источников
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все HTTP-методы
    allow_headers=["*"],  # Разрешает все заголовки
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
