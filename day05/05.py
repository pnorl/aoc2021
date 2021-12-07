from collections import defaultdict
lines = open("05.in").read().splitlines()
lines = [line.split(" -> ") for line in lines]
lines = [[[int(x) for x in cord.split(",")] for cord in line] for line in lines]

def is_horizontal(line):
    return line[0][1] == line[1][1]

def is_vertical(line):
    return line[0][0] == line[1][0]

def get_y(line):
    return line[0][1], line[1][1]

def get_x(line):
    return line[0][0], line[1][0]

def get_points_in_line(line, include_diagonal = False):
    if is_horizontal(line):
        return [(x,line[0][1]) for x in range(min(get_x(line)), max(get_x(line))+1)]
    elif is_vertical(line):
        return [(line[0][0],y) for y in range(min(get_y(line)), max(get_y(line))+1)]
    elif include_diagonal:
        x_step = 1 if line[0][0] < line[1][0] else -1
        x = [x for x in range(line[0][0], line[1][0] + x_step, x_step)]
        y_step = 1 if line[0][1] < line[1][1] else -1
        y = [y for y in range(line[0][1], line[1][1] + y_step, y_step)]
        return [(x[i], y[i]) for i in range(len(x))]
    return []

def part1():
    overlaps = defaultdict(int)
    for line in lines:
        points = get_points_in_line(line)
        for point in points:
            overlaps[point] += 1
    return len([x for x in overlaps.values() if x >= 2])


def part2():
    overlaps = defaultdict(int)
    for line in lines:
        points = get_points_in_line(line, True)
        for point in points:
            overlaps[point] += 1
    return len([x for x in overlaps.values() if x >= 2])

print("part1", part1())
print("part2", part2())