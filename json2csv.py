import json
import csv
import os
import sys


def json_to_csv(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

        base_filename = os.path.splitext(os.path.basename(json_file))[0]
        csv_file = f"{base_filename}.csv"

        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)

            record_list = list(data.keys())
            records = data.get(record_list[0])

            headers = list(records[0].keys())
            writer.writerow(headers)

            for record in records:
                writer.writerow(record.values())

        print(f"Результат сохранён как: {csv_file}")

    except Exception as e:
        print(f"{str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Введите: json2csv.py example.json")
    else:
        json_file = sys.argv[1]
        json_to_csv(json_file)
