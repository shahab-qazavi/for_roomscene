from psd_tools import PSDImage, composite
from name_variables import Var
import time

from PIL import Image, ImageChops
import requests
import csv
# r = csv.reader(open('./test.csv'))
# writer = csv.writer(open('./test.csv', 'w'))
# for i in r:
#    if 'https' in i[3]:
#        split = i[3].split('/')
#        i[3] = "https://rmimages2.blob.core.windows.net/roomscene/design/" + split[4] + '/' + split[5]
#        print(i[3])
#        writer.writerows(r)
import io

# image = Image.open('./green.png')
# print(image.size)


psd = PSDImage.open(Var.psd_name)
for layer in psd:
    # bbox = (layer.bbox[0], layer.bbox[1])
    # if layer.name == Var.green_screen:
    #     Var.green_size = layer.size
    #     Var.green_bbox = bbox
    # elif layer.name == Var.top_layer:
    #     Var.layer1_bbox = bbox
    print(layer.name)
    print(layer.size)
    print(layer.bbox)
    layer_image = layer.composite()
    layer_image.save('%s.png' % layer.name, )


