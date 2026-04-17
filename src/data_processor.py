from src.model import User

class DataProcessor:
    def __init__(self, users: list[User]):
        self.users = users

    def calculate_statistics(self) -> dict:
        """
        Calculates aggregate statistics for the loaded users.
        Returns:
        dict: A dictionary containing:
            - 'average_age': The mean age of all users
            - 'cities_count': A breakdown of users per city
            - 'oldest_user': The User object with the maximum age
            - 'youngest_user': The User object with the minimum age
        """
        if not self.users:
            return {
                "average_age": 0.0,
                "cities": {},
                "oldest_user": None,
                "youngest_user": None
            }
        total_users = len(self.users)
        average_age = sum(user.age for user in self.users) / total_users

        # Count the number of users per city using a frequency dictionary
        cities = {}
        for user in self.users:
            if user.city in cities:
                cities[user.city] += 1
            else:
                cities[user.city] = 1

        # Identify the oldest and youngest users using the 'age' attribute as the comparison key
        oldest_user = max(self.users, key=lambda user: user.age)
        youngest_user = min(self.users, key=lambda user: user.age)

        return {
            "average_age": average_age,
            "cities": cities,
            "oldest_user": oldest_user,
            "youngest_user": youngest_user
        }

    def filter_by_age(self, age: int) -> list[User]:
        return [user for user in self.users if user.age >= age]

    def get_average_age_by_city(self) -> dict:
        """
        Groups users by city and calculates the average age for each group.
        :return:
            dict: A mapping of city names to their average user age
        """
        city_data = {}  # {"City":[sum of age in city, population in city]}

        # Aggregating total age and count users per city
        for user in self.users:
            if user.city not in city_data:
                city_data[user.city] = [user.age, 1]
            else:
                city_data[user.city][0] += user.age
                city_data[user.city][1] += 1

        # Calculating average age for each city
        averages = {}
        for city, data in city_data.items():
            sum, count = data    # Unpacking the sum and count
            averages[city] = sum / count

        return averages
