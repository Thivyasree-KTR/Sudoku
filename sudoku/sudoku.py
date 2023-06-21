import numpy as np
#print("Hello world !")

grid=[[5,3,0,0,7,0,0,0,0],
      [6,0,0,1,9,5,0,0,0],
      [0,9,8,0,0,0,0,6,0],
      [8,0,0,0,6,0,0,0,3],
      [4,0,0,8,0,3,0,0,1],
      [7,0,0,0,2,0,0,0,6],
      [0,6,0,0,0,0,2,8,0],
      [0,0,0,4,1,9,0,0,5],
      [0,0,0,0,8,0,0,0,0]]

#print(np.matrix(grid))

def possible(row,col,num):
    global grid
    for i in range(9):
        if grid[row][i]==num:
            return False
        if row!=col:
            if grid[i][col]==num:
                return False
    
    x0=(row//3)*3
    y0=(col//3)*3

    for i in range(3):
        for j in range(3):
            if grid[x0+i][y0+j]==num:
                return False
    return True

def solve():
    global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col]==0:
                for num in range(1,10):
                    if possible(row,col,num):
                        grid[row][col]=num
                        solve()
                        grid[row][col]=0
                return 
            
    #print(np.matrix(grid))
    print_board(grid)
    input("Press enter to see if there is more possible solutions...")

def print_board(grid):
    for i in range(9):
        if i%3==0 and i!=0:
            print("--------------------")
        for j in range(9):
            if j%3==0 and j!=0:
                print("|",end="")

            if j==8:
                print(grid[i][j])
            else:
                print(str(grid[i][j])+" ",end="")

solve()