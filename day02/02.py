lines = open("02.in").read().splitlines()

def part1():
    horizontal, depth = 0,0
    for line in lines:
        command, value = line.split(" ")
        value = int(value)
        if (command == "forward"):
            horizontal += value
        elif(command == "down"):
            depth += value
        elif (command == "up"):
            depth -= value        

    return depth*horizontal

def part2():
    horizontal, depth, aim = 0,0,0

    for line in lines:
        command, value = line.split(" ")
        value = int(value)
        if (command == "forward"):
            horizontal += value
            depth += aim*value
        elif(command == "down"):
            aim += value
        elif (command == "up"):
            aim -= value
    return depth*horizontal

print("part1", part1())
print("part2", part2())