
import random

####====================================
#### CONSTANT

BIG_WIDTH = 8
BIG_SIZE = BIG_WIDTH * BIG_WIDTH

SMALL_WIDTH = 10
SMALL_SIZE  = SMALL_WIDTH * SMALL_WIDTH

####====================================
#### MAZE DIGGING

DIR1 = [(0,-1),(1,0),(0,1),(-1,0)]
DIR2 = [(0,-2),(2,0),(0,2),(-2,0)]

MAZE = [[True for i in range(BIG_WIDTH*2+1)] for j in range(BIG_WIDTH*2+1)]
START = (1,1)

def draw_maze(m):
    for y in range(BIG_WIDTH*2+1):
        for x in range(BIG_WIDTH*2+1):
            if MAZE[x][y]:
                print("[]", end="")
            else:
                print("  ",end="")
        print()

def dig(s):
    MAZE[s[0]][s[1]]=False
    
def dig_maze(m):
    dig(m)
    DIR  = [0,1,2,3]
    random.shuffle(DIR)

    for i in DIR:
        m1 = (m[0]+DIR1[i][0] ,m[1]+DIR1[i][1])
        m2 = (m1[0]+DIR1[i][0] ,m1[1]+DIR1[i][1])
        print(f"m2={m2}")
        if (m2[0]>=0) and (m2[0]<=BIG_SIZE*2+1) and (m2[1]>=0) and (m2[1]<=BIG_SIZE*2+1) and MAZE[m2[0]][m2[1]]:
            dig(m1)
            draw_maze(MAZE)
            dig_maze(m2)
            

        
if __name__=="__main__":
    dig_maze((1,1))
    draw_maze(MAZE)