# Домашнее задание по теме "Основы Fast Api и маршрутизация"
# Цель: научиться создавать базовую маршрутизацию для обработки данных в FastAPI.
#
# Задача "Начало пути":
# Подготовка:
# Установите фреймворк FastAPI при помощи пакетного менеджера pip. Версию Python можете выбрать самостоятельно (3.9 - 3.12).
#
# Маршрутизация:
# Создайте приложение(объект) FastAPI предварительно импортировав класс для него.


from fastapi import FastAPI
app = FastAPI()

# 2.Создайте маршрут к главной странице - "/". По нему должно выводиться сообщение "Главная страница".
@app.get("/")
async def welcome() -> dict:
    return {"mesage": "ГЛАВНАЯ СТРАНИЦА"}

# # 3.Создайте маршрут к странице администратора - "/user/admin". По нему должно выводиться сообщение "Вы вошли как администратор".
@app.get("/user/admin")
async def welcome() -> dict:
    return {"mesage": "Вы вошли как администратор"}

# 4.Создайте маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}".
# По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".
@app.get("/user/{user_id}")
async def enter_user(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь №: {user_id}"}



# # 5.Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user".
# # По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".

@app.get("/user/{username}/{age}")
async def id_users(username: str, age: int) -> dict:
    return {"Информация о пользователе. Имя: ": username, "Возраст: ": age}



# uvicorn main:app
# uvicorn main:app --reload
# http://127.0.0.1:8000/openapi.json.