#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, "r", encoding="utf-8") as f:
            csv_reader = csv.DictReader(f)
            data = list(csv_reader)
        with open(csv_filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return True
    except Exception as e:
        print(f"Exception caught: {e}")
        return False
