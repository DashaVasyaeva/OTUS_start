import csv
import json


def book_distribution():
    # чтение csv файла, формирование списка с книгами
    with open("books.csv", "r") as f:
        books = csv.DictReader(f)
        books = [i for i in books]

    # чтение json файла
    with open("users.json", "r") as f:
        users = json.load(f)

    # формирование списка с юзерами
    users_result = []

    for user in users:
        user_res = {
            key: value
            for key, value in user.items()
            if key in ["name", "gender", "address", "age", "books"]
        }
        user_res["books"] = []
        users_result.append(user_res)

    # раздача книг юзерам
    while books:
        for user_res in users_result:
            if books:
                user_res["books"].append(books.pop())
            else:
                break

    # сохранение результатов в итоговый файл
    with open("result.json", "w") as f:
        json.dump(users_result, f, indent=4)


book_distribution()
