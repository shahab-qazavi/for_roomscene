class Var:
    file_name = '04-GreanScrean'
    psd_name = f'./{file_name}.psd'
    png_name = f'./{file_name}.png'
    multiply = False
    transparent_carpet = 'transparent_carpet'
    # carpet = './test.png'
    # carpet = './carpet.png'
    carpet = './with white.jpg'
    # carpet = './carpet in red.png'
    # carpet = f'{transparent_carpet}.png'
    # carpet = 'carpet-removebg-preview.png'
    green_screen = 'Green-Screen'
    top_layer = 'Top-Layer'
    green_size = ''
    green_bbox = ''
    layer1_bbox = ''
    tag = ''
    class_content = """from Design.utils import Utils
import os
class BELLISSIMAFOUR2:
      @staticmethod
      def prpare(url, path, data):
            Utils(ratio=1.48148,
                  tag='{}',
                  info=data,
                  dest={},
                  height={},
                  width={},
                  bbox={},
                  url=url,
                  multiply=True,
                  room_addr=path+'/bellissimafour2.png',
                  imageName='test',
                  imagePath='hemmat/roomSceen',
                  additonals=$'full': True, 'image': [path+'/Shadows.png', path+'/Objects.png'],
                              'bbox': [(0, 596), (0, 116)]*).rebuild_new_image()
    """



