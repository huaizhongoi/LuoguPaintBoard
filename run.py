import requests
import time
import random
import json

with open("cookies.json",'r') as cookiesjson:
    cookies=json.load(cookiesjson)

with open("data/board.json",'r') as boardjson:
    board=json.load(boardjson)

last_time = []
for i in range(len(cookies)):
    last_time.append(0)

getheader={
    "refer":"https://www.luogu.com.cn/paintBoard",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

cur = -1
Timeout = 5
Left = 0
def paint(x,y,col):
    global cur
    cur=(cur+1)%len(cookies)
    
    while (time.time() - last_time[cur]) < 10.5 :
        time.sleep(0.5)
    
    data={
        'x':x,
        'y':y,
        'color':col
    }
    headers={
        "refer":"https://www.luogu.com.cn/paintBoard",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "cookie":cookies[cur]
    }
    try:
        response = requests.post("https://www.luogu.com.cn/paintBoard/paint",data=data,headers=headers)
        status = response.json()['status']
    except:
        status = -1
    
    global Left
    if status == 200:
        Left -= 1
        print('[200] Success by', cur, '! (', x, y, col,') |' , Left, 'need to do')
        last_time[cur] = time.time()
        return 0
    elif status == 401:
            print('[401] Not login.')
    elif status == 500:
            print('[500] Please wait for trying again.')
    else:
            print('[???] Unknown error.', '[', status, ']')
    return -1

while True:
    try:
        getboard=requests.get("https://www.luogu.com.cn/paintBoard/board",headers=getheader)
    except:
        continue
    todo = []
    for i in board:
        x=i[0]
        y=i[1]
        col=i[2]
        if x*401+y<len(getboard.text) and int(getboard.text[x*401+y],32)!=col:
            todo.append(i)
    Left = len(todo)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) , "[Info]:Have", Left , 'to do')
    if Left == 0:
        time.sleep(Timeout)
    for i in range(Left):
        bd = todo[i]
        x=bd[0]
        y=bd[1]
        col=bd[2]
        while True:
            if paint(x,y,col)==0:
                break