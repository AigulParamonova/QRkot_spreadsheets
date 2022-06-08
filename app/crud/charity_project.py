from typing import Optional, List, Dict, Any

from sqlalchemy import select, extract
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        ''''''
        project_name = await session.execute(
            select(CharityProject).where(
                CharityProject.name == project_name
            )
        )
        project_name = project_name.scalars().first()
        return project_name

    async def get_projects_by_completion_rate(
        self,
        session: AsyncSession()
    ) -> List[Dict[str, Any]]:
        '''Возвращает все завершённые проекты.'''
        projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested
            ).order_by(
                extract('year', self.model.close_date) -
                extract('year', self.model.create_date),
                extract('month', self.model.close_date) -
                extract('month', self.model.create_date),
                extract('day', self.model.close_date) -
                extract('day', self.model.create_date)
            )
        )
        projects = projects.all()
        return projects


charity_project_crud = CRUDCharityProject(CharityProject)