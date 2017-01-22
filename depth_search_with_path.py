
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
#goal = [0, 5]
cost = 1
found_path=[]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    error=0
    x = init[0]
    y = init[1]
    g = 0
    expand_2=[[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand_3=[[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    computations=0
    while not found and not resign:
        if len(open) == 0:
            resign = True
            #return 'fail' #Original
	    print 'fail'
            error=1
	    break

        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            expand_2[x2][y2]=i
			    computations=computations+1
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
    #return expand_3 #Original
    return expand_3,found_path,error
    
expand,path,error=search(grid,init,goal,cost)
if(error==0):
	print "Directions:"
	for i in range(len(expand)):
	    print(expand[i])

	print "Path:"
	print(list(reversed(path)))
else:
	print "Fail"
