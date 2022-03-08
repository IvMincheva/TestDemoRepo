from collections import deque

queue = deque()

numb_petrol_pumps = int(input())

for _ in range(numb_petrol_pumps):
    pump = [int(x) for x in input().split()]
    queue.append(pump)

for idx in range(numb_petrol_pumps):
    car_fuel = 0
    completed = True
    for pump in queue:
        petrol = pump[0]
        km = pump[1]
        car_fuel += petrol
        if car_fuel < km:
            completed = False
            break
        car_fuel -= km
    if completed:
        print(idx)
        break
    queue.append(queue.popleft())

