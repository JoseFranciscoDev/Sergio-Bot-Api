from typing import Literal
from pydantic import BaseModel, Field


class FiltersSchema(BaseModel):
    limit: int = Field(10, ge=10, le=100)
    page: int = Field(default=1, ge=1)
    order_by: Literal["name", "id"] = "id"


class CreateUserSchema(BaseModel):
    name: str = Field(min_length=4)
    number: str = Field(min_length=11)
