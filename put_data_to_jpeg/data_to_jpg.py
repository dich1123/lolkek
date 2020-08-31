from PIL import Image, JpegImagePlugin as JIP
from encode_string import Encoder


class ImageModifier:

    def __init__(self, photo_path):
        self.photo_path = photo_path
        self.image = Image.open(photo_path)

    def put_data_to_image(self, data):
        img = Image.new(self.image.mode, self.image.size)
        pixels = self.image.load()
        pixels_new = img.load()
        size_x, size_y = img.size
        data_pieces = (data[x:x+2] for x in range(0, len(data), 2))
        for x in range(size_x):
            for y in range(size_y):
                r, g, b = pixels[x, y]
                r = bin(r)[2:]
                g = bin(g)[2:]
                b = bin(b)[2:]
                data_r = next(data_pieces, '')
                data_g = next(data_pieces, '')
                data_b = next(data_pieces, '')
                new_r = r[:-len(data_r) or len(r)] + data_r
                new_g = g[:-len(data_g) or len(g)] + data_g
                new_b = b[:-len(data_b) or len(b)] + data_b
                pixels_new[x, y] = (int(new_r, 2), int(new_g, 2), int(new_b, 2))

        new_file_name = '.'.join(self.photo_path.split('.')[:-1]) + '_new.' + 'png'
        img.save(new_file_name, subsampling=JIP.get_sampling(img))

    def get_data_from_image(self):  # stop symbol: 16 x 0
        pixels = self.image.load()
        size_x, size_y = self.image.size
        data = ''
        for x in range(size_x):
            for y in range(size_y):
                for color in pixels[x, y]:
                    data += bin(color)[-2:]
                    if data.endswith('0' * 16):
                        return data


encoder = Encoder(password='hello kniga', data='My name is potato! I very like to swim and drink vodka '
                                               'but only very cold, with ice, or maybe cocktail like White Russian'
                                               'Это все обо мне, а что ты скажешь о себе?')
encoder.encode()
string_to_img = encoder.prepare_to_file()
image = ImageModifier(photo_path='dima.jpg')
image.put_data_to_image(data=string_to_img)


encoder = Encoder(password='hello kniga', data='My name is potato!')
encoder.encode()
string_to_img = encoder.prepare_to_file()
print('to: ', string_to_img)
image = ImageModifier(photo_path='dima_new.png')
data = image.get_data_from_image()
print(data)
encoder = Encoder(password='hello kniga')
encoder.prepare_to_decode(data)
encoder.decode()
print(encoder.decode_data)