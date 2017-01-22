# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:46:42 2015

@author: ShubhankarP
"""

# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
# 
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

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
