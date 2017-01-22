import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    #global ix,iy    
    if event == cv2.EVENT_LBUTTONDOWN:
	x_dash=x/divisions
	y_dash=y/divisions
	if(map_matrix[y_dash][x_dash]==0):
		map_matrix[y_dash][x_dash]=1		
		
	else:
		map_matrix[y_dash][x_dash]=0	
		



def print_matrix(matrix):
	for i in range(len(matrix)):
		print matrix[i]


cap = cv2.VideoCapture(0)	
ret, frame = cap.read()
height,width=frame.shape[:2]
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',draw_circle)
divisions=80
h=height/divisions
w=width/divisions
map_matrix=[[0 for rows in range(w)] for cols in range(h)]
	
p=0#cv2.circle(img,(20,20),5,(0,0,255),-1)
while(1):
    ret, frame = cap.read()
    for i in range(w+1):
	for j in range(h+1):
		cv2.circle(frame,(i*divisions,j*divisions),2,(0,0,255),-1)

    for i in range(len(map_matrix)):
	for j in range(len(map_matrix[0])):
		if(map_matrix[i][j]==1):
			x1=j*divisions
			y1=i*divisions
			x2=x1+divisions
			y2=y1+divisions
			cv2.rectangle(frame, (x1, y1), (x2, y2), (255,0,0), -1)
						
				
    cv2.imshow('frame',frame)	
    #cv2.imshow('image',img)	
    if cv2.waitKey(10) & 0xFF == ord('p'):
	p=1
    
    if(p==1):
	print "Map:"
	print_matrix(map_matrix)
	p=0		
    if cv2.waitKey(10) & 0xFF == 27:
        break
cv2.destroyAllWindows()
