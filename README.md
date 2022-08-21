# python-tkinter-US-to-NT-
# Exchange rate change made by python Tkinter.(real time)
## __autor__ = "YOU XHUN-CHANG"
# 參考匯率為台灣銀行官網 https://rate.bot.com.tw/xrt?Lang=zh-TW
import sys
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import urllib.request as httplib  # 3.x
import json
import requests
from bs4 import BeautifulSoup


if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
    print("linux")  # linux
elif sys.platform == "darwin":  # MAC OS X
    from matplotlib.font_manager import FontProperties      # 中文字體
    wordColor = "black"
    font1 = ("Helvetica", 14)
    font2 = ("Helvetica", 20)
    font3 = ("Helvetica", 32)
elif sys.platform == "win32":
    # Windows (either 32-bit or 64-bit)
    font1 = ("Helvetica", 14)
    font2 = ("Helvetica", 20)
    font3 = ("Helvetica", 32)
req=requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")
phoneMediumFont = soup.select('.phone-medium-font')
tBody = soup.select('tbody')
name = soup.select('.hidden-phone')
rate = tBody[0].select('.rate-content-sight')
cashRate = tBody[0].select('.rate-content-cash')

win = tk.Tk()

label1Str1 = tk.StringVar()  # 建立StringVar 變數
label1Str1.set("")           # 將label1Str1先設為空值
# 下拉式選單選取時連結的函式--選取國家後左方將顯示該國家國旗
def fromFlag(event):
    labelFromFlag['text'] = nationalFlag[int(currencyList.index(fromComboboxCurrency.get()))]
def toFlag(event):
    labelToFlag['text'] = nationalFlag[int(currencyList.index(toComboboxCurrency.get()))]
# 按下按鈕所連結之
def transform():
    if fromComboboxCurrency.get() == toComboboxCurrency.get():
        result = entryTransform.get()
    elif fromComboboxCurrency.get() == "新台幣(TWD)":
        for i in range(0, len(name), 1):
            if toComboboxCurrency.get() == (name[i].text.split()[0] + name[i].text.split()[1]):
                try:
                    result = float(entryAmount.get()) / float(rate[i*2].text)
                except:
                    result = float(entryAmount.get()) / float(cashRate[i*2].text)
    else:
        if toComboboxCurrency.get() == "新台幣(TWD)":
            for i in range(0, len(name), 1):
                if fromComboboxCurrency.get() == (name[i].text.split()[0] + name[i].text.split()[1]):
                    try:
                        result = float(entryAmount.get()) * float(rate[i * 2].text)
                    except:
                        result = float(entryAmount.get()) * float(cashRate[i * 2].text)
        else:
            for i in range(0, len(name), 1):
                for j in range(0, len(name), 1):
                    if fromComboboxCurrency.get() == (name[i].text.split()[0] + name[i].text.split()[1]):
                        if toComboboxCurrency.get() == (name[j].text.split()[0] + name[j].text.split()[1]):
                            try:
                                a = float(rate[i * 2].text)
                            except:
                                a = float(cashRate[i * 2].text)
                            try:
                                b = float(rate[j * 2].text)
                            except:
                                b = float(cashRate[j * 2].text)
                            result = (float(entryAmount.get()) * a) / b
    labelResult['text'] = "%s%s = %.4f%s" % (entryAmount.get(), fromComboboxCurrency.get(), result, toComboboxCurrency.get())


win.wm_title("（台灣銀行）貨幣轉換器")
win.resizable(width=False, height=False)                  # 視窗設為長寬皆可調整
win.minsize(width=480, height=240)                      # 視窗最小設為480*480
win.maxsize(width=480, height=240)
# 輸入要轉換的金額
labelAmount = tk.Label(win, text="金額  ：", fg="#537791", bg="#ececec", font=font2)
labelAmount.place(x=20, y=20)
entryTransform = tk.StringVar()
# 輸入框
entryAmount = tk.Entry(win, textvariable=entryTransform)        # 新增輸入框Entry
entryAmount.place(x=90, y=20)
# label 從
fromLabelCurrency = tk.Label(win, text="從     ：", fg="#537791", bg="#ececec", font=font2)
fromLabelCurrency.place(x=20, y=60)
# 選擇幣別-下拉式選單
fromComboboxCurrency = tk.StringVar()
fromComboboxCurrency.set('美金(USD)')
fromCurrency = ttk.Combobox(win, width=20, font=font1, textvariable=fromComboboxCurrency)
# 將國旗以及爬蟲爬到的幣別放入下拉式選單
currencyList = []
nationalFlag = ["🇺🇸", "🇭🇰", "🇬🇧", "🇦🇺", "🇨🇦", "🇸🇬", "🇨🇭", "🇯🇵", "🇿🇦", "🇸🇪", "🇳🇿", "🇹🇭", "🇵🇭", "🇮🇩",
                "🇪🇺", "🇰🇷", "🇻🇳", "🇲🇾", "🇨🇳", "🇹🇼"]
labelFromFlag = tk.Label(win, text="🇺🇸", fg="#537791", bg="#ececec", font=font2)
labelFromFlag.place(x=45, y=60)
# 以迴圈放入
for i in range(0, len(name), 1):
    str1 = name[i].text.split()[0] + name[i].text.split()[1]
    currencyList.append(str1)
currencyList.append("新台幣(TWD)")
fromCurrency['values'] = currencyList
fromCurrency.place(x=90, y=60)
fromCurrency.bind('<<ComboboxSelected>>', fromFlag)
# label 到
toLabelCurrency = tk.Label(win, text="到     ：", fg="#537791", bg="#ececec", font=font2)
toLabelCurrency.place(x=20, y=100)
labelToFlag = tk.Label(win, text="🇹🇼", fg="#537791", bg="#ececec", font=font2)
labelToFlag.place(x=45, y=100)
# 選擇欲轉換之幣別-下拉式選單
toComboboxCurrency = tk.StringVar()
toComboboxCurrency.set('新台幣(TWD)')
toCurrency = ttk.Combobox(win, width=20, font=font1, textvariable=toComboboxCurrency)
toCurrency['values'] = currencyList
toCurrency.place(x=90, y=100)
toCurrency.bind('<<ComboboxSelected>>', toFlag)
# 轉換結果
labelResult = tk.Label(win, text="", fg="#537791", bg="#ececec", font=font2)
labelResult.place(x=20, y=140)



# 按鈕Button
btn1 = tk.Button(win, text="轉換", command=transform, fg="#537791", bg="#ececec", bd=0, font=font1)     # 建立Button物件 按下後會出叫event1函式
btn1.place(x=400, y=97)




win.mainloop()
