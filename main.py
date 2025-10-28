import argparse
from tabulate import tabulate
from utils import read_csv_files
from reports.average_rating import AverageRatingReport

REPORTS = {
    "average-rating": AverageRatingReport,
}

def main():
    parser = argparse.ArgumentParser(description="Анализ рейтинга брендов")
    parser.add_argument("--files", nargs="+", required=True, help="Пути к CSV-файлам")
    parser.add_argument("--report", required=True, help="Название отчёта (например, average-rating)")
    args = parser.parse_args()

    if args.report not in REPORTS:
        raise ValueError(f"Неизвестный отчёт: {args.report}")

    data = read_csv_files(args.files)
    report = REPORTS[args.report]()
    results = report.generate(data)

    print(tabulate(results, headers=["Бренд", "Средний рейтинг"], floatfmt=".2f"))

if __name__ == "__main__":
    main()
