from PIL import Image, ImageDraw
import numpy as np
import skimage.morphology


def remove_background(img):
    img = Image.open('carpet in red.png')
    ImageDraw.floodfill(img, xy=(1, 1), value=(255, 0, 255), thresh=50)
    img.show()


remove_background('carpet.png')
