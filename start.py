####2022-11-12 start
#1.註解
print(" Hello python2")

#2.資料型態
#字
#字串
#布林值
#有順序, 可動的列表 list
[3,4,5]
#有順序,不可動的列表 Tuple
(3,4,5)
#變數 : 用來儲存資料的自訂名稱
#集合,無順序的概念 set
{3,4,5}
#字典 dictionary
{"apple":"蘋果","data":"資料"}
#變數名稱=資料
data=3
#print(資料)
print(data)
data=True #取代舊的資料
print(data)
data={3,4,5}
print(data)

#3.數字、字串基本運算
#字串運算
s="Hell\"o" #跳脫
print(s)

s="Hello"+"world" #字串串接
print(s)

s="Hello\nworld" #換行
print(s)

s="""Hello
world""" #連續三個雙引號是換行
print(s)

s="Hello"*3+"World" #字串* 重複3次 +字串
print(s)
#字串會對內部的字元編號(索引),從0開始算起
s="Hello"
print(s[1:4])
print(s[1:])
print(s[:4])

#####2022-11-13
#4.有序列表的運算
#有序可變動列表 list
grades=[12,60,15,70,90]
print(grades[0]) #取得特定列表中的資料
print(grades[1:4]) #輸出60 15 70 1:4表示1~3不包含4

#修改列表中的資料
grades[0]=55 #把55放到列表中第一個位置
print(grades)

#刪除列表中的元素
grades[1:4]=[] #連續刪除列表中從編號1到編號4(不包括) 的資料
print(grades)

#列表串接
grades=[12,60,15,70,90]
grades=grades+[12,33]
print(grades)

#len() 取得列表長度
grades=[12,60,15,70,90]
length=len(grades)
print(length)

#巢狀列表
data=[[3,4,5],[6,7,8]]
print(data[0]) #[3,4,5]
print(data[0][0]) #[3]
print(data[0][0:2]) #[3,4]

data[0][0:2]=[5,5,5] #把 3,4換成 5,5,5
print(data)

#有序不可變動列表 Tuple
data=(3,4,5)
data[0]=5 # 注意:錯誤, tuple的資料不可以變動
print(data)

#5.集合、字典的基本運算
#判斷資料是否存在 , 使用 in 和 not in運算符號
#差集、反交集 ,使用- 和 ^ 運算符號
#字串拆解為集合 set(字串)

#字典
#基本概念 :鍵值對 (key - value pair)  
#字典[key]
#字典[key]=value
#判斷資料是否存在 , 使用 in 和 not in運算符號
#刪除鍵值對 ,使用del 運算關鍵字
#從列表建立字典 , 以列表的資料為基礎來建立字典

#集合的運算
s1={3,4,5}
print(3 in s1) # OUTPUT: True
print(10 in s1) # OUTPUT: False
print(10 not in s1) # OUTPUT: True

s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 #交集
print(s3)
s3=s1|s2 #聯集
print(s3)
s3=s1-s2 #差集
print(s3)
s3=s1^s2 #反交集
print(s3)
s=set("hello") #字串拆解為集合 : set(字串)
print(s)
print("h" in s) #T
print("a" in s) #F

#字典的運算 : key-value 配對
dic = {"apple":"蘋果","bug":"蟲蟲"}
print(dic["apple"]) #蘋果
dic["apple"]="小蘋果" #改值
print(dic["apple"])

dic = {"apple":"蘋果","bug":"蟲蟲"}
print("apple" in dic) #判對 key 是否存在
print("test" not in dic)

dic = {"apple":"蘋果","bug":"蟲蟲"}
print(dic)
del dic["apple"] #刪除字典的鍵值對
print(dic)

#從列表建立字典 , 以列表的資料為基礎來建立字典
dic={x:x*2 for x in [3,4,5]}
print(dic) #{3: 6, 4: 8, 5: 10}

#6.流程控制 : 判斷式
#if 判斷式
 
#基本語法一
#if 布林值: 
#   若布林值為 true .執行命令 (注意縮排 Tab)

#固定語法
# if ... :


#基本語法二
#if 布林值: 
#   若布林值為 true .執行命令 (注意縮排 Tab)
#else:
#   若布林值為 false, 執行命令

