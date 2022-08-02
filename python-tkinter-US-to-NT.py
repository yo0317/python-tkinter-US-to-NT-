"""
no.1
美金轉台幣
"""
import sys
import tkinter as tk
from PIL import ImageTk, Image
import urllib.request as httplib  # 3.x
import json
if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
    print("linux")  # linux
elif sys.platform == "darwin":  # MAC OS X
    from matplotlib.font_manager import FontProperties      # 中文字體
    wordColor = "black"
    font1 = ("Helvetica", 16)
    font2 = ("Helvetica", 20)
    font3 = ("Helvetica", 64)
elif sys.platform == "win32":
    # Windows (either 32-bit or 64-bit)
    font1 = ("Helvetica", 16)
    font2 = ("Helvetica", 20)
    font3 = ("Helvetica", 64)

url = "https://quality.data.gov.tw/dq_download_json.php?nid=31897&md5_url=f8407732b6cd8a0ba132de7b7fd274a9"
req = httplib.Request(url, data=None,
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"})
reponse = httplib.urlopen(req)               # 開啟連線動作
if reponse.code==200:                        # 當連線正常時
    contents=reponse.read()                  # 讀取網頁內容
    contents=contents.decode("utf-8")        # 轉換編碼為 utf-8

obj1 = json.loads(contents)
win = tk.Tk()
x = Image.open("#c1c0b9.png")                   # 讀取圖片（背景）
img = ImageTk.PhotoImage(x)                     # 轉換成PhotoImage
labelBackground = tk.Label(win, image=img)      # 建立Label物件 顯示圖片（背景）
labelBackground.pack()                          # 置入圖片（背景）

label1Str1 = tk.StringVar()  # 建立StringVar 變數
label1Str1.set("")           # 將label1Str1先設為空值

# 美金轉台幣函式
def usToNT(n):
    number = float(n) * float(obj1[len(obj1)-1]['新台幣'])
    return number
# 按轉換鈕後觸發的函示
def event1():
    global label1Str1
    global entryUSToNT
    num = entryUSToNT.get()       # 取得entryUSToNT 上的文字

    ans = usToNT(num)
    label1 = tk.Label(win, text="轉換後台幣金額:", textvariable=label1Str1, fg="#537791", bg="#c1c0b9", font=font2)
    label1Str1.set("轉換後台幣金額:%30.2f元" % ans)
    label1.place(x=20, y=150)


win.wm_title("美金轉台幣")
win.resizable(width=False, height=False)                  # 視窗設為長寬皆可調整
win.minsize(width=480, height=480)                      # 視窗最小設為480*480
win.maxsize(width=480, height=480)
# 最上排顯示美金轉台幣的文字
labelUS = tk.Label(win, text="美金              →              臺幣", fg="#537791", bg="#c1c0b9", font=font2)
labelUS.place(x=120, y=40)
# 最上排放置台灣及美國國旗裝飾
y = Image.open("臺灣國旗.png")
imgTw = ImageTk.PhotoImage(y)
labelTw = tk.Label(win, image=imgTw, width=40, height=25)
labelTw.place(x=400, y=40)
z = Image.open("美國國旗.png")
imgUs = ImageTk.PhotoImage(z)

labelUs = tk.Label(win, image=imgUs, width=40, height=23)
labelUs.place(x=60, y=40)
labelUS1 = tk.Label(win, text="請輸入要轉換的金額：", fg="#537791", bg="#c1c0b9", font=font1)
labelUS1.place(x=20, y=100)
entryUSToNT = tk.StringVar()
entry1 = tk.Entry(win, textvariable=entryUSToNT)        # 新增輸入框Entry
entry1.place(x=190, y=97)
# 按鈕Button
btn1 = tk.Button(win, text="轉換", command=event1, fg="#c1c0b9", bg="#537791", bd=0, font=font1)     # 建立Button物件 按下後會出叫event1函式
btn1.place(x=400, y=97)




win.mainloop()