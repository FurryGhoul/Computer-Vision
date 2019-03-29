
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
                    cv2.rectangle(image_i,(j,i),(j+cols_t,i+rows_t),(0,255,0),2)
                    counter+=1

        cv2.imshow("input image",image_i)
        print("Target found ",counter," times")
        image_found = np.zeros((40, 245, 3), np.uint8)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image_found, "TARGET FOUND", (5, 30), font, 1, (0, 255, 0), 2)
        cv2.imshow("Result", image_found)

    else:
        cv2.imshow("input image", image_i)
        print("Target not-found")
        image_found = np.zeros((40, 335, 3), np.uint8)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image_found, "TARGET NOT FOUND", (5, 30), font, 1, (0, 255, 255), 2)
        cv2.imshow("Result", image_found)


if __name__=="__main__":
    print("practise_1")

    error = True
    while error == True:
        name_template = input('Enter template image: ')
        try:
            f = open(name_template)
        except FileNotFoundError:
            print('File not found')
        else:
            error = False
            print('Image found. Opening', name_template)
            image_T=cv2.imread(name_template,cv2.IMREAD_GRAYSCALE)
            color_T=cv2.imread(name_template,cv2.IMREAD_ANYCOLOR)

    error = True
    while error == True:
        name_input = input('Enter input image: ')
        try:
            f = open(name_input)
        except FileNotFoundError:
            print('File not found')
        else:
            error = False
            print('Image found. Opening', name_input)
            image_I=cv2.imread(name_input,cv2.IMREAD_GRAYSCALE)
            color_I=cv2.imread(name_input,cv2.IMREAD_ANYCOLOR)

    threshold = float(input('Enter threshold: '))

    cv2.imshow("input image",image_I)
    cv2.imshow("Template image",image_T)

    MatchMap=Template_Matching(image_T,image_I)
    cv2.imshow("Matching map",np.uint8(MatchMap))

    ReturnResult(MatchMap,image_T,color_I,threshold)

    cv2.waitKey(0)




