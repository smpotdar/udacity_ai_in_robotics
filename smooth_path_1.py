# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 11:49:40 2015

@author: ShubhankarP
"""

# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and 
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite 
# correct).
# -----------
import matplotlib.pyplot as plt
from copy import deepcopy

# thank you to EnTerr for posting this on our discussion forum


#print newpath{}    

def printpaths(path,newpath):
    for old,new in zip(path,newpath):
        print '['+ ', '.join('%.3f'%x for x in old) + \
               '] -> ['+ ', '.join('%.3f'%x for x in new) +']'

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    newpath = deepcopy(path)
    change=0
    change_1=0
    change_2=0
    #timer=0
    #limit=5000
    #while(change>t)
    while True:    
        for i in range(1,len(path)-1):
            #if(newpath[i][0]-pat)
            x1=newpath[i][0]
            y1=newpath[i][1]
            newpath[i][0]=newpath[i][0]+weight_data*(path[i][0]-newpath[i][0])+weight_smooth*(newpath[i+1][0]+newpath[i-1][0]-2*newpath[i][0])
            newpath[i][1]=newpath[i][1]+weight_data*(path[i][1]-newpath[i][1])+weight_smooth*(newpath[i+1][1]+newpath[i-1][1]-2*newpath[i][1])
            x2=newpath[i][0]
            y2=newpath[i][1]
            change=change+abs(x2-x1)+abs(y2-y1)
            #newpath[i][0]=newpath[i][0]+weight_smooth*(newpath[i+1][0]+newpath[i-1][0]-2*newpath[i][0])
            #newpath[i][1]=newpath[i][1]+weight_smooth*(newpath[i+1][1]+newpath[i-1][1]-2*newpath[i][1])
            #x3=newpath[i][0]
            #y3=newpath[i][1]
            #change=change+abs(x3-x2)+abs(y3-y2)
        
        change_1=change
        delta=abs(change_2-change_1)
        change_2=change_1
        
        if(delta<tolerance):
            break
         
        if(delta>=tolerance):
            #print change
            change=0
            
        
    #######################
    ### ENTER CODE HERE ###
    #######################
    
    return newpath # Leave this line for the grader!

def plot_vector(path_vec):
    a=[]
    b=[]
    for i in range(len(path_vec)):
        a.append(path_vec[i][0])
        b.append(path_vec[i][1])
 
    plt.plot(b, a, 'ro')
    plt.axis([-1, 5, -1, 5])
    plt.show()

newpath=smooth(path, weight_data = 0.1, weight_smooth = 0.5, tolerance = 0.000001)
print newpath
plot_vector(newpath)
#plot_vector(path)

#plot_vector(smooth(path))
#print newpath
    
#printpaths(path,smooth(path))
