lines = open("01.in").read().splitlines()
numbers = [int(x) for x in lines]

def conv(numbers, i):
    return numbers[i] + numbers[i+1] + numbers[i+2]

def part1(numbers):
    return len([1 for i in range(1,len(numbers)) if numbers[i] > numbers[i-1]])

def part2(numbers):
    return len([1 for i in range(1,len(numbers)-2) if conv(numbers, i) > conv(numbers, i-1)])

print("part1", part1(numbers))
print("part2", part2(numbers))