import cv2 as cv
import numpy as np
import time
import copy


def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)


def main():
    # vidfilename="TestVid1.mp4"
    vidfilename="TestVid2.mp4"
    count =0
    pageBorder=0.8
    filename="IMG"
    filecount=1
    path="extract"
    al=[]
    with open("values.txt",mode="r") as MyFile:
        for x in MyFile:
            al.append(x)
    scale=float(al[0])
    frameskip=int(al[1])
    timegap=int(al[2])
    vidfilename=str(al[3])
    vidfilename=vidfilename.strip()
    choice=int(al[4])
    mul=float(al[5])
    frameskip+=1
    filename=path+"\\IMG1.png"
    print("started",vidfilename,"-")
    if(choice==0):
        capture = cv.VideoCapture("D:\\Alans-Folder\\projects\\BigO Project\\Seoul - 21985.mp4")
    elif( choice ==1):
        capture = cv.VideoCapture(0)
    else:
        capture = cv.VideoCapture("TestVid1.mp4")
    isTrue, framefull=capture.read()
    while(True):
        isTrue, frame=capture.read()
        count+=1
        if(isTrue==False):
            break
        if(choice==1):
            frame=cv.flip(frame,1)
        if(count==frameskip):
            sumimg=frame.astype(float)
            avgimg=None
            print("paged")
        sumimg+=frame.astype(float)        
        avgimg=(sumimg/count)
        avgimg=avgimg.astype("uint8")
        cv.imshow("frame",frame)
        cv.imshow("avg",avgimg)
        if( cv.waitKey(timegap) & 0xFF==ord('d')):
            break    

    avgimg=sumimg*(mul/count)
    avgimg=avgimg.astype("uint8")
    cv.imshow("avg",avgimg.astype("uint8"))
    cv.imwrite("Long Shot.png",avgimg)
    if( cv.waitKey(10000) & 0xFF==ord('d')):
        print("end")
    capture.release()
    
    cv.destroyAllWindows()

    cv.waitKey(0)


main()
