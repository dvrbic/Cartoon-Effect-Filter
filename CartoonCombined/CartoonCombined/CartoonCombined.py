import cv2 
import numpy as np
#imports the edge detector from previous part as well as the median filter files
from EdgeCartoon import Edge_Dectection_func
from MedianCartoon import filterset
if __name__ == '__main__': 
    #Reads input image
    input_image  = cv2.imread('mandrill.png',1)
    output_image = input_image .copy()


def CartoonFilter(in_img):
    new_img = np.copy(in_img)
    #sends the input image through the edge detector imported from the previous part to get highlighted edges
    edge_img = Edge_Dectection_func(new_img)
    #Sends the input image through the series of median filters imported from previous part
    median_img = filterset(new_img)
    #loops through the entire range of the image
    for i in range(in_img.shape[0]):
        for j in range(in_img.shape[1]):
            #If the loop encounters 0 intensity (non edges), the median filtered image is used
            if edge_img[i,j][0] ==0 and edge_img[i,j][1]==0 and edge_img[i,j][2]==0 :
                new_img[i,j] = median_img[i,j] 
            #Else, the intensity is made black or 0 intensity
            else:
                new_img[i,j] = 0
    #returns the cartoonie image            
    return new_img
if __name__ == '__main__': 
    #Calls upon CartoonFilter function
    output_image = CartoonFilter(input_image)
    cv2.imshow('Cartoonie',output_image)
    cv2.imwrite('Snowy_cartoon.jpg',output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
