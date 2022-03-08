from collections import deque

green_light_seconds = int(input())
free_window_seconds = int(input())

car_models = deque()
total_cars_passed = 0

crash = False

command = input()
while command != "END" and not crash:

    if command == "green":
        current_green_light = green_light_seconds
        while car_models and current_green_light > 0:
            current_car = car_models.popleft()
            if current_green_light >= len(current_car) or current_green_light + free_window_seconds >= len(current_car):
                total_cars_passed += 1
                current_green_light -= len(current_car)
            else:
                character_hit = current_car[current_green_light + free_window_seconds]
                print("A crash happened!")
                print(f"{current_car} was hit at {character_hit}.")
                crash = True
                break
    else:
        car_models.append(command)

    command = input()
if not crash:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")
