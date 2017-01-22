# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:46:31 2015

@author: ShubhankarP
"""

# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0
    expand=[[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand_2=[[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand_3=[['' for row in range(len(grid[0]))] for col in range(len(grid))]
    counter=0
    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        
        if len(open) == 0:
            resign = True
            print next
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                expand[x][y]=counter
                
                found = True
            else:
                for i in range(len(delta)):
                    expand[x][y]=counter
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]                    
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                                                      
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            expand_2[x2][y2]=i    
                            
                    
                
        counter=counter+1
       
    x=goal[0]
    y=goal[1]
    expand_3[x][y]='*'
    while(x!=init[0] or y!=init[1]):
        x2=x-delta[expand_2[x][y]][0]
        y2=y-delta[expand_2[x][y]][1]
        expand_3[x2][y2]=delta_name[expand_2[x][y]]
        x=x2
        y=y2
        
    return expand_2

expand=search(grid,init,goal,cost)
for i in range(len(expand)):
    print(expand[i])
