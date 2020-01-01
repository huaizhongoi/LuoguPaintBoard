from PIL import Image
import json
import sys

DataPath = 'board.json'
col=[
    [0, 0, 0],
    [255, 255, 255],
    [170, 170, 170],
    [85, 85, 85],
    [254, 211, 199],
    [255, 196, 206],
    [250, 172, 142],
    [255, 139, 131],
    [244, 67, 54],
    [233, 30, 99],
    [226, 102, 158],
    [156, 39, 176],
    [103, 58, 183],
    [63, 81, 181],
    [0, 70, 112],
    [5, 113, 151],
    [33, 150, 243],
    [0, 188, 212],
    [59, 229, 219],
    [151, 253, 220],
    [22, 115, 0],
    [55, 169, 60],
    [137, 230, 66],
    [215, 255, 7],
    [255, 246, 209],
    [248, 203, 140],
    [255, 235, 59],
    [255, 193, 7],
    [255, 152, 0],
    [255, 87, 34],
    [184, 63, 39],
    [121, 85, 72]
]
if len(sys.argv)<5:
    print("transform.py 'add'/'create' ImagePath LeftTopX LeftTopY")
    exit(0)
Type = sys.argv[1]
ImagePath = sys.argv[2]
X = int(sys.argv[3])
Y = int(sys.argv[4])
# print(Type, ImagePath, X, Y)
if Type != 'add' and Type != 'create':
    print("transform.py ImagePath add/create")
    exit(0)
if Type == 'add':
    Type = 0
else:
    Type = 1
oldimage = Image.open(ImagePath)

coldata = []
Length = len(col)
for i in range(Length):
    coldata.append(col[i][0])
    coldata.append(col[i][1])
    coldata.append(col[i][2])

# 转换为board.json
def toboard(im):
    size = im.size
    src = im.load()
    board = []
    for x in range(size[0]):
        for y in range(size[1]):
            board.append([x + X, y + Y, src[x,y]])
    board = json.dumps(board)
    with open(DataPath,'w+') as f:
        f.write(board)


# 抖动算法
def method1():
    palimage = Image.new('P', oldimage.size)
    palimage.putpalette(coldata * (int)(256/Length))
    newimage = oldimage.quantize(palette=palimage)
    toboard(newimage)

def quantizetopalette(silf, palette, dither=False):
    """Convert an RGB or L mode image to use a given P image's palette."""

    silf.load()

    # use palette from reference image
    palette.load()
    if palette.mode != "P":
        raise ValueError("bad mode for palette image")
    if silf.mode != "RGB" and silf.mode != "L":
        raise ValueError(
            "only RGB or L mode images can be quantized to a palette"
            )
    im = silf.im.convert("P", 1 if dither else 0, palette.im)
    # the 0 above means turn OFF dithering

    # Later versions of Pillow (4.x) rename _makeself to _new
    try:
        return silf._new(im)
    except AttributeError:
        return silf._makeself(im)

# 非抖动算法
def method2():
    palimage = Image.new('P', oldimage.size)
    palimage.putpalette(coldata * (int)(256/Length))
    newimage = quantizetopalette(oldimage, palimage, dither=False)
    toboard(newimage)

method1()

# ↓效果较差，勿用↓
# method2()