#固定語法
# if ... :
# else:

#基本語法三
#if 布林值一: 
#   若布林值一為 true .執行命令 (注意縮排 Tab)
#elif 布林值二:
#   若布林值二為 true .執行命令 (注意縮排 Tab)
#else:
#   若布林值一和二都 false, 執行命令(注意縮排 Tab)

#固定語法
# if ... :
# elif ... :
# else :

#判斷式
x = input("請輸入數字: ") #input() 取得字串形式的使用者輸入
x = int(x) #將字串型態轉換成數字型態 
if x>200:
    print("大於 200")
elif x>100:
    print("大於 100")
else:
    print("小於等於 100")

#四則運算
n1 = int (input("請輸入數字一: "))
n2 = int (input("請輸入數字二: "))
op = input("請輸入運算: +, -, *, / : ")
if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "/":
    print(n1/n2)
else:
    print("不支援")

#7.流程控制 : 迴圈基礎
#while 迴圈
#基本語法
# while 布林值:
#   若布林值為 True, 執行命令

n = 1
while n<=3:
    print(n)
    n+=1

#1+2+3+...+10
n = 1
sum = 0 #紀錄累加的結果
while n <= 10:
    sum = sum+n
    n += 1
print(sum)

 
#for 迴圈
# for 變數名稱 in 列表或字串:
#   將列表中的項目或字串中的字元逐一取出, 逐一處理
#使用 range()
# for 變數名稱 in range(3): 等同於 for 變數名稱 in [0,1,2]: 
# for 變數名稱 in range(3:6): 等同於 for 變數名稱 in [3,4,5]:

for x in [3,5,1]:
    print(x) #output : 3,5,1

for x in "hello":
    print(x) #output : h,e,l,l,o

for x in range(5):
    print(x) #output : 0,1,2,3,4 (注意不包括5)

for x in range(5,10):
    print(x) #output : 5,6,7,8,9

#1+2+3+...+10
sum = 0
for x in range(1,11):
    sum = sum+x
print(sum) #55

#8. 流程控制 : 迴圈進階控制
# break and continue

#強制結束迴圈
# while 布林值:
#   break
# for 變數名稱 in 列表或字串:
#   break

# break 簡易範例
n=0
while n<5:
    if n==3:
        break
    print(n)
    n+=1
print("最後的 n: ", n) #output : 最後的 n: 3

#強制繼續下一圈
# while 布林值:
#   continue
# for 變數名稱 in 列表或字串:
#   continue

# continue 簡易範例
n = 0
for x in [0,1,2,3]:
    if x%2==0: # x 是偶數
        continue # 繼續執行
    print(n) #1,3
    n+=1
print("最後的 n:",n) #output : 最後的 n: 2
# x=0 > continue
# x=1 > 印1 > n=1
# x=2 > comtinue
# x=3 > 印3 > n=2

#else
#基本語法
# while 布林值:
#   若布林值為 True, 執行命令
#   回到上方, 坐下一次的迴圈判斷
# else:
#   迴圈結束前,執行此區塊的命令

#else 簡易範例
n = 1 
while n<5:
    print("變數n的資料是: " ,n)
    n+=1
else:
    print(n) #迴圈結束前, 印出5



# for 變數名稱 in 列表或字串:
#   將列表中的項目或字串中的字元逐一取出, 逐一處理
# else:
#   迴圈結束前,執行此區塊的命令

#else 簡易範例
sum = 0
for n in range(11): #0~10
    sum+=n
else:
    print(sum) #印出 0+1+..._10 的結果


for c in "hello":
    print("逐一取出字串中的字元" ,c)
else:
    print(c) #迴圈結束前, 印出o

#綜合範例: 找出整數平方根
n = int(input("輸入一個正整數: "))
for i in range(n): #從i 到 n-1
    if i*i==n:
        print("整數平方根: " ,i)
        break #注意: 用break強制結束, 不會執行else區塊
else:
    print("沒有整數平方根")

