from uuid import UUID

from pydantic import BaseModel

#-------------workaround for hashing-------------------
class MyBaseModel(BaseModel):
    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))

class UserResponse(BaseModel):
    id: UUID
    username: str
    email: str 
    first_name: str | None
    last_name: str | None
    nationally: str | None
    bio: str | None

    class Config:
        orm_mode = True


class PublicUserResponse(BaseModel):
    username: str
    first_name: str

    class Config:
        orm_mode = True


class UserCreateRequest(BaseModel):
    email: str
    username: str
    password: str


class UserUpdateRequest(BaseModel):
    first_name: str | None
    last_name: str | None
    nationally: str | None
    bio: str | None
    email: str | None


class UserLoginResponse(BaseModel):
    access_token: str


class UserLoginRequest(MyBaseModel):
    username: str
    password: str
