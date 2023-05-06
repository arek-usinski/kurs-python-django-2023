import csv

LOCATIONS = {}

with open('guide_locations.csv', 'r', encoding='UTF-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        id, height, location_name, mountain_range = int(row[0]), int(row[1]), row[2], int(row[3])
        LOCATIONS.update({location_name: {'id': id, 'height': height, 'mountain_range': mountain_range}})

flag = True
counter = 0

while flag and counter < 3:
    user_input = input("Podaj punkt startowy podróży: ")
    if not user_input:
        print("No input. Try again!")
        counter += 1
    elif user_input and user_input in LOCATIONS:
        location = LOCATIONS.get(user_input, "Location not found. Try again!")
        # id = LOCATIONS[user_input]['id']
        print("Your choice:", user_input, location)
        flag = False
    else:
        print("Try again. Location not found!")
        counter += 1

# print(LOCATIONS)