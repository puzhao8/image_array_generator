


import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import glob, os

dataPath = "E:\Sydney_WildFire_SAR_MSI_200m_EPSG_3577\Sydney_time_series_images_SWIR\\new\\"
savePath = dataPath + "add_txt_woKTH\\"

if not os.path.exists(savePath):
    os.mkdir(savePath)

fileNameList = glob.glob(dataPath + 'MSI*.png')

print("----------------------------")
print("Add text to Image: ")
for file in fileNameList:
    fileName = file.split("\\")[-1][:-4]
    print("Processing {} ...".format(fileName))

    # blank_image = Image.new('RGBA', (400, 300), 'white')
    blank_image = Image.open(dataPath + fileName + ".png")

    w, h, c = np.array(blank_image).shape
    # print(w, h, c)

    img_draw = ImageDraw.Draw(blank_image)
    # img_draw.rectangle((70, 50, 270, 200), outline='red', fill='blue')

    font = ImageFont.truetype("calibrib.ttf", 50) # timesbd.ttf
    txt = fileName.replace('MSI_', '').replace('_', '-')
    img_draw.text((np.floor(h*0.73), np.floor(w*0.02)), txt, fill='red', font=font)

    font2 = ImageFont.truetype("times.ttf", 50)  # timesbd.ttf
    # img_draw.text((np.floor(h * 0.9), np.floor(w * 0.95)), 'KTH', fill='lightblue', font=font2)

    blank_image.save(savePath + fileName + '.png')