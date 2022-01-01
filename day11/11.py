import copy
grid_size = 10 # grid size

def increase_energy_by_one(grid):
    for x in range(grid_size):
        for y in range(grid_size):
            grid[x][y] += 1

def is_on_grid(point):
    return (point[0] < grid_size and point[0] >= 0 and point[1] < grid_size and point[1] >= 0)

def get_adjecant_points(x, y):
    adjecants = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
    return [adjecant for adjecant in adjecants if is_on_grid(adjecant)]

def reset_grid(grid):
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] > 9:
                grid[x][y] = 0

def print_grid(grid):
    for row in grid:
        print("".join([str(x) for x in row]))

def simulate_step(grid):
    total_flashes = 0
    increase_energy_by_one(grid)
    flashed = set()
    flashing = []
    while True:
        for x in range(grid_size):
            for y in range(grid_size):
                if grid[x][y] > 9 and (x,y) not in flashed:
                    flashing.append((x,y))
        if len(flashing) == 0:
            break
        for flashing_point in flashing:
            for adjecant in get_adjecant_points(flashing_point[0], flashing_point[1]):
                grid[adjecant[0]][adjecant[1]] += 1
        flashed.update(flashing)
        total_flashes += len(flashing)
        flashing = []   
    reset_grid(grid)
    return total_flashes

def part1(grid):
    steps = 100
    total_flashes = 0
    for step in range(steps):
        total_flashes += simulate_step(grid)
    return total_flashes

def part2(grid):
    i = 0
    while True:
        i += 1
        simulate_step(grid)
        if sum([sum(row) for row in grid]) == 0:
            return i

def format_input(filename):
    lines = open(filename).read().splitlines()
    lines = [[int(x) for x in list(line)] for line in lines]
    return lines

def main():
    grid = format_input("11.in")
    print("part1", part1(copy.deepcopy(grid)))
    print("part2", part2(copy.deepcopy(grid)))

if __name__ == '__main__':
    main()