# -*- coding: utf-8 -*-
"""
Created on Sun Dec 06 12:05:04 2015

@author: ShubhankarP
"""

#Modify the program to find and print the sum of all 
#the entries in the list p.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
pHit = 0.6
pMiss = 0.2

p[0]=p[0]*pMiss
p[1]=p[1]*pHit
p[2]=p[2]*pHit
p[3]=p[3]*pMiss
p[4]=p[4]*pMiss

s=0

for x in range(0,5):
    s=s+p[x]
    
print s 

# Enter your code below
