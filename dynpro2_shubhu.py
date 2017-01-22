# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:22:46 2015

@author: ShubhankarP
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 17:03:11 2015

@author: ShubhankarP
"""

# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one
value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
closed[goal[0]][goal[1]]=1
delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j]==1):
                value[i][j]=99
    x=goal[0]
    y=goal[1]
    open=[]
    g=0
    value[x][y]=g
    error=0
    while(x!=0 or y!=0):
    
        for i in range(len(delta)):
            x2=x-delta[i][0]
            y2=y-delta[i][1]        
            if( x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0])):
                if closed[x2][y2] == 0 and grid[x2][y2] == 0:                
                    g=g+cost
                    action[x2][y2]=i
                    closed[x2][y2]=1
                    open.append([g,x2,y2])
                    #print open
                    value[x2][y2]=g
                    g=g-cost
        if(open):            
            next = open[0]
            open.remove(next)
            x=next[1]
            y=next[2]
            g=next[0]
        else:
            error=1
        
        if(error==1):
            break
    
    #policy[goal[0]][goal[1]]='*'
    #for i in range(len(action)):
    #    for j in range(len(action[0])):
    #        if(action[i][j]>-1):
    #            policy[i][j]=delta_name[action[i][j]]
    x=goal[0]
    y=goal[1]
    policy[x][y]='*'
    action[x][y]=2
    while(x!=0 or y!=0):
        x2=x-delta[action[x][y]][0]
        y2=y-delta[action[x][y]][1]
        policy[x2][y2]=delta_name[action[x][y]]
        x=x2
        y=y2        
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return policy




    #timer=timer+1
value=compute_value(grid,goal,cost)
for i in range(len(value)):
    print value[i]
    
    
    