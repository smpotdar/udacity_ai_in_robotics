grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]


init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
#goal=[0,5]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

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

heuristic=get_heuristic(grid,goal)

def search(grid,init,goal,cost,heuristic):
    # ----------------------------------------
    # modify the code below
    # ----------------------------------------
    error=0
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    found_path=[]
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    expand_2=[[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand_3=[[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    f=0
    open = [[f,g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    count = 0
    computations=0
    while not found and not resign:
        if len(open) == 0:
            resign = True
            print "Motion failed"
            error=1
	    break
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[2]
            y = next[3]
            g = next[1]
            #f=  g+heuristic[x][y]
            #f=  next[0]
            expand[x][y] = count
            count += 1
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            f2= g2+heuristic[x2][y2]
                            expand_2[x2][y2]=i
			    computations=computations+1
                            open.append([f2,g2, x2, y2])
                            closed[x2][y2] = 1

    x=goal[0]
    y=goal[1]
    found_path.append([x,y])
    expand_3[x][y]='*'
    if(error==0):
    	while(x!=init[0] or y!=init[1]):
        	x2=x-delta[expand_2[x][y]][0]
        	y2=y-delta[expand_2[x][y]][1]
        	expand_3[x2][y2]=delta_name[expand_2[x][y]]
		found_path.append([x2,y2])
        	x=x2
        	y=y2

    print computations
    return expand_3,list(reversed(found_path)),error

expand,path,error=search(grid,init,goal,cost,heuristic)
if(error==0):
	print "Heuristic:"
	for i in range(len(heuristic)):
	    print(heuristic[i])	
	print "Map:"
	for i in range(len(grid)):
	    print(grid[i])
	print"Directions:"
	for i in range(len(expand)):
	    print(expand[i])
	print "Path:"
	print path
else:
	print "Search Failed"
