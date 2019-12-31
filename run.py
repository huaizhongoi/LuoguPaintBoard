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
def paint(x,y,col):
    global cur
    cur=(cur+1)%len(cookies)
    
    while (time.time() - last_time[cur]) < 10 :
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
    response = requests.post("https://www.luogu.com.cn/paintBoard/paint",data=data,headers=headers)
    status = response.json()['status']
    if status == 200:
            print('[200] Success by', cur, '! (', x , y , col , ')')
            last_time[cur] = time.time()
            return 0
    elif status == 401:
            print('[401] Not login.')
    elif status == 500:
            print('[500] Please wait for trying again.')
    else:
            print('[???] Unknown error.')
    return -1

while True:
    getboard=requests.get("https://www.luogu.com.cn/paintBoard/board",headers=getheader)
    todo = []
    for i in board:
        x=i[0] + 30
        y=i[1]
        col=i[2]
        if x*401+y<len(getboard.text) and int(getboard.text[x*401+y],32)!=col:
            todo.append(i)
    cnt = len(todo)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) , "[Info]:Have", cnt , 'to do')
    if cnt == 0:
        time.sleep(Timeout)
    for i in range(cnt):
        bd = todo
        x=bd[0] + 30
        y=bd[1]
        col=bd[2]
        while True:
            # if cur==0:
            #     getboard=requests.get("https://www.luogu.com.cn/paintBoard/board",headers=getheader)
            if paint(x,y,col)==0:
                break