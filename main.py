import sys

import json

from faker import Faker
fake_ru = Faker('ru_RU')
dict = {}

OUTPUT_FILE = "namelist.txt"


def task():
    for i in range(1, 251):
        name_ = fake_ru.name()
        tn = fake_ru.phone_number()
        j = fake_ru.job()
        a = fake_ru.address()
        dict[i] = {i: [name_, tn, j, a]}
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.writelines(dict)


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
