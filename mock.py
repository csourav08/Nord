from faker import Faker
import json

fake = Faker()

credentials = {
    "firstName": fake.first_name(),
    "lastName": fake.last_name(),
    "company": fake.company(),
    "email": fake.email(),
    "phone": fake.phone_number(),
    "jobTitle": fake.job(),
    "country": fake.country()
}

with open("credentials.json", "w") as f:
    json.dump(credentials, f)
