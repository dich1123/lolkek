from PIL import Image

pil_im = Image.open('cat.jpg')
box = (100, 100, 300, 900)
region = pil_im.crop(box)
region.show()
