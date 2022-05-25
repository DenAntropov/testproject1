from faker import Faker

fake_ru = Faker('ru_RU')
print(fake_ru.simple_profile())
print(fake_ru.isbn10())
