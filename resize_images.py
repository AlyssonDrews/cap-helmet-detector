from PIL import Image
from glob import glob

path = ('positivas/')
files = glob(path + '/*')

for file in files:
    img = Image.open(file)
    width, height = img.size
    (new_width, new_height) = (width*2, height*2)
    img = img.resize((500,500), Image.ANTIALIAS)

    img.save(file, format='png')
    print(img.size)