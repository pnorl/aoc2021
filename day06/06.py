from collections import defaultdict
lanterns = [int(x) for x in open("06.in").read().split(",")]

def simulate(lanterns, n):
    grouped_lanterns = [0]*9
    for lantern in lanterns:
        grouped_lanterns[lantern] += 1
    
    for _ in range(n):
        new_lanterns = [0]*9
        for lantern in range(len(grouped_lanterns)):
            if (lantern == 0):
                new_lanterns[6] += grouped_lanterns[lantern]
                new_lanterns[8] += grouped_lanterns[lantern]
            else:
                new_lanterns[lantern-1] += grouped_lanterns[lantern]    
        grouped_lanterns = new_lanterns
    return sum(grouped_lanterns)

print("part1", simulate(lanterns, 80))
print("part2", simulate(lanterns, 256))