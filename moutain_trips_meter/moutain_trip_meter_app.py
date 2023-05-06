import csv

LOCATIONS = {}

with open('guide_locations.csv', 'r', encoding='UTF-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        id, height, location_name, mountain_range = int(row[0]), int(row[1]), row[2], int(row[3])
        LOCATIONS.update({location_name: {'id': id, 'height': height, 'mountain_range': mountain_range}})
# print(LOCATIONS)

counter = 0

while counter < 3:
    user_input = input("Provide starting point: ")
    if user_input:
        location = LOCATIONS.get(user_input, "Location has not been found")
        print(location)
    else:
        print("Closing ...")
        exit(1)
    counter += 1
