

from PIL import Image, ImageDraw, ImageColor
from pathlib import Path
import os, glob
# from images2gif import writeGif
# ok

def img_mask(file):
    im_rgb = Image.open(file)
    # im_rgb.putpalette([0, 0, 0,
    #                 255, 255, 255])
    im_a = im_rgb.convert('L')
    im_rgba = im_rgb.copy()
    im_rgba.putalpha(im_a)
    return im_rgba


dataPath = Path(f"E:\Wildfire_Events_2020\Results_Analysis\elephant_progression_show\elephant\\1_transfer_to_elephant")
savePath = dataPath / "gif_results"
if not os.path.exists(savePath): os.mkdir(savePath)

fileList = sorted(glob.glob(str(dataPath / "*.png")))
# print(fileList)
imgMaskedList = list(map(img_mask, fileList))

imgMaskedList[0].show()

# imgMaskedList[0].save(savePath / 'out.gif', format='GIF', save_all=True, 
#                     append_images=imgMaskedList[1:],
#                     optimize=False, duration=600, loop=0)



# im_rgba.save(f"trans_{imgName}.png")
# im_rgba.show()