from typing import Protocol
from typing import TypeVar, Generic, Optional
from sqlalchemy.orm import Session

EntityT = TypeVar("EntityT")  # Generic type for entities

class EntityRepositoryContract(Protocol, Generic[EntityT]):
    db: Session

    def get_by_uuid(self, uuid: str) -> Optional[EntityT]:
        ...

    def add(self, entity: EntityT) -> None:
        ...
