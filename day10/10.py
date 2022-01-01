open_close = {'(' : ')', '<': '>','{' :'}','[':']'}
points = {')': 3,']': 57,'}': 1197,'>': 25137}
points_2 = {')': 1,']': 2,'}': 3,'>': 4}

def check_syntax(line):
    stack = []
    for char in line:
        if char in open_close:
            stack.append(open_close[char])
        else:
            if (stack.pop() != char):
                return char
    return None

def part1(lines):
    return sum([points[char] for char in [check_syntax(line) for line in lines] if char != None])

def calculate_closing_chars(line):
    stack = []
    for char in line:
        if char in open_close:
            stack.append(open_close[char])
        else:
            stack.pop()
    stack.reverse()
    return stack

def score_2(chars):
    score = 0
    for char in chars:
        score = score * 5
        score += points_2[char]
    return score    

def part2(lines):
    lines = [line for line in lines if check_syntax(line) == None]
    scores = [score_2(calculate_closing_chars(line)) for line in lines]
    scores.sort()
    return scores[int(len(scores)/2)]

def format_input(filename):
    lines = open(filename).read().splitlines()
    return lines

def main():
    lines = format_input("10.in")
    print("part1", part1(lines))
    print("part2", part2(lines))

if __name__ == '__main__':
    main()