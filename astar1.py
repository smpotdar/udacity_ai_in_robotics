# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:15:35 2015

@author: ShubhankarP
"""

# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
#goal=[2,3]
cost = 1
len_grid=len(grid[0])
delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']
pos=init
x=init[0]
y=init[0]

list_obstacles=[]
checked=[init]
g=0
motion=[[0,0,0]]
def find_obstacles(empty_list,grid_array):
    for i in range(len(grid_array)):
        for j in range(len(grid_array[0])):
            if(grid_array[i][j]==1):
                c=[i,j]
                empty_list.append(c)    
    return empty_list
    
def move(delta,pos_g_list,list_obstacles,checked,len_grid):
    #for q in range(len(pos_g_list)):        
        point=[pos_g_list[1],pos_g_list[2]]
        g=pos_g_list[0]    
        list_c=[]
        list_c_2=[]
        checked_2=[]
        checked_3=[]
        counter=0
        for i in range(len(delta)):
            c=0
            c=[point[0]+delta[i][0],point[1]+delta[i][1]]
            if(c[0]>=0 and c[1]>=0 and c[0]<=(len_grid-2) and c[1]<=(len_grid-1)):
                list_c.append(c)
    
        for i in range(len(list_c)):
            for j in range(len(checked)):
                if(list_c[i]==checked[j]):
                    counter=counter+1
            if(counter==0):
                list_c_2.append(list_c[i])
            else:
                counter=0
            
    
        for i in range(len(list_c_2)):
            for j in range(len(list_obstacles)):
                if(list_c_2[i]==list_obstacles[j]):
                    counter=counter+1
            if(counter==0):
                checked.append(list_c_2[i])
                g=g+1
                x=list_c_2[i][0]
                y=list_c_2[i][1]
                z=[g,x,y]
                checked_2.append(z)
                g=g-1
                
            else:
                counter=0
           
        #if not checked_2:
        #    checked_2=pos_g_list
            
        
        return checked,checked_2
        

#def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    #while(pos!=goal):
        
        
        
        
    #return path

list_obstacles=find_obstacles(list_obstacles,grid)
error=0
while(pos!=goal):    
    try:    
        #print motion[0]    
        checked,movement=move(delta,motion[0],list_obstacles,checked,len_grid)
        #print movement    
        if(movement):
            for i in range(len(movement)):
                motion.append(movement[i])
    #print motion[0]
        motion.remove(motion[0])
        pos=[motion[0][1],motion[0][2]]
    except:
        print "fail"
        error=1
        break

if not error:    
    print motion[0]



#a,b1,c1=move(delta,pos_g_list,list_obstacles,checked,len_grid)
#print b1
#a,b2,c1=move(delta,b1[0],list_obstacles,checked,len_grid)
#print b2

#a,b3,c1=move(delta,b1[1],list_obstacles,checked,len_grid)
#print b3

#a,b4,c1=move(delta,b2[0],list_obstacles,checked,len_grid)
#print b4

#a,b5,c1=move(delta,b2[1],list_obstacles,checked,len_grid)
#print b5

#a,b6,c1=move(delta,b4[0],list_obstacles,checked,len_grid)
#print b6

#a,b7,c1=move(delta,b4[1],list_obstacles,checked,len_grid)
#print b7
