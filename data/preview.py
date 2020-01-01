from PIL import Image
import json
import sys
import requests

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

getheader={
    "refer":"https://www.luogu.com.cn/paintBoard",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
getboard=requests.get("https://www.luogu.com.cn/paintBoard/board",headers=getheader)

W = 800
H = 400

# ↓使用纯色画板（速度快）↓
def GetImage1():
    img = Image.new("RGB", (W, H), (170, 170, 170))
    return img

# ↓使用当前画板（速度慢）↓
def GetImage2():
    img = Image.new("RGB", (W, H))
    pimg = img.load()
    print('AllX:', W)
    for x in range(W):
        if x % 100 == 0:
            print('nowX:', x)
        for y in range(H):
            c = col[int(getboard.text[x*401+y],32)]
            pimg[x, y] = (c[0], c[1], c[2])
    return img

if len(sys.argv) >= 2 and sys.argv[1] == 'speed':
    img = GetImage1()
else:
    img = GetImage2()
pimg = img.load()
try:
    with open(DataPath,'r') as boardjson:
        board=json.load(boardjson)
except:
    board = []
for i in board:
    x = i[0]
    y = i[1]
    c = col[i[2]]
    pimg[x, y] = (c[0], c[1], c[2])

img.save("preview.bmp")
print('Finish.')