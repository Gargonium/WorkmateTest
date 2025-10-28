import pytest
from reports.average_rating import AverageRatingReport

@pytest.fixture
def sample_data():
    return [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
        {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
        {"name": "macbook air", "brand": "apple", "price": "1299", "rating": "4.7"},
    ]

def test_average_rating_report(sample_data):
    report = AverageRatingReport()
    result = report.generate(sample_data)
    assert isinstance(result, list)
    assert result[0][0] == "apple"
    assert round(result[0][1], 2) == 4.8  # среднее 4.9 и 4.7
