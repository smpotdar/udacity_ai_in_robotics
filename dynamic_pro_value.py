
grid = [[0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
#goal=[0,5]
cost = 1 # the cost associated with moving from a cell to an adjacent one


def dynamic_program_search(grid,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------

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
#    while(x!=0 or y!=0):
    while(True):
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
    
    policy[goal[0]][goal[1]]='*'
    for i in range(len(action)):
        for j in range(len(action[0])):
            if(action[i][j]>-1):
                policy[i][j]=delta_name[action[i][j]]

    return policy

value=dynamic_program_search(grid,goal,cost)
print "Directions:"
for i in range(len(value)):
    print value[i]
    
