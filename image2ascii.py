from PIL import Image
from sys import argv


class AsciiImage:

    STANDARD_SCALE = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
    EXPRESS_SCALE = '@%#*+=-:. '

    def __init__(self, image, scale=1):
        self._image = (image.resize(map(lambda x: int(x * scale), image.size)) \
                            if scale != 1 else image).convert('L')

    def convert(self, gray_scale=STANDARD_SCALE):
        sc_len = len(gray_scale) - 1
        return '\n'.join(''.join(
            gray_scale[self._image.getpixel((x, y)) * sc_len // 255] \
                for x in range(self._image.width)) for y in range(self._image.height))

if __name__ == '__main__':
    if len(argv) <= 1:
        print("usage: py image2ascii.py <file-path> [-p <percent>] [-w <file-path>] [--std | --expr]")
        exit()

    try:
        percent = float(argv[argv.index('-p') + 1])
    except:
        percent = 100

    try:   
        write = argv.index('-w')
    except:
        write = -1
        
    gray_scale = AsciiImage.EXPRESS_SCALE if '--expr' in argv else AsciiImage.STANDARD_SCALE
    im = AsciiImage(Image.open(argv[1]), percent / 100)
    res = im.convert(gray_scale)

    if write != -1:
        with open(argv[write + 1], 'w') as f:
            f.write(res)
    else:
        print(res)
    
