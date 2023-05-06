import csv

LOCATIONS = {}

with open('guide_locations.csv', 'r', encoding='UTF-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        id, height, location_name, mountain_range = map(str.strip, row)
        print(id, height, location_name, mountain_range)