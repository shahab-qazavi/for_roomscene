import cv2
import numpy as np
from PIL import Image
from psd_tools import PSDImage
import io
from opencv_mask import remove_background
from blend_modes import multiply
from name_variables import Var
bbox = [[-15, 1268], [5281, 1268], [1350, -3], [3308, -3]]
# bbox = [[0, 1268], [5281, 1268], [1375, -1], [3308, -1]]


def open_transparent_image(file_name):
    try:
        src = cv2.imread(file_name, cv2.IMREAD_UNCHANGED)
        bgr = src[:, :, :3]
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        alpha = src[:, :, 3]
        result = np.dstack([bgr, alpha])
    except Exception as e:
        print(e)
        return cv2.imread(file_name)
    return result


def extract_psd_name():
    green_bbox = ''
    rug_bbox = ''
    l_bbox = ''
    psd = PSDImage.open(Var.psd_name)
    for layer in psd:
        bbox = (layer.bbox[0], layer.bbox[1])
        if layer.name == Var.green_screen:
            green_bbox = layer.size
            rug_bbox = bbox
        elif layer.name == Var.top_layer:
            l_bbox = bbox
    return green_bbox, rug_bbox, l_bbox


def fit_image_into_smartObject(file_directory):
    try:
        Ratio = 1.48148
        # image = open_transparent_image(file_directory)
        # image = remove_background(image=file_directory, save=True)
        # image = cv2.imread(Var.carpet, cv2.IMREAD_UNCHANGED)
        image = cv2.imread(file_directory)
        green_layer = cv2.imread(f'{Var.green_screen}.png')



        # image = cv2.imread(Var.carpet)

        # cv2.imshow('image', image)
        # cv2.imwrite('testing.png',image)
        # cv2.waitKey()
        lower = np.array([35, 0, 0], dtype='uint8')
        upper = np.array([131, 255, 185], dtype='uint8')
        mask = cv2.inRange(green_layer, lower, upper)
        mask = mask.flatten()
        image = cv2.resize(image, (int(round(image.shape[0] / Ratio, 0)), image.shape[0]), interpolation=cv2.INTER_AREA)



        # image = cv2.resize(image, (green_size[0], green_size[1]), interpolation=cv2.INTER_AREA)

        points_A = np.float32([[0, 0], [int(round(image.shape[0] / Ratio, 0)), 0], [0, image.shape[0]],
                               [int(round(image.shape[0] / Ratio, 0)), image.shape[0]]])
        points_B = np.float32(bbox) #[[279, 0], [0, 200], [977, 3], [1092, 200]]
        M = cv2.getPerspectiveTransform(points_A, points_B)
        warped = cv2.warpPerspective(image, M, green_size) # size of green layer 1092, 200
        img = Image.fromarray(cv2.cvtColor(warped, cv2.COLOR_BGR2RGB))
        # img.show()
        img = img.convert("RGBA")
        # imo = Image.open(img)
        # img.show()
        datas = img.getdata()
        newData = []
        # temp = [x for x in range(0, 10)]
        # print(mask)
        # cv2.imshow('mask', mask)
        # cv2.imwrite('mask.png',mask)
        # cv2.waitKey()
        for d, m in zip(datas, mask):
            # if item[0] in temp and item[1] in temp and item[2] in temp:
            if m == 0:
                newData.append((0, 0, 0, 0))
            else:
                newData.append(d)
        # print(newData)
        # cv2.imshow('newdata', newData)
        # cv2.waitKey()
        buff = io.BytesIO()
        img.putdata(newData)
        # img.convert('RGBA')
        img.save(buff, "PNG")

        return buff
    except Exception as e:
        return print(str(e))


def rebuild_new_image():
    # try:
        room2_rug_bbocx = green_coordination #(,289, 1039
        PSDImage.open(Var.psd_name).composite().save(Var.png_name)
        room = Image.open(Var.png_name)
        room_C = room.copy()
        rug = Image.open(fit_image_into_smartObject(Var.carpet))
        # rug = np.array(rug)
        # rug = rug.astype(float)
        # shadow_cv = cv2.imread('./Shadows.png', -1).astype(float)
        layer1 = Image.open('./Top-Layer.png')
        layer_bbox = object_coordination #, 525, 903,
        # layer2 = Image.open('./Objects.png')
        layer_bbox2 = (319, 524,)
        # layer3 = Image.open('./Objects.png')
        layer_bbox3 = (464, 574)

        # blended = multiply(rug, shadow_cv, 0.5)
        # blended_img = np.uint8(blended)
        # blended_img_raw = Image.fromarray(blended_img)
        room_C.paste(rug, room2_rug_bbocx, rug)
        room_C.paste(layer1, layer_bbox, layer1)
        # room_C.paste(layer3, layer_bbox3, layer3)
        temp = io.BytesIO()
        room_C.save(temp, 'PNG', quality=95)
        res = Image.open(temp)
        res.save('1.png')
        res.show()
    # except Exception as e:
    #     return print(str(e))


# cv2.imshow('im',Var.carpet)
green_size, green_coordination, object_coordination = (5281, 1268), (-643, 1230), (-105, -54)
rebuild_new_image()
