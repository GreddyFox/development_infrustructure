from pydantic import BaseModel

class User(BaseModel):
    username: str
    lastname: str
    firstname: str
