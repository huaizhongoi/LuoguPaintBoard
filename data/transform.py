from PIL import Image
import json
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

coldata = []
Length = len(col)
for i in range(Length):
    coldata.append(col[i][0])
    coldata.append(col[i][1])
    coldata.append(col[i][2])

im = Image.open('ll.bmp')

'''
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

# palettedata = [0, 0, 0, 102, 102, 102, 176, 176, 176, 255, 255, 255]
palimage = Image.new('P', im.size)
palimage.putpalette(coldata * (int)(256/Length))
# oldimage = Image.open("School_scrollable1.png")
newimage = quantizetopalette(im, palimage, dither=False)
# newimage.show()
'''
palimage = Image.new('P', im.size)
palimage.putpalette(coldata * (int)(256/Length))
newimage = im.quantize(palette=palimage)

# expanded_coldata = coldata * (int)(256/Length)
# newimage = im.convert('P', dither=Image.NONE, palette=expanded_coldata)

# newimage = Image.new('P', im.size)
# newimage.putpalette(coldata * (int)(256/Length))
# newimage.paste(im, (0, 0) + im.size)
# im.putpalette( tmp * 64)
newimage.save('3.bmp')