
import os, glob
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pathlib import Path

def append_images(images, direction='horizontal',
                  bg_color=(255,255,255), aligment='center'):
    """
    Appends images in horizontal/vertical direction.

    Args:
        images: List of PIL images
        direction: direction of concatenation, 'horizontal' or 'vertical'
        bg_color: Background color (default: white)
        aligment: alignment mode if images need padding;
           'left', 'right', 'top', 'bottom', or 'center'

    Returns:
        Concatenated image as a new PIL image object.
    """
    widths, heights = zip(*(i.size for i in images))

    if direction=='horizontal':
        new_width = sum(widths)
        new_height = max(heights)
    else:
        new_width = max(widths)
        new_height = sum(heights)

    margin = 50 # margin between images
    offset = margin # offset from Top-Left
    

    if direction=='horizontal':
        new_width += (len(images) + 1)*margin
    else:
        new_height += (len(images) + 1)*margin

    new_im = Image.new('RGB', (new_width, new_height), color=bg_color)
    for im in images:
        if direction=='horizontal':
            y = margin
            if aligment == 'center':
                y = int((new_height - im.size[1])/2)
            elif aligment == 'bottom':
                y = new_height - im.size[1]
            new_im.paste(im, (offset, y))
            offset += im.size[0] 
        else:
            x = margin
            if aligment == 'center':
                x = int((new_width - im.size[0])/2)
            elif aligment == 'right':
                x = new_width - im.size[0]
            new_im.paste(im, (x, offset))
            offset += im.size[1] # - 2*margin
        offset += margin
        # print("offset: {}".format(offset))

    return new_im

def img_add_txt(file):
    blank_image = Image.open(file)
    # print(np.array(blank_image).shape)
    h = np.array(blank_image).shape[0]
    w = np.array(blank_image).shape[1]
    img_draw = ImageDraw.Draw(blank_image)

    font = ImageFont.truetype("calibrib.ttf", 500) # timesbd.ttf
    txt = os.path.split(file)[-1].split('T')[0][-4:]
    img_draw.text((50, 50), f"{txt}", fill='white', font=font)
    # img_draw.text((np.floor(h*0.1), np.floor(w*0.9)), f"{txt}", fill='white', font=font)
    # blank_image.save(savePath / f"{os.path.split(file)[-1]}")
    return blank_image

if __name__ == "__main__":

    fireName = 'AugustComplex' #  "CAL_Creek"  # 
    rootPath = Path(f"E:\Wildfire_Events_2020\Results_Analysis\{fireName}")
    dataPath = Path(glob.glob(str(rootPath / f"Progression*"))[0])

    print(dataPath)
    folderList = sorted(os.listdir(dataPath))
    print(folderList)

    savePath = rootPath / "imgArray"
    if not os.path.exists(savePath):
        os.mkdir(savePath)

    ratio = 0.2 # scale ratio
    saveName = 'imgArray_{}'.format(ratio)

    print("\n\n===================> Start to Arrange Images Into Image Array <====================")


    rowList = []
    for folder in folderList:
        fileNameList = glob.glob(str(dataPath / folder / f"*.png"))

        if 'rgb' in folder:
            imageList = list(map(img_add_txt, fileNameList))
        else:
            imageList = list(map(Image.open, fileNameList))

        row = append_images(imageList, direction='horizontal')
        rowList.append(row)

    imgArray = append_images(rowList, direction='vertical')
    w, h = imgArray.size

    imgArray_scaled = imgArray.resize((int(np.floor(w*ratio)), int(np.floor(h*ratio))))

    print("----------------------------------------------------------------------------------")
    print("savePath: {}".format(savePath))
    imgArray_scaled.save(savePath / f"{fireName}_imgArray_{ratio}.png")
    imgArray_scaled.save(savePath / f"{fireName}_imgArray_{ratio}.pdf")
    print("===========================> Finished and be Saved! <=============================")




