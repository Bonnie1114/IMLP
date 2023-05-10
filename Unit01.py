#!/usr/bin/env python
# coding: utf-8

# # Python programming 
# ## Crash Course on Python Coding Practice
# 
# No matter the level of mastery you hope to get to in Python,<br> 
# you'll need these fundamentals in place before you jump into any project.<br><br>
# 
# You need to know how to:
# 
# - declare variables
# - collect user input
# - store information
# - repeat an action through loops
# - write functions to repeat blocks of code
# 

# ### 01 - 奇偶數辨別（Odd or even）
# #### 當使用者輸入一個的數字，它能夠辨別奇偶，並輸出檢驗結果給使用者。
# 
# > 題目：輸入一數字判斷奇數或偶數<br>
# 輸入(Input): 一個數字 <br>
# 輸出(Output):奇數或偶數
# 
# * 進階: 可以限制輸入一個介於一定範圍（例如 1 到 1000）的數字

# In[7]:


num = input()
num = int(num)
print(type(num))

if num % 2 == 0: 
    print("你的數字為偶數")
else: 
    print("你的數字為奇數")

if num >= 1 and num <= 100 :
    print("在範圍值裡")
else:
    print("超出範圍")


# ### 02 - 填字遊戲（Mad libs game）
# #### 使用者輸入任何字，它可以是名詞、形容詞、動詞、代名詞等。程式得到文字後，可自行排列，組成成一個模板故事。
# 
# > 題目：輸入一數字判斷奇數或偶數<br>
# 輸入(Input): 一連串依據說明輸入對應文字 <br>
# 輸出(Output): 模板故事
# 
# * 進階: 可以讓程式重複執行

# In[28]:


name = input("請輸入你的寵物名稱:")
number = input("請輸入你飼養的寵物數量:")
type_of_pets = input("請輸入你養什麼寵物:")
gender = input("請輸入寵物性別:")

print("--------")
print("姓名: ", name)
print("寵物數量: ", number)
print("寵物品種: ", type_of_pets)
print("性別: ", gender)
print("--------")


# ### 03 -  猜數字（Guess the number）
# #### 請使用者猜一個介於範圍（例如 1 到 100）之間的數字，
# #### 若使用者猜錯，就詢問他們想繼續玩還是退出；若使用者猜對，就顯示祝賀訊息，
# #### 並統計使用者的嘗試次數。如果使用者輸入的數字超出設定範圍，就顯示錯誤提示。
# 
# ![](data\guess.png)
# 

# In[32]:





# ### 04 - 計算字數（Word count）
# #### 使用者輸入一段文字或讀取一檔案，程式統計字數。
# 
# > 輸入(Input):我要成為寫程式的專家 <br>
# 輸出(Output):你用了 10 個文字述說內心的想法
# 
# #### 在特定的文章字串中搜尋輸入的特定字，請使用者輸入欲搜尋的文字，印出總共有幾個。<br>
# >輸入(Input):天<br>
# 輸出(Output): 9
# 
# * 進階:計算文章中去除標點符號後的字數，找出文章中出現最多的字與次數

# In[40]:


word = input()
print("你用了 %d 個文字述說內心的想法"%(len(word)))


