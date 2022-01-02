import copy
from collections import defaultdict

def isSmallCave(cavename):
    # Big Caves - Written in uppercase
    # Small Caves - lowecase letters
    return cavename[0].islower()

def find_paths_1(path_so_far, paths, connections):
    next_caves = connections[path_so_far[-1]]
    for next_cave in next_caves:
        new_path = copy.deepcopy(path_so_far)
        if isSmallCave(next_cave) and next_cave in path_so_far:
            #We have already visited this cave
            continue
        new_path.append(next_cave)    
        if next_cave == "end":
            paths.append(new_path)
        else:
            find_paths_1(new_path, paths, connections)    

def print_paths(paths):
    paths.sort()
    for path in paths:
        print(",".join(path))

def find_paths_2(path_so_far, small_cave_visited_twice, paths, connections):
    next_caves = connections[path_so_far[-1]]
    for next_cave in next_caves:
        new_path = copy.deepcopy(path_so_far)
        new_path.append(next_cave)
        if next_cave == "start":
            continue
        elif next_cave == "end":
            paths.append(new_path)
        elif isSmallCave(next_cave) and small_cave_visited_twice and next_cave in path_so_far:
            continue
        else:
            new_small_cave_visited_twice = small_cave_visited_twice
            if isSmallCave(next_cave) and not small_cave_visited_twice and new_path.count(next_cave) > 1:
                new_small_cave_visited_twice = True
            find_paths_2(new_path, new_small_cave_visited_twice, paths, connections)    

def part1(connections):
    paths = []
    find_paths_1(["start"], paths, connections)
    return len(paths)

def part2(connections):
    paths = []
    find_paths_2(["start"], False, paths, connections)
    return len(paths)

def format_input(filename):
    lines = open(filename).read().splitlines()
    connections = defaultdict(list)
    for line in lines:
        path_start, path_end = line.split("-")
        connections[path_start].append(path_end)
        connections[path_end].append(path_start)
    return connections

def main():
    connections = format_input("12.in")
    print("part1", part1(connections))
    print("part2", part2(connections))

if __name__ == '__main__':
    main()