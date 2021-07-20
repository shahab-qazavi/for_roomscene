from name_variables import Var
import numpy as np
import cv2


def remove_background(image, result_name):
    try:
        # read image
        img = cv2.imread(image)

        # convert image to gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # create mask from image with threshold
        _, mask = cv2.threshold(gray, 245, 255, cv2.THRESH_BINARY)

        # In previous step we create mask from surrounding margins of image, mask is white and object of image is black
        # and we have to reverse it.

        # reverse mask : white to black, black to white
        mask = 255 - mask

        # create an matrix one to one for remove noises
        kernel = np.ones((1, 1), np.uint8)

        # remove noises
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # blur mask
        mask = cv2.GaussianBlur(mask, (0, 0), sigmaX=1, sigmaY=1, borderType=cv2.BORDER_DEFAULT)

        mask = (2*(mask.astype(np.float32))-255.0).clip(0, 255).astype(np.uint8)

        # create a copy from image
        result = img.copy()

        # convert origin image to transparent
        result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)

        # negative mask from transparent image
        result = cv2.bitwise_and(result, result, mask=mask)
        result[:, :, 3] = mask

        # save image
        cv2.imwrite(f'{result_name}.png', result)
    except Exception as e:
        print(e)

# print(np.ones((1,3), np.uint8))
remove_background('with white.jpg', Var.transparent_carpet)
# remove_background('carpet.png', 'alaki')
"""
img = cv2.imread('carpet.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, mask = cv2.threshold(gray, 245, 255, cv2.THRESH_BINARY)

mask = 255 - mask

kernel = np.ones((1, 1), np.uint8)

mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.GaussianBlur(mask, (1, 1), sigmaX=2, sigmaY=2, borderType=cv2.BORDER_DEFAULT)

mask = (2*(mask.astype(np.float32))-255.0).clip(0, 255).astype(np.uint8)
msko = [i for i in mask if all(i)]
result2 = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite('result2.PNG', result2)
result = img.copy()
result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
result_copy = result.copy()
res = cv2.bitwise_and(result, result, mask=mask)
cv2.imwrite('testmode.png', res)
result[:, :, 3] = mask
cv2.imwrite(f'{Var.transparent_carpet}.png', result)
"""





# display result, though it won't show transparency
# cv2.imshow("INPUT", img)
# cv2.imshow("GRAY", gray)
# cv2.imshow("MASK", mask)
# cv2.imshow("RESULT", msko)
# cv2.waitKey()
# cv2.destroyAllWindows()


# img = cv2.imread(Var.carpet)
# img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
# lower_white = np.array([0,0,0])
# upper_white = np.array([0,0,255])
# mask = cv2.inRange(img_hsv, lower_white, upper_white)
# cv2.imshow('mask',mask)
#
# output = cv2.bitwise_and(img_hsv, img_hsv, mask=mask)
#
# cv2.waitKey(0)
# cv2.destroyWindow('mask')
# for msk, org_img in zip(mask, img):
#     print('mask')
#     print(msk)
#     print('image')
#     print(org_img)
#     print('--------------')








# cv2.imwrite("img.png", output)
# print(mask0)
# # upper mask (170-180)
# lower_red = np.array([170,50,50])
# upper_red = np.array([180,255,255])
# mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
#
# # join my masks
# # mask = mask0+mask1
# mask = cv2.bitwise_or(mask0, mask1)
#
# # set my output img to zero everywhere except my mask
# output_img = img.copy()
# output_img[np.where(mask==0)] = 0
#
# # or your HSV image, which I *believe* is what you want
# output_hsv = img_hsv.copy()
# output_hsv[np.where(mask==0)] = 0
#
# cv2.imwrite("img.png", output_img)
# cv2.imwrite("hsv.png", output_hsv)