from typing import Optional
from sqlmodel import SQLModel, Field

class Asset(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    type: str = Field(max_length=30)
    balance: float = Field()
   
class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    email: str = Field(unique=True, max_length=255)
    hashed_password: str = Field(max_length=255)