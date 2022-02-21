import cv2
import numpy as np

userInput = input("Enter the name of the image file with extension: ")
blurType = input(
    "What filter would you like to generate a kernel for?\nThe options are Blur, GBlur, MBlur: ")

# this loads the cascade
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# this specifies what photo we want
img = cv2.imread(userInput)

# facial detection code using method within openCV
faces = cascade.detectMultiScale(img, 1.05, 4)
if blurType == "Blur":
    # this constructs a rectangle around the detected faces and then blurs the area inside the rectangle.
    # this explains how a kernel matrix can be created then scaled for Blur and gaussianBlur functions
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        for y in range(0, w, 3):
            for x in range(0, h, 3):
                pix1 = img[x][y]
                pix2 = img[x][y+1]
                pix3 = img[x][y+2]
                pix4 = img[x+1][y]
                pix5 = img[x+1][y+1]
                pix6 = img[x+1][y+2]
                pix7 = img[x+2][y]
                pix8 = img[x+2][y+1]
                pix9 = img[x+2][y+2]

                average = (pix1/9. + pix2/9. + pix3/9. + pix4/9. + pix5 /
                           9. + pix6/9. + pix7/9. + pix8/9. + pix9/9.)  # this calculates the average value of the kernel matrix.
                
                # this sets the central pixel equal to the average of the pixel around it.
                img[x+1][y+1] = average
    print("The average values for the 3x3 matrix are:\n", average)

if blurType == "GBlur":
    print("This is the Gaussian Kernel for a blurring effect using a 3x3 matrix\n",
          cv2.getGaussianKernel(3, 0.0))

if blurType == "MBlur":
    for (x, y, w, h) in faces:
        for y in range(0, w, 3):
            for x in range(0, h, 3):
                pix1 = img[x][y]
                pix2 = img[x][y+1]
                pix3 = img[x][y+2]
                pix4 = img[x+1][y]
                pix5 = img[x+1][y+1]
                pix6 = img[x+1][y+2]
                pix7 = img[x+2][y]
                pix8 = img[x+2][y+1]
                pix9 = img[x+2][y+2]
                array = [pix1, pix2, pix3,
                         pix4, pix5, pix6, pix7, pix8, pix9]
                x = np.array(array)
    print("The 3x3 matrix is:\n", x)