#####2022-11-19
# 9. 函式基礎 
# 程式區塊 : 程式碼包裝在一個區塊中, 方便隨時呼叫使用
# 定義 > 呼叫
# 要先定義(建立)函式 , 然後才能呼叫(使用) 函式
# 基本語法
# def 函式名稱(參數名稱):
    #函式內部的程式碼
#固定語法
# def ():

#定義一個印出hello的函式
def sayhello():
    print("hello")
#定義可以印出任何訊息的函式
def say(msg):
    print(msg)
#定義一個可以做加法的函式
def add(n1, n2):
    result=n1+n2
    print(result)

#呼叫函式
#基本語法
# 函式名稱(參數資料)

#定義一個印出hello的函式
def sayhello():
    print("hello")
#呼叫上方定義的函式
sayhello()

#定義可以印出任何訊息的函式
def say(msg):
    print(msg)
#呼叫上方定義的函式
say("hello fuction")
say("hello python")

#定義一個可以做加法的函式
def add(n1, n2):
    result=n1+n2
    print(result)
#呼叫上方定義的函式
add(3,4)
add(7,8)

#回傳值
#基本語法
# def 函式名稱(參數名稱):
    #函式內部的程式碼
    #return #結束函式, 回傳 None
# def 函式名稱(參數名稱):
    #函式內部的程式碼
    #return 資料 #結束函式, 回傳「資料」
def say(msg):
    print(msg)
    return
value=say("hello fuction")
print(value) #None

def add(n1, n2):
    result=n1+n2
    return "hello"
value=add(3,4)
print(value) #hello

def add(n1, n2):
    result=n1+n2
    return result
value=add(3,4)
print(value) #印出 7

#函式內部的程式碼, 沒有呼叫. 就不會執行
def multiply():
    print(3*4)
#呼叫上方定義的函式
multiply()

#實例.
def multiply(n1,n2):
    print(n1*n2)
multiply(3,4)
multiply(10,8)

def multiply(n1,n2):
    print(n1*n2)
    return #none
value=multiply(3,4) 
print(value)
#output: 12, none
#step1 呼叫multiply() print12
#step2 return #none ,value=none > print none

def multiply(n1,n2):
    print(n1*n2)
    return n1*n2
value=multiply(3,4) 
print(value)
#output: 12, 12

#return比直接在函數裡面print結果有彈性
def multiply(n1,n2):
    return n1*n2
value=multiply(3,4)+multiply(10,5)
print(value)

#程式的包裝
def calculate(max):
    sum=0
    for n in range(1,max):
        sum=sum+n
    print(sum)

calculate(10)
calculate(20)

#####2022-12-02
# 10. 函式參數詳解
# 基本語法
# def函式名稱(參數名稱=預設資料):
    函式內部的程式碼

#參數msg預設資料為"hello"
def say(msg='hello'):
    print(msg)
#印出 hello fuction
say('hello fuction')
#印出預設資料 hello
say()

# 名稱對應
# 基本語法
# def函式名稱(名稱1, 名稱2):
    函式內部的程式碼
#呼叫函式, 以參數名稱對應資料
函式名稱(名稱2=3, 名稱1=5)

#範例
def divide(n1,n2):
    result=n1/n2
    print(result)

divide(2,4) #印出0.5
divide(n2=2, n1=4) #印出2.0

# 無限參數
# 基本語法
# def 函式名稱(*無限參數):
#     無限參數以tuple資料形態處理
#     函式內部的程式碼
#呼叫函式, 可傳入無線數量的參數
# 函式名稱(資料一. 資料二, 資料三)

#函式接受無限參數 msgs
def say(*msgs):
    #以tuple的方式處理
    for msg in msgs:
    print(msg)
#呼叫函式, 傳入三個參數資料
say('hello','arbitraty','arguments')

#參數的預設資料
def power(base,exp=0):
    print(base**exp)
power(3,2) #9
power(4) #exp沒給, 預設exp=0. 印出1

#使用參數名稱對應
def divide(n1,n2):
    print(n1/n2)
divide(2,4) #印出0.5
divide(n2=2,n1=4) #印出2

#無限參數資料
def avg(*ns): #ns 是 tuple的資料型態
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))