s = '''漢皇重色思傾國，御宇多年求不得。

楊家有女初長成，養在深閏人未識。

天生麗質難自棄，一朝選在君王側。

回眸一笑百媚生，六宮粉黛無顏色。

春寒賜浴華清池，溫泉水滑洗凝脂；

侍兒扶起嬌無力，始是新承恩澤時。

雲鬢花顏金步搖，芙蓉帳暖度春宵；

春宵苦短日高起，從此君王不早朝。

承歡侍宴無閑暇，春從春遊夜專夜。

後宮佳麗三千人，三千寵愛在一身。

金屋妝成嬌侍夜，玉樓宴罷醉和春。

姊妹弟兄皆列士，可憐光彩生門戶。

遂令天下父母心，不重生男重生女。

驪宮高處入青雲，仙樂風飄處處聞。

緩歌慢舞凝絲竹，盡日君王看不足。

漁陽鼙鼓動地來，驚破霓裳羽衣曲。

九重城闕煙塵生，千乘萬騎西南行。

翠華搖搖行復止，西出都門百餘里；

六軍不發無奈何？宛轉蛾眉馬前死。

花鈿委地無人收，翠翹金雀玉搔頭。

君王掩面救不得，回看血淚相和流。

黃埃散漫風蕭索，雲棧縈紆登劍閣。

峨嵋山下少人行，旌旗無光日色薄。

蜀江水碧蜀山青，聖主朝朝暮暮情。

行宮見月傷心色，夜雨聞鈴腸斷聲。

天旋地轉迴龍馭，到此躊躇不能去。

馬嵬坡下泥土中，不見玉顏空死處。

君臣相顧盡霑衣，東望都門信馬歸。

歸來池苑皆依舊，太液芙蓉未央柳；

芙蓉如面柳如眉，對此如何不淚垂？

春風桃李花開日，秋雨梧桐葉落時。

西宮南內多秋草，落葉滿階紅不掃。

梨園子弟白髮新，椒房阿監青娥老。

夕殿螢飛思悄然，孤燈挑盡未成眠。

遲遲鐘鼓初長夜，耿耿星河欲曙天。

鴛鴦瓦冷霜華重，翡翠衾寒誰與共？

悠悠生死別經年，魂魄不曾來入夢。

臨邛道士鴻都客，能以精誠致魂魄；

為感君王輾轉思，遂教方士殷勤覓。

排空馭氣奔如電，升天入地求之遍；

上窮碧落下黃泉，兩處茫茫皆不見。

忽聞海上有仙山，山在虛無縹緲間。

樓閣玲瓏五雲起，其中綽約多仙子。

中有一人字太真，雪膚花貌參差是。

金闕西廂叩玉扃，轉教小玉報雙成。

聞道漢家天子使，九華帳裡夢魂驚；

攬衣推枕起徘徊，珠箔銀屏迤邐開。

雲鬢半偏新睡覺，花冠不整下堂來。

風吹仙袂飄飄舉，猶似霓裳羽衣舞。

玉容寂寞淚闌干，梨花一枝春帶雨。

含情凝睇謝君王，一別音容兩渺茫。

昭陽殿裡恩愛絕，蓬萊宮中日月長。

回頭下望人寰處，不見長安見塵霧。

唯將舊物表深情，鈿合金釵寄將去。

釵留一股合一扇，釵擘黃金合分鈿。

但教心似金鈿堅，天上人間會相見。

臨別殷勤重寄詞，詞中有誓兩心知，

七月七日長生殿，夜半無人私語時：「

在天願作比翼鳥，在地願為連理枝。」

天長地久有時盡，此恨綿綿無絕期。
'''

print ("------------------------------------------")
#請使用者輸入一文字
#計算該文字在文章出現次數
#列印出現次數
string = input()
s_num = s.count(string)
print(s_num)

print ("------------------------------------------")
#把文字中 '。，\n；：？「」'的標點符號去除
for i in '。，\n；：？「」':
    s = s.replace(i,'')
#目前已知出現最多次的字的次數
#目前已知出現最多次的字
maxstr = ''
maxct = 0

print('文章總字數:',len(s))

for astr in s:
    #print(astr)
    act=s.count(astr)
    # 如果 現在這個字出現的次數(act) 大於 目前已知出現最多次字的次數
        #就讓 現在這個字出現的次數 成為 目前已知出現最多次的字的次數
        #還要記錄 現在這個字(astr) 到 目前已知出現最多次的字
    if act > maxct:
        maxct = act
        maxchar = astr
else:
    print(maxchar,maxct)


# In[50]:


# Get user email address
email = input("What is your email address?: ").strip()

# Slice out the user name
user_name = email[0:email.index('@')]

# Slice the domain name
domain_name = email[email.index('@')+1:len(email)]

# Format message
output = "Your username is '{}' and your domain name is '{}'".format(user_name,domain_name)

# Display output message
print(output)


domain = {'gmail.com':'Google','yahoo.com.tw':'Yahoo','ntu.edu.tw':'臺大','hotmail.com.tw':'Hotmail','hotmail.com':'Hotmail'}
if domain_name in domain:
    output = "這是註冊在 {} 之下的 Email 地址'".format(domain[domain_name])
