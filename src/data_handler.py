import csv
import json
from src.model import User

def load_data(file_path: str) -> list[User]:
    """
    Loads data from json file
    Returns:
        list of Users
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            users = []
            for item in data:
                user = User(**item)
                users.append(user)
            return users

    except FileNotFoundError:
        print('File not found')
        return []
    except json.decoder.JSONDecodeError:
        print('JSON decode error')
        return []
    except TypeError as e:
        print(e)
        return []

def save_to_csv(users: list[User], path: str) -> None:
    """
    Saves users to csv file
    """
    try:
        with open(path, 'w', newline='', encoding='utf-8') as f:
            field_names = ['name', 'age', 'city']
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()

            for user in users:
                writer.writerow({'name': user.name, 'age': user.age, 'city': user.city})

        print(f"successfully saved users to {path}")
    except Exception as e:
        print(e)