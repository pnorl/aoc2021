def part1(lines):
    return "not solved"

def part2(lines):
    return "not solved"

def format_input(filename):
    lines = open(filename).read().splitlines()
    return lines

def main():
    lines = format_input("0.in")
    print("part1", part1(lines))
    print("part2", part2(lines))

if __name__ == '__main__':
    main()