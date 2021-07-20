from psd_tools import PSDImage
from name_variables import Var


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


bbox_ = [[1296, 0], [0, 854], [2976, 0], [4325, 857]]
green_bbox_, rug_bbox_, l_bbox_ = extract_psd_name()
class_content = Var.class_content.format(str('BedRoom'), bbox_, green_bbox_[1], green_bbox_[0], rug_bbox_)
class_content = class_content.replace('$', '{')
class_content = class_content.replace('*', '}')
file = open('util.py', 'w+')
file.write(class_content)
file.close()