from PIL import Image 
from os.path import join

image1 = Image.open(join('resources', 'img1.jpg')).convert('RGB')
image2 = Image.open(join('resources', 'img2.png')).convert('1')

image1.paste(image2, (100,400))

image1.show()