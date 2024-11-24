from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from src.repository.contacts import ContactRepository
from src.schemas import ContactBase, ContactUpdate
from src.database.models import Contact


class ContactService:
    def __init__(self, db: AsyncSession):
        self.contact_repository = ContactRepository(db)

    async def create_contact(self, body: ContactBase):
        return await self.contact_repository.create_contact(body)

    async def get_contacts(self, skip: int, limit: int, filters: dict):
        return await self.contact_repository.get_contacts(
            skip=skip, limit=limit, filters=filters
        )

    async def get_contact(self, contact_id: int):
        return await self.contact_repository.get_contact_by_id(contact_id)

    async def update_contact(self, contact_id: int, body: ContactUpdate):
        return await self.contact_repository.update_contact(contact_id, body)

    async def remove_contact(self, contact_id: int):
        return await self.contact_repository.remove_contact(contact_id)

    async def get_upcoming_birthdays(self):
        return await self.contact_repository.get_upcoming_birthdays()

    async def update_phone(self, contact_id: int, phone: str) -> Optional[Contact]:
        return await self.contact_repository.update_phone(contact_id, phone)

    async def update_email(self, contact_id: int, email: str) -> Optional[Contact]:
        return await self.contact_repository.update_email(contact_id, email)
