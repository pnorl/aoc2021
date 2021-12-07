positions = [int(x) for x in open("07.in").read().split(",")]

def fuel_consumption_1(start, target):
    return abs(target-start)

def fuel_consumption_2(start, target):
    length = abs(target-start)
    return int(length*(length+1)/2)

def min_fuel(positions, fuel_consumption):
    min_fuel = None
    for i in range(min(positions), max(positions)+1):
        fuel = sum([fuel_consumption(position, i) for position in positions])
        if min_fuel == None or min_fuel > fuel:
            min_fuel = fuel
    return min_fuel        

print("part1", min_fuel(positions, fuel_consumption_1))
print("part2", min_fuel(positions, fuel_consumption_2))