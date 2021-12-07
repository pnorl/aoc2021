lines = open("03.in").read().splitlines()

part1 = 0
part2 = 0

def most_common(numbers):
    return int(sum(numbers) > len(numbers)/2)

def least_common(numbers):
    return 1 - most_common(numbers)

def is_equals(numbers):
    return sum(numbers) == len(numbers)/2

gamma = ""
for i in range(0,len(lines[0])):
    gamma += str(most_common([int(line[i]) for line in lines]))

epsilon = "".join([str(1-int(x)) for x in gamma])

part1 = int(gamma, 2) * int(epsilon, 2)
print("part1", part1)

oxygen = 0
scrubber = 0

def calc(bitfunction, bit):
    numbers = lines.copy()
    for i in range(len(lines[0])):
        colon = [int(line[i]) for line in numbers]
        comparison = bitfunction(colon)
        print(comparison)
        if is_equals(colon):
            comparison = bit  
             
        numbers = [x for x in numbers if int(x[i]) == comparison]
        if (len(numbers) == 1):
            return numbers[0]

oxygen = calc(most_common, 1)
print(oxygen)

scrubber = calc(least_common, 0)
print(scrubber)
part2 = int(oxygen, 2) * int(scrubber, 2)
print("part2", part2)