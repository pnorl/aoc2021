from collections import defaultdict
import itertools

def decode_by_length(lines):
    length_mapper = {2 : 1, 4 : 4, 3 : 7, 7: 8}
    decoded = []
    for line in lines:
        decoded_line = [length_mapper[len(output)] if len(output) in length_mapper else None for output in line[1]]
        decoded.append(decoded_line)
    return decoded
            
def part1(lines):
    decoded = decode_by_length(lines)
    return len([output for line in decoded for output in line if output != None])
    
def letter_to_mask_map(segment_order):
    map = dict()
    for i in range(len(segment_order)):
        map[segment_order[i]] = 2**(6-i)
    return map
    
    
def part2(lines):
    permutations = list(itertools.permutations('abcdefg', r = 7))
    segments_to_digit = {
        int('1110111', 2) : 0,
        int('0010010', 2) : 1,
        int('1011101', 2) : 2,
        int('1011011', 2) : 3,
        int('0111010', 2) : 4,
        int('1101011', 2) : 5,
        int('1101111', 2) : 6,
        int('1010010', 2) : 7,
        int('1111111', 2) : 8,
        int('1111011', 2) : 9}
    
    
    candidates = [letter_to_mask_map(candidate) for candidate in permutations]
    
    correct_candidates = []
    for line in lines:
        for candidate in candidates:
            patterns = line[0]
            correct_patterns = 0
            for pattern in patterns:
                segments = sum([candidate[segment] for segment in pattern])
                if (segments not in segments_to_digit):
                    break
                correct_patterns += 1
            if (correct_patterns == 10):
                correct_candidates.append(candidate)
                break
    
    assert(len(correct_candidates) == len(lines))
        
    numbers = []
    for line, mapper in zip(lines, correct_candidates):
        digits = []
        for segments in line[1]:
            digit = segments_to_digit[sum([mapper[segment] for segment in segments])]
            digits.append(str(digit))
        numbers.append(int(''.join(digits)))
         
    return sum(numbers)
    

def format_input(filename):
    lines = open(filename).read().splitlines()
    lines = [format_input_line(line) for line in lines]
    return lines
    
def format_input_line(line):
    line = line.split(" | ")
    return [x.split(" ") for x in line]
    
def main():
    lines = format_input("08.in")
    print("part1", part1(lines))
    print("part2", part2(lines))

if __name__ == '__main__':
    main()
