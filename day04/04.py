import re
data = open("04.in").read().split("\n\n")
draws = [int(x) for x in data.pop(0).split(",")]
boards = data
part1 = 0
part2 = 0

def format_board(board):
    rows = board.split("\n")
    rows = [row.strip().split() for row in rows]
    return [[{"number": int(box), "marked": False} for box in row] for row in rows]

boards = [format_board(board) for board in boards]  

def mark_board(board, number):
    for row in board:
        for box in row:
            if (box["number"] == number):
                box["marked"] = True

def is_all_marked(boxes):
    return len(boxes) == len([box for box in boxes if box["marked"]])

def is_winning(board):
    for row in board:
        if is_all_marked(row):
            return True
    for i in range(len(board[0])):
        column = [board[j][i] for j in range(len(board))]
        if is_all_marked(column):
            return True
    return False   

def score(board):
    return sum([box["number"] for row in board for box in row if box["marked"] == False])

scores = [0]*len(boards)
win_order = []
for number in draws:
    for i, board in enumerate(boards):
        mark_board(board, number)
        if scores[i] == 0 and is_winning(board):
            scores[i] = score(board) * number
            win_order.append(i)
part1 = scores[win_order[0]]
part2 = scores[win_order[-1]]
print("part1", part1)
print("part2", part2)