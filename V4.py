import cv2 as cv
import numpy as np
import time
import copy

def main():
    # vidfilename="TestVid1.mp4"
    vidfilename="TestVid2.mp4"
    count =0
    al=[]
    with open("values.txt",mode="r") as MyFile:
        for x in MyFile:
            al.append(x)
    MyFile.close()
    vidfilename=str(al[3])
    vidfilename=vidfilename.strip()
    choice=int(al[4])
    multiplier=float(al[5])
    print("started",vidfilename,"-")
    sumimg=None
    if(choice==0):
        capture = cv.VideoCapture(vidfilename)
    else:
        capture = cv.VideoCapture("TestVid1.mp4")
    while(True):
        isTrue, frame=capture.read()
        count+=1
        if(isTrue==False):
            break
        if(choice==1):
            frame=cv.flip(frame,1)
        if sumimg is None:
            sumimg=frame.astype(float)
            avgimg=None
            print("paged")
        sumimg+=frame.astype(float) +(frame.astype(float)*(frame>250))      
    
    avgimg=(sumimg/count)*multiplier
    avgimg=avgimg.astype("uint8")
    cv.imshow("avg",avgimg)

    with open("count.txt",mode="r+") as f:
        ct=[]
        for x in f:
            ct.append(x)
        cv.imwrite("extract\\Long Shot"+str(int(ct[0]))+".png",avgimg)
        f.seek(0)
        f.write(str(int(ct[0])+1)+"\n")
        f.close()
    if( cv.waitKey(300) & 0xFF==ord('d')):
        print("end")
    capture.release()
    
    cv.destroyAllWindows()

    cv.waitKey(0)


main()