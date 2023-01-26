import random
from faker import Faker

from data.data import Person

faker_ru = Faker('ru_RU')
Faker.seed()


def create_person():
    yield Person(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        phone_number=faker_ru.phone_number(),
        current_address=faker_ru.address(),
    )


def generate_file():
    path = rf"C:\Users\Ira\Pictures\filetest{random.randint(0, 999)}.txt"
    file = open(path, 'w+')
    file.write(f"Hello World{random.randint(0, 999)}")
    file.close()
    return file.name, path
