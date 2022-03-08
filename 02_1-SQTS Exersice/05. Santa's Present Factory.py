from collections import deque

boxes = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}
crafted_presents = {}

while boxes and magic_levels:
    current_box = boxes.pop()
    current_magic_level = magic_levels.popleft()
    result = current_box * current_magic_level

    if current_box == 0 and current_magic_level == 0:
        continue
    if current_box == 0:
        magic_levels.appendleft(current_magic_level)
        continue
    if current_magic_level == 0:
        boxes.append(current_box)
        continue

    if result < 0:
        boxes.append(current_box + current_magic_level)
    elif result in presents:
        present = presents[result]
        if present in crafted_presents:
            crafted_presents[present] += 1
        else:
            crafted_presents[present] = 1
    else:
        boxes.append(current_box + 15)

is_done = ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or \
          ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents)
if is_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes:
    print(f"Materials left: {', '.join(reversed([str(x) for x in boxes]))}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

for key, value in sorted(crafted_presents.items()):
    print(f"{key}: {value}")
