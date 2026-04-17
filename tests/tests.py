import pytest
from src.model import User
from src.data_processor import DataProcessor

@pytest.fixture
def sample_users():
    return [
        User(name="Anna", age=20, city="Warszawa"),
        User(name="Jan", age=30, city="Kraków"),
        User(name="Maria", age=40, city="Warszawa")
    ]

def test_filtering(sample_users):
    processor = DataProcessor(sample_users)
    filtered = processor.filter_by_age(31)
    assert len(filtered) == 1
    assert all(user.age >= 31 for user in filtered)

def test_get_statistics(sample_users):
    processor = DataProcessor(sample_users)
    stats = processor.calculate_statistics()

    assert stats["average_age"] == 30.0
    assert stats["cities"]["Warszawa"] == 2
    assert stats["cities"]["Kraków"] == 1
    assert stats["oldest_user"].name == "Maria"

def test_get_average_age_by_city(sample_users):
    processor = DataProcessor(sample_users)
    city_avgs = processor.get_average_age_by_city()

    assert city_avgs["Warszawa"] == 30.0
    assert city_avgs["Kraków"] == 30.0