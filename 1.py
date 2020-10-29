from PIL import Image
ASCII_CHAR=['&','#','$','%','?','*','+',';',':','.',' ']
import numpy as np
def to_gray(image):
    return image.convert('L')
def resize(image,width,height):
    resized_image=image.resize((width,height))
    return resized_image
def pixel_to_ascii(image):
    pixel=image.getdata()
    characters="".join([ASCII_CHAR[pixels//25] for pixels in pixel])
    return characters
image =Image.open('sup.jpg').convert('L')
width=200
new_data=pixel_to_ascii(to_gray(resize(image,width,width//2)))
l=len(new_data)
k="\n".join([new_data[i:i+width] for i in range(0,l,width)])
with open("ascii_img.txt","w") as f:
    f.write(k)