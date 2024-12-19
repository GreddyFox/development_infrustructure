from fastapi import FastAPI
import uvicorn

import database
from model import User

app = FastAPI()


@app.post("/user/create")
async def create_user(user: User):
    cursor = database.get_cursor()
    cursor.execute(
        "insert into users(username, firstname, lastname) "
        "values (%s, %s, %s);",
        (user.username, user.lastname, user.firstname))
    return user


@app.get("/users")
async def get_users():
    cursor = database.get_cursor()
    cursor.execute("select * from users;")
    return cursor.fetchall()


@app.get("/user/{username}")
async def get_user(username: str):
    cursor = database.get_cursor()
    cursor.execute(
        "select * "
        "from users "
        "where users.username = %s;",
        (username, )
    )
    return cursor.fetchall()


if __name__ == '__main__':
    uvicorn.run(app, host="db", port=8001)