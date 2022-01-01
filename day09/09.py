            
def is_on_map(point, max_x, max_y):
    return (point[0] <= max_x and point[0] >= 0 and point[1] <= max_y and point[1] >= 0)

def get_adjecant_points(x, y, max_x, max_y):
    adjecants = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
    return [adjecant for adjecant in adjecants if is_on_map(adjecant, max_x, max_y)]

def part1(lines):
    max_x = len(lines)-1
    max_y = len(lines[0])-1
    low_points = []
    for x in range(max_x+1):
        for y in range(max_y+1):
            point = lines[x][y]
            adjecants = [lines[adjecant_point[0]][adjecant_point[1]] for adjecant_point in get_adjecant_points(x,y, max_x, max_y)]
            if len([adjecant for adjecant in adjecants if point >= adjecant]) == 0:
                low_points.append(point)
    return sum([point+1 for point in low_points])
    
def part2(lines): 
    return "not solved"

def format_input(filename):
    lines = open(filename).read().splitlines()
    lines = [[int(x) for x in line] for line in lines]
    return lines
    
def main():
    lines = format_input("09.in")
    print(lines)
    print("part1", part1(lines))
    print("part2", part2(lines))

if __name__ == '__main__':
    main()
