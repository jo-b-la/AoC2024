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

def check_for_word(grid, row,col,dx,dy,word):
    # print(row,col,dx,dy,word)
    for i in range(len(word)):
           if grid[row + i*dy][col + i*dx] != word[i]:
               return False

    return True

def process_file(filename,word):
    grid = read_grid_from_file(filename)
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)

    # print(grid)

    total_xmas=0

    for row in range(rows-word_len-1):
       for col in range(cols-word_len-1):
            # Top Down Check
            if check_for_word(grid,row,col,1,1,word) or check_for_word(grid,row,col,1,1,word[::-1]):
                # Bottom up check
                if check_for_word(grid,row+word_len-1,col,1,-1,word) or check_for_word(grid,row+word_len-1,col,1,-1,word[::-1]):
                    total_xmas += 1
    print (total_xmas)

def main():
    filename = "input.txt"
    current_dir = Path(__file__).parent
    input_file = current_dir / filename
    process_file(input_file, "MAS")


if __name__ == "__main__":
    main()
