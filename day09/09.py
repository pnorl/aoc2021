            
def is_on_map(point, max_x, max_y):
    return (point[0] <= max_x and point[0] >= 0 and point[1] <= max_y and point[1] >= 0)

def get_adjecant_points(x, y, max_x, max_y):
    adjecants = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [adjecant for adjecant in adjecants if is_on_map(adjecant, max_x, max_y)]

def get_value(lines, point):
    return lines[point[0]][point[1]]    

def get_low_points(lines):
    max_x = len(lines)-1
    max_y = len(lines[0])-1
    low_points = []
    for x in range(max_x+1):
        for y in range(max_y+1):
            point = lines[x][y]
            adjecant_points = get_adjecant_points(x, y, max_x, max_y)
            adjecant_values = [get_value(lines, adjecant_point) for adjecant_point in adjecant_points]            
            if len([adjecant for adjecant in adjecant_values if point >= adjecant]) == 0:
                low_points.append((x,y))
    return low_points

def calc_basin(lines, low_point, basin):
    if (low_point in basin):
        return basin
    max_x = len(lines)-1
    max_y = len(lines[0])-1
    adjecants = get_adjecant_points(low_point[0], low_point[1], max_x, max_y)
    basin.add(low_point)
    for adjecant in adjecants:
        adjecant_value = get_value(lines, adjecant)
        point_value = get_value(lines, low_point)
        if adjecant_value != 9 and point_value < adjecant_value:
            basin = calc_basin(lines, adjecant, basin)
    return basin

def part1(lines):
    low_points = get_low_points(lines)
    return sum([get_value(lines, point)+1 for point in low_points])
    
def part2(lines):
    low_points = get_low_points(lines)
    basins = [calc_basin(lines, low_point, set()) for low_point in low_points]
    basin_sizes = [len(basin) for basin in basins]
    basin_sizes.sort()
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

def format_input(filename):
    lines = open(filename).read().splitlines()
    lines = [[int(x) for x in line] for line in lines]
    return lines
    
def main():
    lines = format_input("09.in")
    print("part1", part1(lines))
    print("part2", part2(lines))

if __name__ == '__main__':
    main()