avg(3,4) #3.5
avg(3,5,10) #6.0
avg(1,4,-1,-8) #-1.0

#####2022-12-04
# 11. 模組載入與使用
# 模組
# 獨立的程式檔案
# 將程式寫在一個檔案中, 此檔案可重複載入使用
# 載入> 使用
# 先載入模組, 再使用模組中的函式或變數

#載入模組
#基本語法
#import 模組名稱 as 模組別名

#使用模組
# 基本語法
# 模組名稱或別名.函式名稱(參數資料)
# 模組名稱或別名.變數名稱

#內建模組
# sys模組

#載入sys模組
import sys
#使用sys模組
print(sys.platform) #印出作業系統
print(sys.maxsize) #印出整數型態的最大值
print(sys.path) #印出搜尋模組的路徑

#載入sys模組- 利用別名
import sys as s
#使用sys模組
print(s.platform) #印出作業系統
print(s.maxsize) #印出整數型態的最大值
print(s.path) #印出搜尋模組的路徑

#自訂模組
# 建立幾何運算模組
# 建立檔案 geometry.py ,定義平面幾何運算用的函式

#載入與使用
#載入geometry模組, 並使用模組中的定義的功能
import geometry
result=geometry.distance(1,1,5,5)
print(result)
result=geometry.slope(1,2,5,6)
print(result)

#調整搜尋模組的路徑
import sys
sys.path.append("modules") #python 多加一個模組搜尋路徑
print(sys.path) #印出搜尋模組的路徑
print("--------------------------------------------------")
import geometry
print(geometry.distance(1,1,5,5))

#####2022-12-04
# 12. 封包
# 包含模組的資料夾
# 用來整理, 分類模組程式

#建立封包
# 專案檔案配置

# -專案資料夾
#   -主程式.py
#   -封包資料夾
#       - __init__.py
#       - 模組一.py
#       - 模組二.py

#基本語法
#import 封包名稱.模組名稱 as 模組別名


#主程式
import modules.geometry
result=modules.geometry.distance(3,4)
print(result)

import modules.geometry
result=modules.geometry.slope(1,5,3,5)
print("斜率", result)

import modules.geometry as line
result=line.slope(1,5,3,5)
print("斜率", result)

#####2022-12-04
# 13.讀檔
# 檔案操作流程
# 開啟檔案> 讀檔或寫入> 關閉檔案

#基本語法
# 檔案物件=open(檔案路徑, mode=開啟模式)
# 開啟模式 : 讀取模式(-r), 寫入模式(-w), 讀寫模式(-r+)

##讀取檔案
# 讀取全部文字
# 檔案物件.read()

#一次讀取一行
# for 變數 in 檔案物件:
#   從檔案依序讀取每行文字到變數中

#讀取JSON 格式
# import json
#   讀取到的資料=json.load(檔案物件)

##寫入檔案
# 寫入文字
# 檔案物件.write(字串)

#寫入換行符號
# 檔案物件.write("這是範例文字\n")

#寫入 json 格式
# import json
# json.dump(要寫入的資料, 檔案物件)

##關閉檔案
# 檔案物件.close()

#最佳實務- 只要記住這個就好 !!!!
# with open(檔案路徑, mode=開啟模式) as 檔案物件:
#   讀取或寫入檔案的格式
#不用close, 以上區塊會自動, 安全的關閉檔案

#儲存檔案
file=open('data.text',mode='w') #開啟並寫入
file.write('hello file\nsecond line') #寫入
file.close() #關閉

file=open('data.text',mode='w',encoding='utf-8') #開啟並寫入
file.write('中文測試\n成功') #寫入
file.close() #關閉

with open('data.text',mode='w',encoding='utf-8') as file:
    file.write('中文測試\n成功123')

#讀檔, 一行一行讀取, 並計算總合
with open('data.text',mode='w',encoding='utf-8') as file:
    file.write('5\n3')

sum=0
with open('data.text',mode='r',encoding='utf-8') as file:
    for line in file:
        sum+=int(line)
print(sum)

#讀取JSON 格式
import json
with open("config.json",mode='r') as file:
    data=json.load(file) 
print(data) #data資料型態 : 字典
print("name: ", data["name"])
print("version: ", data["version"])

