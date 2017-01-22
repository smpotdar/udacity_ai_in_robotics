# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 23:20:21 2015

@author: ShubhankarP
"""

# -----------
# User Instructions
#
# Implement a PD controller by running 100 iterations
# of robot motion. The steering angle should be set
# by the parameter tau so that:
#
# steering = -tau_p * CTE - tau_d * diff_CTE
# where differential crosstrack error (diff_CTE)
# is given by CTE(t) - CTE(t-1)
#
# Your code should print output that looks like
# the output shown in the video.
#
# Only modify code at the bottom!
# ------------
 
from math import *
import random
import matplotlib.pyplot as plt


# ------------------------------------------------
# 
# this is the robot class
#

class robot:

    # --------
    # init: 
    #    creates robot and initializes location/orientation to 0, 0, 0
    #

    def __init__(self, length = 20.0):
        self.x = 0.0
        self.y = 0.0
        self.orientation = 0.0
        self.length = length
        self.steering_noise = 0.0
        self.distance_noise = 0.0
        self.steering_drift = 0.0

    # --------
    # set: 
    #	sets a robot coordinate
    #

    def set(self, new_x, new_y, new_orientation):

        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation) % (2.0 * pi)


    # --------
    # set_noise: 
    #	sets the noise parameters
    #

    def set_noise(self, new_s_noise, new_d_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.steering_noise = float(new_s_noise)
        self.distance_noise = float(new_d_noise)

    # --------
    # set_steering_drift: 
    #	sets the systematical steering drift parameter
    #

    def set_steering_drift(self, drift):
        self.steering_drift = drift
        
    # --------
    # move: 
    #    steering = front wheel steering angle, limited by max_steering_angle
    #    distance = total distance driven, most be non-negative

    def move(self, steering, distance, 
             tolerance = 0.001, max_steering_angle = pi / 4.0):

        if steering > max_steering_angle:
            steering = max_steering_angle
        if steering < -max_steering_angle:
            steering = -max_steering_angle
        if distance < 0.0:
            distance = 0.0


        # make a new copy
        res = robot()
        res.length         = self.length
        res.steering_noise = self.steering_noise
        res.distance_noise = self.distance_noise
        res.steering_drift = self.steering_drift

        # apply noise
        steering2 = random.gauss(steering, self.steering_noise)
        distance2 = random.gauss(distance, self.distance_noise)

        # apply steering drift
        steering2 += self.steering_drift

        # Execute motion
        turn = tan(steering2) * distance2 / res.length

        if abs(turn) < tolerance:

            # approximate by straight line motion

            res.x = self.x + (distance2 * cos(self.orientation))
            res.y = self.y + (distance2 * sin(self.orientation))
            res.orientation = (self.orientation + turn) % (2.0 * pi)

        else:

            # approximate bicycle model for motion

            radius = distance2 / turn
            cx = self.x - (sin(self.orientation) * radius)
            cy = self.y + (cos(self.orientation) * radius)
            res.orientation = (self.orientation + turn) % (2.0 * pi)
            res.x = cx + (sin(res.orientation) * radius)
            res.y = cy - (cos(res.orientation) * radius)

        return res

    def __repr__(self):
        return '[x=%.5f y=%.5f orient=%.5f]'  % (self.x, self.y, self.orientation)

############## ADD / MODIFY CODE BELOW ####################

# ------------------------------------------------------------------------
#
# run - does a single control run.

def plot_vector(a,b):   
    plt.plot(a, b, 'ro')
    #plt.axis([0, 100, -2, 2]) #original
    plt.axis([-100, 100, -100, 100])
    plt.show()

def run(param1, param2):
    myrobot = robot()
    #myrobot.set(0.0, 1.0, 0.0) #original
    myrobot.set(-1.0, -2.0, 3*pi/4)
    speed = 1.0 # motion distance is equal to speed (we assume time = 1)
    #N = 100   #original
    N = 500
    #myrobot.set_steering_drift(10.0/180.0 * pi)
    cte_new=myrobot.y
    cte_old=myrobot.y
    tau_p=param1
    tau_d=param2
    a=[]
    b=[]
    for i in range(N):
        
        diff_cte=cte_new-cte_old
        cte_old=cte_new
        steering = -tau_p * cte_new - tau_d * diff_cte
        myrobot=myrobot.move(steering, speed)
        cte_new=myrobot.y
        a.append(myrobot.x)
        b.append(myrobot.y)
        
        #a.append(myrobot.x)
        #b.append(myrobot.y)
        print myrobot,steering
    
    plot_vector(a,b)
        
    # Enter code here
    #

# Call your function with parameters of 0.2 and 3.0 and print results
run(0.2, 3.0)



