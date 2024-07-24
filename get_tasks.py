from fastapi import APIRouter, Query, Path
from typing import Optional, List
from pydantic import BaseModel
from datetime import date

router = APIRouter()

class Status(BaseModel):
    id: str
    name: str
    color: str

class Event(BaseModel):
    id: str
    responsible: str
    comment: str
    risk: str
    type: str
    startedAt: date
    endedAt: date

class Task(BaseModel):
    id: str
    name: str
    comment: str
    section: str
    release: str
    status: Status
    events: List[Event]

class TasksResponse(BaseModel):
    page: int
    perPage: int
    count: int
    tasks: List[Task]

@router.get("/api/project/{slug}/tasks", response_model=TasksResponse)
async def get_tasks(
    slug: str = Path(..., description="The slug of the project"),
    page: int = Query(1, ge=1, description="Page number"),
    perPage: int = Query(10, ge=1, description="Number of items per page"),
    responsible: Optional[List[str]] = Query(None, description="List of responsible IDs"),
    release: Optional[List[str]] = Query(None, description="List of release IDs"),
    section: Optional[List[str]] = Query(None, description="List of section IDs")
):
    
    example_task1 = {
        "id": "8f7e8563-5681-4441-a776-e76f4d8e1224",
        "name": "Атрибуты (детальная страница + список в каталоге)",
        "comment": "Задержка из-за отсутствия оплат, подписанных актов, решение орг. вопросов",
        "section": "b1385765-aec3-40cd-a8e8-1308bf51a65d",
        "release": "d44b91df-8061-4047-a51a-dea0c4efbdcf",
        "status": {
            "id": "2bbb0413-b29a-4a10-83f9-ce5420a8dd0f",
            "name": "Задача завершена",
            "color": "#f7f7f7"
        },
        "events": [
            {
                "id": "65354087-f3b4-4864-a76c-756fdce3ee1f",
                "responsible": "694a251e-caea-43be-936f-aa4efbd49de3",
                "comment": "Не получили ответ от коллег",
                "risk": "done",
                "type": "transfer",
                "startedAt": "2024-09-10",
                "endedAt": "2024-09-11"
            }
        ]
    }
    
    example_task2 = {
        "id": "7a5d3821-2a68-43a1-ba36-024a09d18fa1",
        "name": "Оптимизация производительности API",
        "comment": "Необходимо ускорить ответы от API до 2 секунд",
        "section": "b1385765-aec3-40cd-a8e8-1308bf51a65d",
        "release": "a44b91df-1234-4047-a51a-dea0c4efbdcf",
        "status": {
            "id": "982ed361-e4a6-4721-be69-69373b4ae1f3",
            "name": "Проверка по тест-кейсам",
            "color": "#f7f7f7"
        },
        "events": [
            {
                "id": "12345678-abcd-9876-ijkl-abcdef123456",
                "responsible": "98765432-abcd-efgh-ijkl-0987654321ef",
                "comment": "Найдены узкие места в коде, требуется рефакторинг",
                "risk": "high",
                "type": "bugfix",
                "startedAt": "2024-08-20",
                "endedAt": "2024-08-21"
            },
            {
                "id": "56789012-efgh-3456-mnop-7890abcdef12",
                "responsible": "11223344-aabb-ccdd-eeff-112233445566",
                "comment": "Тестирование оптимизаций на стенде среды",
                "risk": "medium",
                "type": "testing",
                "startedAt": "2024-08-22",
                "endedAt": "2024-08-23"
            }
        ]
    }
    
    example_task3 = {
        "id": "1b2c3d4e-5f6a-7b8c-d9e0-f1a2b3c4d5e6",
        "name": "Интеграция с внешними системами",
        "comment": "Необходимо согласовать форматы данных с партнерами",
        "section": "12345678-ijkl-mnop-qrst-1234567890gh",
        "release": "c23d72cf-3456-4047-c71a-dec0e4efbdcf",
        "status": {
            "id": "1fda60fc-2348-4193-96df-ac1c1fa1f573",
            "name": "Backlog",
            "color": "#f7f7f7"
        },
        "events": []
    }

    return TasksResponse(
        page=page,
        perPage=perPage,
        count=120,
        tasks=[
            example_task1,
            example_task2,
            example_task3
        ]
    )