#修改變數中的資料, 並寫入JSON
data["name"]="New Name" 
with open("config.json",mode='w') as file:
    json.dump(data, file)
print(data) #data資料型態 : 字典

#####2022-12-10
# 14.亂數與統計模組
import random
#從列表中隨機選取1個資料
random.choice([0,1,5,8])
#從列表中隨機選取2個資料
random.choice([0,1,5,8],2 )

#隨機調換順序
import random
#將列表的資料 「就地」 隨機調換順序
data=[0,1,5,7]
random.shuffle(data)
print(data)

#隨機亂數
import random
#取得0.0~1.0之間的隨機亂數
random.random()
random.uniform(0.0, 1.0) #同上

#常態分配亂數
import random
#取得平均數100、標準差10的 常態分配亂數
random.normalvariate(100,10)

#統計模組
import statistics
#計算平均數
statistics.mean([1,4,6,9])
#計算中位數
statistics.medain([1,4,6,9])
#計算標準差
statistics.stdev([1,4,6,9])

###實作
import random
data=random.choice([1,5,6,10,20]) #隨機選取
print(data)

data=random.sample([1,5,6,10,20],3) #隨機選取3筆
print(data)

data=[1,5,8,20]
random.shuffle(data) #洗牌概念
print(data)

data=random.random() #0~1之間隨機亂數
print(data)

data=random.uniform(60,100) #60~100之間隨機亂數
print(data)

data=random.normalvariate(100,10)
print(data)

import statistics as st
data=st.mean([1,4,6,9])
print(data)

data=st.median([1,4,6,9])
print(data)

data=st.stdev([1,4,6,9])
print(data)

#####2022-12-10
# 15.網路連線程式, 公開資料串接
import urllib.request as re
with re.urlopen(網址) response:
    data=response.read()
print(data)

#確認資料格式 json,csv,其他...
#讀取json格式, 直接載入模組

##實作
import urllib.request as re
src="https://www.eslite.com/"
with re.urlopen(src) as response:
    data=response.read().decode('utf-8')
print(data) #取得誠品線上原始碼

import urllib.request as re
import json as js
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with re.urlopen(src) as response:
    data=js.load(response)
#取出公司名稱列表
clist=data["result"]["results"]
with open("data.txt",'w',encoding='utf-8') as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n") #資料型態: 字典


#####2022-12-10
# 16.類別定義與使用
# 封裝變數或函式
# 封裝變數或函式, 統稱 類別的屬性
# 定義>使用 : 先定義類別, 才能使用類別中封裝的屬性

#定義類別
class 類別名稱:
    定義封裝的變數
    定義封裝的函式

#使用
類別名稱.屬性名稱

##實作
#定義一個類別io, 有兩個屬性supportedsrcs 和read
class io:
    supportedsrcs=["console","file"]
    def read(src):
        if src not in io.supportedsrcs:
            print("not supportedsrcs")
        else:
            print("read from", src)

#使用
print(io.supportedsrcs)
io.read("file")
io.read("internet")

#####2022-12-10
# 17.實體物件建立與使用(上)
#類別的兩種用法
#1.類別與類別屬性. 2.類別與實體物件、實體屬性.
#建立
#透過類別建立 : 先建立類別, 再透過類別建立實體物件
#建立 >使用
#要先建立實體物件, 然後才能使用實體屬性

#建立實體
#基本語法
class 類別名稱:
    #定義初始化函式
    def __init__(self): #_init_(self)是固定語法
        透過操作self來定義實體屬性
#建立實體物件.放入變數obj中
obj=類別名稱() #呼叫初始化函式

#使用實體
實體物件.實體屬性名稱

#實作
#point 實體物件的設計, 平面座標上的點
class point: #建立類別
    def __init__(self): #實體物件
        self.x=3 #x,y實體屬性
        self.y=4
#建立第一個實體物件
p1=point()
print(p1.x, p1.y) #抓3,4
#建立第二個實體物件
p2=point()
print(p2.x, p2.y) #抓3,4

