from fastapi import APIRouter, HTTPException, Path
from pydantic import BaseModel
from typing import List

router = APIRouter()


class Status(BaseModel):
    id: str
    name: str
    color: str


class Release(BaseModel):
    id: str
    name: str
    comment: str
    released: str


class Responsible(BaseModel):
    id: str
    fullName: str
    team: str


class Section(BaseModel):
    id: str
    name: str


class Project(BaseModel):
    slug: str
    name: str
    status: Status
    statuses: List[Status]
    releases: List[Release]
    responsibles: List[Responsible]
    sections: List[Section]


@router.get("/api/projects/{slug}", response_model=Project)
async def get_project(slug: str = Path(..., description="The slug of the project")):
    example_project1 = {
        "slug": "pik",
        "name": "ПИК",
        "status": {"id": "new", "name": "Новый", "color": "#f7f7f7"},
        "statuses": [
            {
                "id": "1fda60fc-2348-4193-96df-ac1c1fa1f573",
                "name": "Backlog",
                "color": "#f7f7f7",
            },
            {
                "id": "6a4ae617-1155-42d3-ba0a-a14f9619a965",
                "name": "Подготовка информации",
                "color": "#f7f7f7",
            },
            {
                "id": "c91f5e8c-02c6-4d37-886f-86aaad40aa76",
                "name": "Разработка",
                "color": "#f7f7f7",
            },
            {
                "id": "23b47812-eec8-4219-b6df-e445148e6362",
                "name": "Бизнес-ревью",
                "color": "#f7f7f7",
            },
            {
                "id": "f4d9f946-b0da-4f3a-b79e-57cfe879d414",
                "name": "Готово к релизному тестированию",
                "color": "#f7f7f7",
            },
            {
                "id": "6b3efd57-5f8f-4cc6-b9ae-0d694e008d2d",
                "name": "Подготовлены тест-кейсы",
                "color": "#f7f7f7",
            },
            {
                "id": "982ed361-e4a6-4721-be69-69373b4ae1f3",
                "name": "Проверка по тест-кейсам",
                "color": "#f7f7f7",
            },
            {
                "id": "2bbb0413-b29a-4a10-83f9-ce5420a8dd0f",
                "name": "Задача завершена",
                "color": "#f7f7f7",
            },
        ],
        "releases": [
            {
                "id": "d44b91df-8061-4047-a51a-dea0c4efbdcf",
                "name": "1",
                "comment": "Планируется после разработки запустить в продакшн первый МВП",
                "released": "2024-09-09",
            },
            {
                "id": "d44b91df-8061-4047-a51a-dea0c4efbdc323f",
                "name": "2",
                "comment": "Планируется после разработки запустить в продакшн первый МВП",
                "released": "2024-09-09",
            },
        ],
        "responsibles": [
            {
                "id": "694a251e-caea-43be-936f-aa4efbd49de3",
                "fullName": "Иванов Иван Иванович",
                "team": "client",
            },
            {
                "id": "694a251e-caea-43be-936f-233efbd49de3",
                "fullName": "Андреев Андрей Андреевич",
                "team": "dev",
            },
        ],
        "sections": [
            {"id": "b1385765-aec3-40cd-a8e8-1308bf51a65d", "name": "Каталог"},
            {"id": "12345678-ijkl-mnop-qrst-1234567890gh", "name": "Тестовый раздел"},
        ],
    }

    example_project2 = {
        "slug": "project-alpha",
        "name": "Alpha",
        "status": {"id": "new", "name": "Новый", "color": "#f7f7f7"},
        "statuses": [
            {
                "id": "1fda60fc-2348-4193-96df-ac1c1fa1f573",
                "name": "Backlog",
                "color": "#f7f7f7",
            },
            {
                "id": "6a4ae617-1155-42d3-ba0a-a14f9619a965",
                "name": "Подготовка информации",
                "color": "#f7f7f7",
            },
            {
                "id": "c91f5e8c-02c6-4d37-886f-86aaad40aa76",
                "name": "Разработка",
                "color": "#f7f7f7",
            },
            {
                "id": "23b47812-eec8-4219-b6df-e445148e6362",
                "name": "Бизнес-ревью",
                "color": "#f7f7f7",
            },
            {
                "id": "f4d9f946-b0da-4f3a-b79e-57cfe879d414",
                "name": "Готово к релизному тестированию",
                "color": "#f7f7f7",
            },
            {
                "id": "6b3efd57-5f8f-4cc6-b9ae-0d694e008d2d",
                "name": "Подготовлены тест-кейсы",
                "color": "#f7f7f7",
            },
            {
                "id": "982ed361-e4a6-4721-be69-69373b4ae1f3",
                "name": "Проверка по тест-кейсам",
                "color": "#f7f7f7",
            },
            {
                "id": "2bbb0413-b29a-4a10-83f9-ce5420a8dd0f",
                "name": "Задача завершена",
                "color": "#f7f7f7",
            },
        ],
        "releases": [
            {
                "id": "a44b91df-1234-4047-a51a-dea0c4efbdcf",
                "name": "1.0",
                "comment": "Initial release for Alpha project",
                "released": "2024-08-15",
            }
        ],
        "responsibles": [
            {
                "id": "12345678-abcd-efgh-ijkl-1234567890ab",
                "fullName": "Alex",
                "team": "backend",
            }
        ],
        "sections": [
            {"id": "09876543-zyxw-vuts-rqpo-0987654321cd", "name": "User Management"}
        ],
    }

    example_project3 = {
        "slug": "project-beta",
        "name": "Beta",
        "status": {"id": "in-progress", "name": "В работе", "color": "#ffcc00"},
        "statuses": [
            {
                "id": "1fda60fc-2348-4193-96df-ac1c1fa1f573",
                "name": "Backlog",
                "color": "#f7f7f7",
            },
            {
                "id": "6a4ae617-1155-42d3-ba0a-a14f9619a965",
                "name": "Подготовка информации",
                "color": "#f7f7f7",
            },
            {
                "id": "c91f5e8c-02c6-4d37-886f-86aaad40aa76",
                "name": "Разработка",
                "color": "#f7f7f7",
            },
            {
                "id": "23b47812-eec8-4219-b6df-e445148e6362",
                "name": "Бизнес-ревью",
                "color": "#f7f7f7",
            },
            {
                "id": "f4d9f946-b0da-4f3a-b79e-57cfe879d414",
                "name": "Готово к релизному тестированию",
                "color": "#f7f7f7",
            },
            {
                "id": "6b3efd57-5f8f-4cc6-b9ae-0d694e008d2d",
                "name": "Подготовлены тест-кейсы",
                "color": "#f7f7f7",
            },
            {
                "id": "982ed361-e4a6-4721-be69-69373b4ae1f3",
                "name": "Проверка по тест-кейсам",
                "color": "#f7f7f7",
            },
            {
                "id": "2bbb0413-b29a-4a10-83f9-ce5420a8dd0f",
                "name": "Задача завершена",
                "color": "#f7f7f7",
            },
        ],
        "releases": [
            {
                "id": "b34c81ef-2345-4047-b61a-deb0d4efbdcf",
                "name": "2.1",
                "comment": "Beta project second phase",
                "released": "2024-10-10",
            }
        ],
        "responsibles": [
            {
                "id": "98765432-abcd-efgh-ijkl-0987654321ef",
                "fullName": "Maria",
                "team": "frontend",
            }
        ],
        "sections": [
            {"id": "87654321-hijk-lmno-pqrs-876543210fed", "name": "Analytics"}
        ],
    }

    example_project4 = {
        "slug": "project-gamma",
        "name": "Gamma",
        "status": {"id": "completed", "name": "Завершен", "color": "#00cc66"},
        "statuses": [
            {
                "id": "1fda60fc-2348-4193-96df-ac1c1fa1f573",
                "name": "Backlog",
                "color": "#f7f7f7",
            },
            {
                "id": "6a4ae617-1155-42d3-ba0a-a14f9619a965",
                "name": "Подготовка информации",
                "color": "#f7f7f7",
            },
            {
                "id": "c91f5e8c-02c6-4d37-886f-86aaad40aa76",
                "name": "Разработка",
                "color": "#f7f7f7",
            },
            {
                "id": "23b47812-eec8-4219-b6df-e445148e6362",
                "name": "Бизнес-ревью",
                "color": "#f7f7f7",
            },
            {
                "id": "f4d9f946-b0da-4f3a-b79e-57cfe879d414",
                "name": "Готово к релизному тестированию",
                "color": "#f7f7f7",
            },
            {
                "id": "6b3efd57-5f8f-4cc6-b9ae-0d694e008d2d",
                "name": "Подготовлены тест-кейсы",
                "color": "#f7f7f7",
            },
            {
                "id": "982ed361-e4a6-4721-be69-69373b4ae1f3",
                "name": "Проверка по тест-кейсам",
                "color": "#f7f7f7",
            },
            {
                "id": "2bbb0413-b29a-4a10-83f9-ce5420a8dd0f",
                "name": "Задача завершена",
                "color": "#f7f7f7",
            },
        ],
        "releases": [
            {
                "id": "c23d72cf-3456-4047-c71a-dec0e4efbdcf",
                "name": "3.0",
                "comment": "Final release of Gamma project",
                "released": "2024-12-01",
            }
        ],
        "responsibles": [
            {
                "id": "abcdef12-3456-7890-abcd-ef1234567890",
                "fullName": "John",
                "team": "devops",
            }
        ],
        "sections": [
            {"id": "12345678-ijkl-mnop-qrst-1234567890gh", "name": "Integration"}
        ],
    }

    example_project5 = {
        "slug": "project-delta",
        "name": "Delta",
        "status": {"id": "new", "name": "Новый", "color": "#f7f7f7"},
        "statuses": [
            {
                "id": "1fda60fc-2348-4193-96df-ac1c1fa1f573",
                "name": "Backlog",
                "color": "#f7f7f7",
            },
            {
                "id": "6a4ae617-1155-42d3-ba0a-a14f9619a965",
                "name": "Подготовка информации",
                "color": "#f7f7f7",
            },
            {
                "id": "c91f5e8c-02c6-4d37-886f-86aaad40aa76",
                "name": "Разработка",
                "color": "#f7f7f7",
            },
            {
                "id": "23b47812-eec8-4219-b6df-e445148e6362",
                "name": "Бизнес-ревью",
                "color": "#f7f7f7",
            },
            {
                "id": "f4d9f946-b0da-4f3a-b79e-57cfe879d414",
                "name": "Готово к релизному тестированию",
                "color": "#f7f7f7",
            },
            {
                "id": "6b3efd57-5f8f-4cc6-b9ae-0d694e008d2d",
                "name": "Подготовлены тест-кейсы",
                "color": "#f7f7f7",
            },
            {
                "id": "982ed361-e4a6-4721-be69-69373b4ae1f3",
                "name": "Проверка по тест-кейсам",
                "color": "#f7f7f7",
            },
            {
                "id": "2bbb0413-b29a-4a10-83f9-ce5420a8dd0f",
                "name": "Задача завершена",
                "color": "#f7f7f7",
            },
        ],
        "releases": [
            {
                "id": "d12e63bf-4567-4047-d81a-def0f4efbdcf",
                "name": "0.9",
                "comment": "Pre-release for Delta project",
                "released": "2024-07-20",
            }
        ],
        "responsibles": [
            {
                "id": "11223344-aabb-ccdd-eeff-112233445566",
                "fullName": "Alice",
                "team": "qa",
            }
        ],
        "sections": [
            {"id": "22334455-6677-8899-aabb-223344556677", "name": "Documentation"}
        ],
    }

    projects = {
        "pik": example_project1,
        "project-alpha": example_project2,
        "project-beta": example_project3,
        "project-gamma": example_project4,
        "project-delta": example_project5,
    }

    if slug not in projects:
        raise HTTPException(status_code=404, detail="Project not found")

    return projects[slug]