else:
    output = "這是在 {} 之下自定義域'".format(domain[domain_name])
print(output)


# # 05 - Email 域名判斷器（Email slicer）
# #### 請用戶輸入 Email 地址，然後判斷它是自定義域名還是熱門域名。
# 
# > 題目：<br>
# 輸入(Input):shelly200318@hotmail.com.tw  <br>
# 輸出(Output):Your username is 'shelly200318' and your domain name is 'hotmail.com.tw' <br>
# 
# 
# * 進階：把常用的信箱存成字典，加入判斷是否為
# >輸入(Input):mary.jane@gmail.com  <br>
# 輸出(Output):這是註冊在 Google 之下的 Email 地址 <br>
# 輸入(Input):matt.pan@myfantasy.com  <br>
# 輸出(Output):這是在 myfantasy 之下自定義域
# 
# 

# ### 06 - 及格名單（Pass list）
# #### 請使用集合功能來完成各科級名單的判斷
# ```
# 米花市帝丹小學一年级B班正舉辦期中考試
# 數學及格的有：柯南、灰原、步美、美環、光彦
# 英文及格的有：柯南、灰原、丸尾、野口、步美
# 以上已列出全班所有人
# ```
# 
# >請分別列出<br>
# 數學及格但英文不及格的同學名單<br>
# 數學不及格但英文及格的同學名單<br>
# 兩者皆及格名單<br>
# * Hint:差集(減法)、交集
# 

# In[ ]:





# In[52]:


m={'柯南','灰原','步美','美環','光彦'}
e={'柯南','灰原','丸尾','野口','步美'}
a=m.intersection(e)
print(a)
print(type(a))
al=list(a)
al.sort()
print(al)

b=m.difference(a)
bl=list(b)
bl.sort()
print(bl)

c=e.difference(a)
cl=list(c)
cl.sort()
print(cl)

full = m.union(e)
dl=list(full)
dl.sort()
print(dl)


# ### 07 - 查詢路徑下所有檔案
# #### 請使用者輸入路徑，自動抓取路徑下所有檔案名稱
# 
# >輸入(Input):data\testfile 或 D:\code\ML_202105\data\testfile  <br>
# 輸出(Output):
# ```
# I'm a directory: file1
# I'm a directory: file2
# I'm a File: hw_07945001.txt
# I'm a File: hw_079450010.doc
# I'm a File: hw_07945002.txt
# I'm a File: hw_07945003.txt
# I'm a File: hw_07945004.txt
# I'm a File: hw_07945005.txt
# I'm a File: hw_07945007.txt
# I'm a File: hw_07945008.txt
# I'm a File: hw_07945009.txt
# ```
# 
# * 進階: 把file的學號抓出來，另存成一個新的csv檔

# In[59]:


import os

# 請使用者輸入或指定要查詢的路徑
yourPath = input()
# 列出指定路徑底下所有檔案(包含資料夾)
allFileList = os.listdir(yourPath)

# 逐一查詢檔案清單
for file in allFileList:
#   這邊也可以視情況，做檔案的操作(複製、讀取...等)
#   使用isdir檢查是否為目錄
#   使用join的方式把路徑與檔案名稱串起來(等同filePath+fileName)
    if os.path.isdir(os.path.join(yourPath,file)):
        print("I'm a directory: " + file)
    #   使用isfile判斷是否為檔案
    elif os.path.isfile(os.path.join(yourPath,file)):
        print("I'm a File: " + file)


# ### 08 - 資料夾管理(shutil)
# #### 說明 ####
# 
# ```
# 在目前所在的目錄下建立一files資料夾
# 
# 令使用者輸入一數字N，並在files資料夾中建立f1, f2… fN等N個資料夾後列出files的資料夾內容
# 
# 將files資料夾裡的f1資料夾重新命名成folder1後再列出files的資料夾內容
# 
# 移除files資料夾中的folder1後再列出files的資料夾內容
# 
# 最後移除files資料夾
# ※須先退出files資料夾(os.chdir(../)) ![image.png](attachment:image.png)
# ```
# 

# In[103]:


import os
import shutil

os.chdir('/Users/bonnie/Downloads/Unit01')

if os.path.exists('files'):
    shutil.rmtree('files')