##彈性用法
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
#建立第一個實體物件
p1=point(3,4)
print(p1.x, p1.y) #抓3,4
#建立第二個實體物件
p2=point(5,6)
print(p2.x, p2.y) #抓5,6

#fullname 實體物件的設計, 分開紀錄姓, 名資料的全名
class fullname:
    def __init__(self, first, last):
        self.first=first
        self.last=last
name1=fullname('Lin','ChaiChing')
print(name1.first,name1.last)

#####2022-12-17
# 18.實體物件建立與使用(下)
# 實體屬性 > 封裝在實體物件中的變數

#基本語法
class 類別名稱:
    #定義初始化函式
    def __init__(self): #_init_(self)是固定語法
        定義實體屬性
    定義實體方法/函式
#建立實體物件.放入變數obj中
obj=類別名稱() #呼叫初始化函式

#詳細版   定義實體方法/函式
class 類別名稱:
    #定義初始化函式
    def __init__(self): #_init_(self)是固定語法
        封裝在實體物件中的變數
    def 方法名稱(self, 更多自訂參數):
        方法主體, 透過self操作實體物件
#建立實體物件.放入變數obj中
obj=類別名稱() #呼叫初始化函式

#使用方法
實體物件.實體方法名稱(參數資料)

#實作
#point 實體物件的設計, 平面座標上的點
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self): #定義實體方法
        print(self.x,self.y)
    def distance(self, targetX, targetY):
        return ((self.x-targetX)**2+(self.y-targetY)**2)**0.5
p=point(3,4) #建立實體物件
p.show() #呼叫實體方法 > 印出 3,4
result=p.distance(0,0) #計算(3,4)到原點座標 的距離
print(result)

#file 實體物件的設計, 包裝檔案讀取的程式
class file:
    def __init__(self, name):
        self.name=name
        self.file=None #尚未開啟檔案, 初期是 None
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
#讀取第一個檔案
f1=file("data.txt")
f1.open()
data=f1.read()
print(data)
#讀取第二個檔案
f2=file("data.text")
f2.open()
data=f2.read()
print(data)

#####2022-12-17
# 19.網路爬蟲 web crawler 基本篇
# 基本流程
# 1.連線到特定網址, 抓取資料
# 2.解析資料, 取得實際想要的部分

# step1. 抓取資料
# 關鍵 !!
# 盡可能地, 讓程式模仿一個普通使用者的樣子

# step2. 解析資料
# 格式 json , 使用內建json模組即可
# 大部分都是html格式資料, 使用第三方套件 beautifulsoup 來做解析

<html>
    <head>
        <title>Document</title>
    </head>
    <body>
        <div class="list">
            <span>階層結構</span>
            <span>樹狀結構</span>
        </div> 
    </body>
</html>

#安裝 beautifulsoup
pip install beautifulsoup4

import urllib.request as req
url="https://www.pttweb.cc/hot/all/today"
#建立一個request物件, 附加request headers的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)

#解析原始碼, 取得標題
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
#print(root.title)
title1=root.find_all("span",class_="e7-show-if-device-is-not-xs")
title2=root.find("span",class_="__e7-full-title-appended-part")
for title in title1:
    print(title.span.string)
for title in title2:
    print(title.string)

#####2022-12-17
# 20.網路爬蟲 web crawler -cookie
#什麼是cookie ?
#網站存放在瀏覽器的一小段內容
#與伺服器的互動
#連線時,放在request headers中送出
#追蹤連結
# <body>
#     <a href="https://www,google.com/">Google</a>
# </body>
#連續抓取頁面實務
#解析頁面的超連結, 並結合程式邏輯完成

import urllib.request as req
url="https://www.ptt.cc/bbs/Gossiping/index.html"
#建立一個request物件, 附加request headers的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)

import urllib.request as req
def getdata(url):
    #建立一個request物件, 附加request headers的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #print(data)

    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    #print(root.title)
    title1=root.find_all("div",class_="title")
    for title in title1:
        print(title.a.string)
    #抓取上一頁的連結
    nextlink=root.find("a",string='‹ 上頁') #找到內文是 <上頁的 a標籤
    return nextlink["href"]
url="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<5:
    url="https://www.ptt.cc"+getdata(url)
    count+=1

