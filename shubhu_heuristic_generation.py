grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]
        
def get_heuristic(grid,goal):

    heuristic=[[0 for cols in range(len(grid[0]))] for rows in range(len(grid))]
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    delta = [[-1, 0 ], # go up
    	     [ 0, -1], # go left
    	     [ 1, 0 ], # go down
    	     [ 0, 1 ]] # go right
    closed[goal[0]][goal[1]]=1
    cost=1
    x=goal[0]
    y=goal[1]
    open=[]
    g=0
    heuristic[x][y]=g
    error=0
#    while(x!=0 or y!=0):
    while(True):
        for i in range(len(delta)):
            x2=x-delta[i][0]
            y2=y-delta[i][1]        
            if( x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0])):
		if closed[x2][y2] == 0:               
                    g=g+cost
                    open.append([g,x2,y2])
		    closed[x2][y2]=1
                    heuristic[x2][y2]=g
                    g=g-cost
        if(open):
	    #print open            
            next = open[0]
            open.remove(next)
            x=next[1]
            y=next[2]
            g=next[0]
        else:
            error=1
        
        if(error==1):
            break
        
    return heuristic

goal=[3,3]
heuristic = get_heuristic(grid,goal)
for i in range(len(heuristic)):
    print heuristic[i]
