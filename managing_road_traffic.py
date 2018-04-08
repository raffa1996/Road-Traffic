import numpy 
import cv2
from PIL import Image, ImageDraw, ImageFont
POLYGON_MASK = [
    (0, 0),
    (0, 288),
    (44, 288),
    (140, 125),
    (160, 125),
    (164, 288),
    (352, 288),
    (352, 0),
]
def count_edge_pixels(opencv_image):
    count = 0

    width, height = opencv_image.shape[:2]

    for x in range(0, width):
        for y in range(0, height):
            if opencv_image[x, y] == 255:
                count = count + 1

    return count

def count_unmasked_pixels(pil_image):
    pixels = pil_image.load()

    count = 0

    for x in range(0, pil_image.size[0]):
        for y in range(0, pil_image.size[1]):
            if pixels[x, y] != (0, 0, 0):
                count = count + 1

    return count
def calculate_img_pixels(file_path): 
    image = Image.open(file_path)
    ImageDraw.Draw(image).polygon(POLYGON_MASK, fill=(0, 0, 0))
    unmasked_pixels = count_unmasked_pixels(image)
    opencv_image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
    edged_image = cv2.Canny(opencv_image, 100, 200)
    cv2.imwrite('C:/Users/win7/Desktop/Traffic/02251.png', edged_image)
    edge_pixels = count_edge_pixels(edged_image)
    T = round(float(edge_pixels) / float(unmasked_pixels), 6) 
    pix = str(T)
    img = Image.open(file_path)
    font_type = ImageFont.truetype('C:/Users/win7/Desktop/arial.ttf', 50)
    draw = ImageDraw.Draw(img)
    draw.text(xy=(10,10), text=pix,fill=(235,69,0),font=font_type)
    img.show()
    
    
calculate_img_pixels('C:/Users/win7/Desktop/Traffic/scene02251.png')



    