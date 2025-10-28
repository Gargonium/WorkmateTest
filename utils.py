import csv

def read_csv_files(file_paths):
    """Читает несколько CSV-файлов и возвращает список словарей."""
    rows = []
    for path in file_paths:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
    return rows
