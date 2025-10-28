from collections import defaultdict
from .base_report import BaseReport

class AverageRatingReport(BaseReport):
    """Отчёт по среднему рейтингу брендов."""

    def generate(self, data):
        brand_ratings = defaultdict(list)

        for item in data:
            brand = item.get("brand")
            rating = item.get("rating")
            if brand and rating:
                try:
                    brand_ratings[brand].append(float(rating))
                except ValueError:
                    continue  # пропускаем некорректные данные

        results = []
        for brand, ratings in brand_ratings.items():
            avg_rating = sum(ratings) / len(ratings)
            results.append((brand, avg_rating))

        # сортируем по рейтингу (по убыванию)
        results.sort(key=lambda x: x[1], reverse=True)
        return results
