import numpy 
import cv2
from PIL import Image, ImageDraw, ImageFont
MASK_POLYGON = [
    (0, 0),
    (0, 288),
    (44, 288),
    (140, 125),
    (160, 125),
    (164, 288),
    (352, 288),
    (352, 0),
]
def COUNT_THE_EDGE_PIXELS(OPENCV_IMAGE):
    COUNT = 0

    width, height = OPENCV_IMAGE.shape[:2]

    for i in range(0, width):
        for j in range(0, height):
            if opencv_image[i, j] == 255:
                COUNT = COUNT + 1

    return COUNT

def COUNT_THE_UNMASKED_PIXELS(PIL_img):
    pixels = PIL_img.load()

    COUNT = 0

    for i in range(0, PIL_img.size[0]):
        for j in range(0, PIL_img.size[1]):
            if pixels[i, j] != (0, 0, 0):
                COUNT = COUNT + 1

    return COUNT

def CALCULATE_THE_IMAGE_PIXELS(FILE_path): 
    image = Image.open(FILE_path)
    ImageDraw.Draw(image).polygon(MASK_POLYGON, fill=(0, 0, 0))
    unmasked_pixels = COUNT_THE_UNMASKED_PIXELS(image)
    opencv_image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
    edged_image = cv2.Canny(opencv_image, 100, 200)
    cv2.imwrite(FILE_path, edged_image)
    edge_pixels = COUNT_THE_EDGE_PIXELS(edged_image)
    T = round(float(edge_pixels) / float(unmasked_pixels), 6) 
    pix = str(T)
    img = Image.open(file_path)
    font_type = ImageFont.truetype('C:/Users/win7/Desktop/arial.ttf', 50)
    draw = ImageDraw.Draw(img)
    draw.text(xy=(10,10), text=pix,fill=(235,69,0),font=font_type)
    img.show()
    
    
calculate_img_pixels(FILE_path)



    
