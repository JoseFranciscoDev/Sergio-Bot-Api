from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict, Field


class FiltersSchema(BaseModel):
    limit: int = Field(10, ge=10, le=100)
    page: int = Field(default=1, ge=1)
    order_by: Literal["name", "id"] = "id"


class CreateUserSchema(BaseModel):
    name: str = Field(min_length=4)
    number: str = Field(min_length=11)


class UpdateUserSchema(BaseModel):
    name: Optional[str] = Field(None, min_length=4)
    number: Optional[str] = Field(None, min_length=11)
    saldo: Optional[int] = Field(None, ge=0)


class UserResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    number: str
    saldo: int
    is_active: bool
