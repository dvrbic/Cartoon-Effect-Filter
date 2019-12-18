import cv2 
import numpy as np

if __name__ == '__main__':
   input_image = cv2.imread('snowglobe_colour.png',1)
   output_image = input_image.copy()

def medfilter(in_img,rad): #Median Filter function that's called upon
    img = np.copy(in_img) #Creates a copy image
    mid = 2*rad*rad+2*rad+1 #  a is the radius of the filter, mid is the middle value of the mask
    r = []
    g = []
    b = [] #RGB array
    for i in range(in_img.shape[0]):
        for j in range(in_img.shape[1]):
            if i<rad or i>(in_img.shape[0]-(rad+1)) or j<rad or j>(in_img.shape[1]-(rad+1)):#Checks to see if the mask is within the range of the image
                pass #does nothing if not within range
            else:
                r.clear();g.clear();b.clear() #makes sure the arrays don't contain values before the mask is passed over them
                for x in range(-1*rad,rad+1):
                    for y in range(-1*rad,rad+1): #loops the 2d dimensions of the mask with corresponding radius
                        r.append(in_img[i+x,j+y][0])
                        g.append(in_img[i+x,j+y][1])
                        b.append(in_img[i+x,j+y][2]) #takes each color value when convolved with mask and appends to their arrays
                #Each array is sorted in ascending order    
                r.sort()
                g.sort()
                b.sort() 
                # The middle value mid is taken from each color array and placed in the image
                img[i,j]=(r[mid],g[mid],b[mid]) # The middle value mid is taken from each color array and placed in the image
    return img

def filterset(img): #puts the image through 3 different filters
    img_output = np.copy(img)
    img_output = medfilter(img,4) #sends the image through a median filter function with a radius of 4
    img_output = medfilter(img_output,3) #repeats previous step for radius of 3
    img_output = medfilter(img_output,2) #repeats previous step for radius of 2
    return img_output

if __name__ == '__main__':
   output_image = filterset(input_image) #Output image calling upon multiple filters method
   cv2.imwrite('Medfiltered_snowglobe_RGB.png',output_image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
