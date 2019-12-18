import numpy as np
import cv2
import math


if __name__ == '__main__': 
   input_image = cv2.imread('snowglobe_colour.png',1) #Reads the input image
   output_image = input_image.copy()

def threshfunc(in_img):
    img_out = np.copy(in_img)
    new_img = np.copy(in_img)
    vert_edge = np.array([[1,0,1],[0,0,0],[-1,0,-1]])
    horz_edge = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])#basic 3x3 edge detection filters for horizontal and vertical slices
    for i in range(new_img.shape[0]):
        for j in range(in_img.shape[1]):
            if i<1 or i>(in_img.shape[0]-2) or j<1 or j>(in_img.shape[1]-2):#skip borders of image
                pass
            else:
                vert = 0
                horz=0
                for x in range(-1,2):
                    for y in range(-1,2): #parameters to do the 3x3 filter in x and y axis
                        horz += new_img[i+x,j+y]*horz_edge[x+1,y+1]
                        vert += new_img[i+x,j+y]*vert_edge[x+1,y+1] #store values of image * filter for both edges
                img_out[i,j] = int(math.sqrt(math.pow(horz,2)+math.pow(vert,2))) # find magnitude 
                if img_out[i,j] > 80: #thresholding at near half intensity 
                    img_out[i,j] = 255
                else:
                    img_out[i,j] = 0 #lower the threshold, the more edges show
    return img_out

def Edge_Dectection_func(in_img):
    new_img = np.copy(in_img)
    img_grey = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY) # line turns the colored rgb image to grayscale
    r = np.copy(img_grey) #Each of the 3 colors will have the same size as
    g = np.copy(img_grey)
    b = np.copy(img_grey) 
    for i in range (in_img.shape[0]):
        for j in range (in_img.shape[1]):
            r[i,j] = new_img[i,j][0]
            g[i,j] = new_img[i,j][1]
            b[i,j] = new_img[i,j][2] #rgb extracted and saved in arrays r g b
    r = threshfunc(r)
    g = threshfunc(g)
    b = threshfunc(b) #thresholding the RGB image layers
    for x in range (in_img.shape[0]):
        for y in range (in_img.shape[1]):
            new_img[x,y][0]=r[x,y]
            new_img[x,y][1]=g[x,y]
            new_img[x,y][2]=b[x,y] # save new RGB image 

    return new_img

if __name__ == '__main__': 
   output_image  = Edge_Dectection_func(input_image) #calls upon edge detection function
   cv2.imwrite('threshed_snow.png',output_image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
