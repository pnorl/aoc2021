def paper_to_string(paper):
    result = ""
    for y in range(len(paper[0])):
        result += "\n" + "".join([str(paper[x][y]) for x in range(len(paper))])
    return result

def fold_up(paper, position):
    for x in range(len(paper)):
        for y in range(position + 1, len(paper[x])):
            if paper[x][y] == "X":
                paper[x][position-(y-position)] = "X"
        paper[x] = paper[x][:position]

def fold_left(paper, position):
    for x in range(position, len(paper)):
        for y in range(len(paper[0])):
            if paper[x][y] == "X":
                paper[position-(x-position)][y] = "X"
    del paper[position:]

def create_paper(coords):
    max_x = max([coord[0] for coord in coords])
    max_y = max([coord[1] for coord in coords])
    
    paper = [[" " for x in range(max_y+1)] for y in range(max_x+1)]
    
    for coord in coords:
        x = coord[0]
        y = coord[1]
        paper[x][y] = "X"
    return paper

def fold_paper(paper, fold):
    diection, position = fold
    if diection == "x":
        fold_left(paper, position)
    else:
        fold_up(paper, position)

def part1(coords, folds):
    paper = create_paper(coords)
    fold_paper(paper, folds[0])
    return sum([sum([1 for x in x if x == "X"]) for x in paper])

def part2(coords, folds):
    paper = create_paper(coords)
    for fold in folds:
        fold_paper(paper, fold)
    return paper_to_string(paper)

def format_input(filename):
    coordinates, folds = open(filename).read().split("\n\n")
    
    coordinates = coordinates.split("\n")
    coordinates = [[int(x) for x in coordinate.split(",")] for coordinate in coordinates]
    
    folds = folds.split("\n")
    folds = [fold.lstrip("fold along ") for fold in folds]
    folds = [fold.split("=") for fold in folds]
    folds = [[x, int(y)] for x,y in [fold for fold in folds]]

    return coordinates, folds

def main():
    coordinates, folds = format_input("13.in")
    print("part1", part1(coordinates, folds))
    print("part2", part2(coordinates, folds))

if __name__ == '__main__':
    main()