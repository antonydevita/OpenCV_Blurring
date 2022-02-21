import cv2

userInput = input("Enter the name of the image file with extension: ")
blurType = input(
    "Choose a Filter: Blur, GBlur, MBlur, BFilter: ")

# this loads the cascade
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# this specifies what photo we want
img = cv2.imread(userInput)

# facial detection code using method within openCV
faces = cascade.detectMultiScale(img, 1.05, 4)
# draws a rectangle around the detected faces of each image
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# uses the blur function and returns the blurred face to blurredImage.jpg
if blurType == "Blur":
    strKernelSize = input(
        "The Blur method takes in an integer that represents n of an nxn kernel matrix. The greater the size of the matrix, the greater the blur effect.\nAny integer works, but a value of 175 or greater effectively blurs most images: ")
    kernelSize = int(strKernelSize)
    if kernelSize < 0:
        print("You have entered a negative number. Rerun the program")
        exit()
    for (x, y, w, h) in faces:
        img[y:y+h, x:x+w] = cv2.blur(img[y:y+h, x:x+w],
                                     (kernelSize, kernelSize))

    cv2.imwrite('./blurredImage.jpg', img)
    cv2.waitKey()
    print("The blurred photo can be found in the folder under blurredImage.jpg")
# uses the gaussianBlur function and returns the blurred face to gaussianBlurredImage.jpg
if blurType == "GBlur":
    strKernelSize = input("For our purposes, GaussianBlur functions very similarly to Blur. This input represents the size of an nxn kernel matrix.\nThe greater the size, the greater the blur effect. The integer must be positive and odd though. A value of 175 or greater effectively blurs most images: ")
    kernelSize = int(strKernelSize)
    if kernelSize < 0 or kernelSize % 2 == 0:
        print("You have entered an even number or a negative number. Rerun the program")
        exit()
    for (x, y, w, h) in faces:
        img[y:y+h, x:x +
            w] = cv2.GaussianBlur(img[y:y+h, x:x+w], (kernelSize, kernelSize), 0, 0)

    cv2.imwrite('./gaussianBlurredImage.jpg', img)
    cv2.waitKey()
    print("The blurred photo can be found in the folder under gaussianBlurredImage.jpg")
# uses the medianBlur function and returns the blurred face to medBlurredImage.jpg
if blurType == "MBlur":
    strBlurStrength = input(
        "Median Blur gets very blurry very fast, but does not require a lot of processing power.\nIt requires an odd integer that is greater than 1, the higher the number the more blurred: ")
    blurStrength = int(strBlurStrength)
    if blurStrength % 2 == 0:
        print("You have entered an even number. Rerun the program.")
        exit()
    for (x, y, w, h) in faces:
        img[y:y+h, x:x+w] = cv2.medianBlur(img[y:y+h, x:x+w], blurStrength)
    cv2.imwrite('./medBlurredImage.jpg', img)
    cv2.waitKey()
    print("The blurred photo can be found in the folder under medBlurredImage.jpg")
# uses the bilateralFilter function and returns the filtered face to bFilterImage.jpg
if blurType == "BFilter":
    strSigmaSpace = input("Bilaterial Filtering takes a lot of processing power, give an integer that represents how filtered you would like the image.\nNote that values of 100+ can take a long time to return and may not work if you dont have enough power: ")
    sigmaSpace = int(strSigmaSpace)
    if sigmaSpace < 0:
        print("You have entered a negative number. Rerun the program")
        exit()
    for (x, y, w, h) in faces:
        img[y:y+h, x:x +
            w] = cv2.bilateralFilter(img[y:y+h, x:x+w], sigmaSpace, 150, 150)
    cv2.imwrite('./bFilterImage.jpg', img)
    cv2.waitKey()
    print("The filtered photo can be found in the folder under bFilterImage.jpg")
