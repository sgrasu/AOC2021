import re

with open('day2.txt', 'r') as file:
    commands = file.read().splitlines()
    horizontal = 0
    depth = 0

    horizontal2 = 0
    depth2 = 0
    aim = 0
    regex = r"(forward|up|down) (\d)+"
    for command in commands:
        extract = re.search(regex,command)
        (direction, increment) = extract.groups()
        if direction == 'forward':
            horizontal += float(increment)
            horizontal2 += float(increment)
            depth2 += aim*float(increment)
        elif direction == 'down':
            depth += float(increment)
            aim += float(increment)
        elif direction == 'up':
            depth -= float(increment)
            aim -= float(increment)
    print(horizontal*depth)
    print(horizontal2*depth2)