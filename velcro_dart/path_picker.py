import cv2
import numpy as np
import pickle

polygons=[] #All the polygons and thier Points
path=[] #Current Single Polygon

img=cv2.imread('imgBoard.png')

def mousePoints(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        path.append([x,y])
while True:
    for point in path:
        cv2.circle(img,point,7,(0,255,0),cv2.FILLED)

    pts=np.array(path,np.int32).reshape((-1,1,2))
    img=cv2.polylines(img , [pts] ,True , (255,0,0), 2)
    #print(path)
    cv2.imshow("Image",img)
    cv2.setMouseCallback("Image",mousePoints)
    a=cv2.waitKey(1)
    if a==ord('q'):
        break
    elif a== ord('s'):
        score=int(input("Enter Score: "))
        polygons.append([path,score])
        print("Total Polygons:",len(polygons))
        path=[]
    elif a==ord('p'):
        with open('Polygons_1','wb') as f:
            print(polygons)
            pickle.dump(polygons,f)
        break