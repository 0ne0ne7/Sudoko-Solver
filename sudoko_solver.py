from pathlib import Path
from pprint import pprint

input_path = Path('Inputs')

puzzle_name='puzzle1'

with open(input_path/ f'{puzzle_name}.txt','r') as f:
    puzzle=f.read().split('\n')
    puzzle=[[int(n) for n in line.split(',')] for line in puzzle]
    # pprint(puzzle)

def possible(grid,x,y,n):
    for i in range(9):
        # Same row validation
        if grid[x][i]==n:
            return False
        # Same column validation
        if grid[i][y]==n:
            return False
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(3):
        for j in range(3):
            # Same grid validation
            if grid[x0+i][y0+j]==n:
                return False
    return True

# print(possible(puzzle,0,1,5))
def solver(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                for n in range(1,10):
                    if possible(grid,i,j,n):
                        grid[i][j]=n
                        solver(grid)
                        grid[i][j]=0
                return
    pprint(grid)
    # input('More?')

if __name__=='__main__':
    solver(puzzle)




