# -*- coding: utf-8 -*-
"""
Created on Sun Dec 06 12:03:42 2015

@author: ShubhankarP
"""

#Write code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.


p=[0.2,0.2,0.2,0.2,0.2]
world=['green','red','red','green','green']
pHit = 0.6
pMiss = 0.2
for i in range(0,len(p)):
    if world[i]=='green':
        p[i]=p[i]*pMiss
     
    if world[i]=='red':
        p[i]=p[i]*pHit
#Enter code here

print p