#####2022-12-17
# 21.網路爬蟲 web crawler -AJAX
#什麼是 AJAX ?
#網頁前端的JavaScript程式技術
#關鍵問題
#認出網站運作, 找出真正能抓到資料的網址


#找不到 MEDIUM的HOME-FEED 所以無法做練習...................
#先跳過

#####2022-12-18
# 22.網路爬蟲 web crawler -request data
# 請求附帶的資料, 叫做request data
# 關鍵問題
# 認出網站的AJAX模式,並懂得發出複雜的請求

# 找不到標題原始碼, 所以先跳過...

#####2022-12-19
# 23.網站開發 Flask

#1.安裝flask套件
#2.建立專案資料夾, 寫程式(後端)
#3.啟動伺服器, 測試網站運作
# 看app.py

#####2022-12-19
# 24.網站開發 Flask - heroku雲端主機
# 上線!

#1.建立flask專案描述檔
#2.安裝git工具
#3.到heroku註冊帳號, 建立應用
#4.安裝heroku命令列工具
#5.將程式部屬到 heroku app,並測試

#heroku 開始收費了...

#####2022-12-24
# 25.資料分析 -　基礎篇

#Series 單維度
#Dataframe 雙維度

import pandas as pd 
data=pd.Series([20,10,15])
print(data)

print("max : ", data.max())
print("median : ", data.median())
data=data*2
print(data)

data=data==20 # == 比較
print(data)
# 0    False
# 1     True
# 2    False

data=pd.DataFrame({
    "name":["amy","john","bob"],
    "salary":[30000,50000,40000]
})

print(data["name"]) #取欄位
print(data.iloc[0]) #取列

#####2022-12-24  
# 26.資料分析 -　Series

#Series 單維度
#Dataframe 雙維度

import pandas as pd 
data=pd.Series([5,4,-2,3,7], index=["a","b","c","d","e"]) #index, 建立資料索引
print(data)

print("資料型態", data.dtype)
print("資料數量", data.size)
print("資料索引", data.index) #object 字串
print(data[2], data[0])
print(data["e"],data["d"])

print(data.sum(), data.max(), data.prod())
print(data.mean(), data.median(), data.std())
print("最大三個數", data.nlargest(3), "最小三個數", data.nsmallest(2))

data=pd.Series(["您好","Python","Pandas"])
print(data.str.len) #算出字串長度
print(data.str.lower) #全部變小寫
print(data.str.cat,sep="-") #字串串接符號
print(data.str.contains("p")) #字串包含p嗎 ?
print(data.str.replace("您好","hello"))

#####2022-12-24
# 27.資料分析 -　DataFrame

#Series 單維度
#Dataframe 雙維度

import pandas as pd 
data=pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[30000,40000,50000]
}, index=["a","b","c"])

print(data)
print("資料數量", data.size)
print("資料形狀 (列x欄)", data.shape)

print("取第二列", data.iloc[1], sep='\n')
print("取得第c列", data.loc["c"], sep='\n')

print("取得 name欄位", data["name"], sep='\n')
names=data["name"] #取得series
print("把names 全部轉大寫", names.str.upper, sep='\n')

print(data["salary"].mean())

#建立新欄位
data["revenue"]=[50000,40000,30000] #data[新欄位]=列表
data["rank"]=pd.Series([3,6,1], index=["a","b","c"]) #data[新欄位]=Series 資料
data["cp"]=data["revenue"]/data["salary"]
print(data)

#####2022-12-24
# 28.資料分析 -　篩選資料

#Series 單維度
import pandas as pd 
data=pd.Series([30,15,20])
condition=data>18
filterData=data[condition]
print(filterData)

data=pd.Series(["您好","Python","Pandas"])
condition=data.str.contains("P")
print(condition)
dilterData=data[condition]
print(dilterData)


#Dataframe 雙維度
data=pd.DataFrame({
    "name":["amy","john","bob"],
    "salary":[30000,50000,40000]
})
condition= data["salary"]>=40000 #dataframe 都是篩選資料列
condition= data["name"]=="amy" #dataframe 都是篩選資料列
filterData=data[condition]
print(filterData)
