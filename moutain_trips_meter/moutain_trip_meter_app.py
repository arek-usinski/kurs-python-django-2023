import csv

LOCATIONS = {}

with open('guide_locations.csv', 'r', encoding='UTF-8') as file:
    reader = csv.reader(file)
    for row in reader:
        id, height, location_name, mountain_range = row[0], row[1], row[2], row[3]
