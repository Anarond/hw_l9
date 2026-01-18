from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_day: str
    birth_month: str
    birth_year: str
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str
