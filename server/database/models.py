from typing import Optional
from sqlmodel import SQLModel, Field

class Asset(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    type: str = Field(max_length=30)
    balance: float = Field()