os.mkdir('files')

n = int(input())

for i in range(1, n+1):
    os.mkdir(f'files/f{i}')

print(os.listdir('files'))

os.rename('files/f1', 'files/folder1')

print(os.listdir('files'))
                 
shutil.rmtree('files/folder1')

print(os.listdir('files'))

os.chdir('/Users/bonnie/Downloads/Unit01')
shutil.rmtree('files')



# ### 09 - 回文判斷（Is a palindrome）
# #### 請使用者輸入單字，判斷它是否為回文，也就是該單字前後對稱，例如 madam，從前讀到後或是從後讀到前的順序都是 madam。
# 
# > 題目：<br>
# 輸入(Input): 雨 滋 春 樹 碧 連 天  天 連 碧 樹 春 滋 雨 <br>
# 輸出(Output):The text you have entered is a palindrome!<br>
# 輸入(Input): 資工訓練班 <br>
# 輸出(Output):The text you have entered is not a palindrome.
# 

# In[104]:


def convertInputString():
    #請使用者輸入一串字串，先轉換字串為統一小寫
    rawInput = input("\nPlease enter a word, phrase, or a sentence \nto check if it is a palindrome: ") 
    return rawInput.lower()


def stripAnalphabetics(dirtyList):
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""]
    #去除相關標點符號
    cleanlist = [char for char in dirtyList if char not in analphabeticList]
    return cleanlist

def runPalindromeCheck(straightList):
    reversedList = straightList[::-1]
    if straightList == reversedList:
        return "The text you have entered is a palindrome!"
    else:
        return "The text you have entered is not a palindrome."

def main():
    print("\nPalindrome checker")
    userInput = convertInputString()
    cleanInput = stripAnalphabetics(userInput)
    result = runPalindromeCheck(cleanInput)
    print(result)

main() 


# ### 10 - 總成績計算
# #### 說明 ####
# 
# 請讀取 `data/english_list.csv`與`data/math_list.csv`檔案(`utf-8`)後，將每位同學的英文與數學成績加總起來，並將檔案寫入至 `./Score.csv`中，編碼成`utf-8`<br>
# 最後列印出每位學生姓名與加總後的分數<br>
# <a href="data\english_list.csv">英文成績下載</a><br>
# <a href="data\math_list.csv">數學成績下載</a><br>
# 
# #### Input Format ####
# 
# <br>
# csv資料(英文成績)<br>
# csv資料(數學成績)<br>
# <br>
# 
# #### Output Format ####
# 
# <br>
# 
# ![](data\05.JPG)<br>
# <br>
# <br>
# (圖片參考用 以文字敘述為準)<br>
# 
# 
# 
# 
# #### Sample Input 1####
# 
# 
# 
# ```
# 無標準輸入，只有檔案輸入
# ```
# 
# 
# 
# #### Sample Output 1####
# 
# 
# ```
# 廖冠霖 142
# 王力中 124
# 張平舜 108
# .
# .
# .
# .
# .
# 陳姿茜 77
# 涂珮瑜 134
# 夏明哲 111
# 
# ```
# 
# 
# #### Hint ####
# 
# 
# 
# ```
# None
# ```
# 

# In[111]:


import os
os.chdir('/Users/bonnie1114/Desktop/git-repos/IMLP/Unit01/data')
fin_E = open('data/english_list.csv', 'r', encoding='UTF-8')
fin_M = open('data/math_list.csv', 'r', encoding='UTF-8')

lisE = []
lisM = []
name = []

for line in fin_E.readlines():
    line = line.strip().split(",")
    name.append(line[0])
    lisE.append(line[1])

for line in fin_M.readlines():
    line = line.strip().split(",")
    lisM.append(line[1])

score = []
fout = open("Score.csv", "w")
line = ''

for i in range(len(name)):
    score.append(int(lisE[i]) + int(lisM[i]))
    list1 = [name[i], str(score[i]), "\n"]
    print(name[i], str(score[i]))

    line = ",".join(list1)
    fout.write(line)

fin_E.close()
fin_M.close()
fout.close()

line = ''
fout = open("Score.csv", "r")
for i in range(len(name)):
    line = fout.readline()
    print(line)

fout.close()


# In[ ]:




