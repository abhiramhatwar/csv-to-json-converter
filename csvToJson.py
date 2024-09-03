import csv
import json
import sys

def csv_to_json(csv_file, json_file):
    with open(csv_file, mode='r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    with open(json_file, mode='w') as f:
        json.dump(rows, f, indent=4)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py [input_csv] [output_json]")
        return
    csv_file = sys.argv[1]
    json_file = sys.argv[2]
    csv_to_json(csv_file, json_file)
    print(f"Converted {csv_file} to {json_file}")

if __name__ == "__main__":
    main()
