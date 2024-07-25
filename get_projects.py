from fastapi import APIRouter, Query
from typing import Optional, List
from pydantic import BaseModel
from datetime import date

router = APIRouter()

class Status(BaseModel):
    name: str
    color: str

class Release(BaseModel):
    id: str
    name: str
    comment: str
    released: date

class Project(BaseModel):
    slug: str
    name: str
    status: Status
    release: Release

class ProjectsResponse(BaseModel):
    page: int
    perPage: int
    count: int
    projects: List[Project]

@router.get("/api/projects", response_model=ProjectsResponse)
async def get_projects(
    status: str = Query(..., description="The status of the projects"),
    page: int = Query(1, ge=1, description="Page number"),
    perPage: int = Query(10, ge=1, description="Number of items per page")
):
    example_project1 = {
        "slug": "pik",
        "name": "ПИК",
        "status": {
            "name": "Новый",
            "color": "#f7f7f7"
        },
        "release": {
            "id": "d44b91df-8061-4047-a51a-dea0c4efbdcf",
            "name": "1",
            "comment": "Планируется после разработки запустить в продакшн первый МВП",
            "released": "2024-09-09"
        }
    }

    example_project2 = {
        "slug": "project-alpha",
        "name": "Alpha",
        "status": {
            "name": "Новый",
            "color": "#f7f7f7"
        },
        "release": {
            "id": "a44b91df-1234-4047-a51a-dea0c4efbdcf",
            "name": "1.0",
            "comment": "Initial release for Alpha project",
            "released": "2024-08-15"
        }
    }
    
    example_project3 = {
        "slug": "project-beta",
        "name": "Beta",
        "status": {
            "name": "В работе",
            "color": "#ffcc00"
        },
        "release": {
            "id": "b34c81ef-2345-4047-b61a-deb0d4efbdcf",
            "name": "2.1",
            "comment": "Beta project second phase",
            "released": "2024-10-10"
        }
    }
    
    example_project4 = {
        "slug": "project-gamma",
        "name": "Gamma",
        "status": {
            "name": "Завершен",
            "color": "#00cc66"
        },
        "release": {
            "id": "c23d72cf-3456-4047-c71a-dec0e4efbdcf",
            "name": "3.0",
            "comment": "Final release of Gamma project",
            "released": "2024-12-01"
        }
    }
    
    example_project5 = {
        "slug": "project-delta",
        "name": "Delta",
        "status": {
            "name": "Новый",
            "color": "#f7f7f7"
        },
        "release": {
            "id": "d12e63bf-4567-4047-d81a-def0f4efbdcf",
            "name": "0.9",
            "comment": "Pre-release for Delta project",
            "released": "2024-07-20"
        }
    }

    if page == 1:
        return ProjectsResponse(
            page=page,
            perPage=perPage,
            count=2,
            projects=[
                example_project1, 
                example_project2,
                example_project3,
                example_project4,
                example_project5,
                example_project1,
                example_project2,
                example_project3,
                example_project4,
                example_project5
            ]
        )
    
    if page == 2:
        return ProjectsResponse(
            page=page,
            perPage=perPage,
            count=2,
            projects=[
                example_project4,
                example_project5
            ]
        )
