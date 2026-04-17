import json
import random


def generate_data(file_path: str, count: int = 100):
    names = ["Alicja", "Jakub", "Krzysztof", "Diana", "Edward", "Fiona", "Shrek", "Kacper", "Luiza", "Adrian"]
    cities = ["Warszawa", "Krakow", "Wroclaw", "Gdansk", "Poznan", "Lodz", "Lublin"]

    users = []
    for i in range(count):
        user = {
            "name": f"{random.choice(names)}",
            "age": random.randint(18, 80),
            "city": random.choice(cities)
        }
        users.append(user)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=4)

    print(f"Successfully generated {count} users in {file_path}")


if __name__ == "__main__":
    generate_data("../data/users_generated.json", 100)