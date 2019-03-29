import numpy as np
import cv2

def Template_Matching(image_T,image_I):

    image_T=np.float64(image_T)
    image_I=np.float64(image_I)

    #Get the size of the Image Template
    rows_t,cols_t=image_T.shape

    #Get the size of the Input Image
    rows_i,cols_i=image_I.shape

    #Generating Matching map
    H_r=rows_i-rows_t+1
    W_r=cols_i-cols_t+1
    MatchingMap=np.zeros(shape=(H_r,W_r))

    #Calculating the Matching map
    for i in range(0,H_r):
        for j in range(0,W_r):
            MatchingMap[i,j]=CalculatePixel(image_T,image_I,i,j,rows_t,cols_t)


    return MatchingMap


def CalculatePixel(image_t,image_i,i,j,height_t,width_t):


    matrix=image_t.copy()-image_i[i:i+height_t,j:j+width_t].copy()
    matrix=matrix**2

    return matrix.sum()/image_t.sum()


def ReturnResult(MatchMap,image_t,image_i,threshold):

    minpix=np.min(MatchMap)
    maxpix=np.amax(MatchMap)

    rows_mm,cols_mm=MatchMap.shape
    rows_t,cols_t=image_t.shape
    counter=0

    if minpix/maxpix<=threshold:
        for i in range(0,rows_mm):
            for j in range(0,cols_mm):
                if MatchMap[i,j]==minpix:
                    cv2.rectangle(image_i,(j,i),(j+cols_t,i+rows_t),(0,255,0),1)

        cv2.imshow("input image",image_i)
        print("Target found ",counter," times")

    else:
        print("Target not-found")


if __name__=="__main__":
    print("practise_1")
    image_I=cv2.imread("img2.png",cv2.IMREAD_GRAYSCALE)
    image_T=cv2.imread("t2-img2.png",cv2.IMREAD_GRAYSCALE)
    color_I=cv2.imread("img2.png",cv2.IMREAD_ANYCOLOR)
    color_T=cv2.imread("t2-img2.png",cv2.IMREAD_ANYCOLOR)

    cv2.imshow("input image",image_I)
    cv2.imshow("Template image",image_T)

    MatchMap=Template_Matching(image_T,image_I)
    cv2.imshow("Matching map",np.uint8(MatchMap))

    ReturnResult(MatchMap,image_T,color_I,0.1)

    cv2.waitKey(0)



