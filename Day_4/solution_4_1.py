from pathlib import Path

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
]


def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

def check_for_word(grid, rows,cols,row,col,dx,dy,word):
    if not (0 <= row + (len(word)-1)*dx < rows and
            0 <= col + (len(word)-1)*dy < cols):
           return False

    for i in range(len(word)):
           if grid[row + i*dx][col + i*dy] != word[i]:
               return False

    return True

def process_file(filename,word):
    grid = read_grid_from_file(filename)
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)

    # print(grid)

    total_xmas=0

    for row in range(rows):
       for col in range(cols):
           for dx, dy in directions:
                if check_for_word(grid, rows,cols,row,col,dx,dy,word):
                    total_xmas += 1
    print (total_xmas)

def main():
    filename = "input.txt"
    current_dir = Path(__file__).parent
    input_file = current_dir / filename
    process_file(input_file, "XMAS")


if __name__ == "__main__":
    main()
