# import random

def ScoreMax(array):
    max=0
    for i in range(len(array)):
        if max < array[i]:
            max = array[i]
    return max

def OddScoreMax(array):
    num=0
    for i in range(len(array)):
        if 1==array[i]%2:
            num = num+1
    return num

def ThreeMin(a, b, c):
    if ((a<b)and(a<c)):
        return a
    elif (b<c):
        return b
    else:
        return c
print("異なる３つの整数を入力")
x=int(input("整数１："))
y=int(input("整数２："))
z=int(input("整数３："))
print("最小値：" +str(ThreeMin(x,y,z)))

"""
score=[]
print("リストに３０〜90をランダムに代入する")

for i in range(5):
    score.append(random.randint(30,90))
    print("点数" +str(i+1) +":"+ str(score[i]))
print("リスト内の最大値：" +str(ScoreMax(score)))
print("リスト内の奇数の個数：" +str(OddScoreMax(score)))


x=int(input("整数1:"))
y=int(input("整数1:"))

#min=Min(x,y)
#print("最小値：" + str(min))
print("最小値：" + str(Min(x,y)))



print("------------------------------")
print("穴埋め問題7")

sum=0


print("合計点" + str(sum))
print("平均点" + str(sum/len(score)))

print("------------------------------")
print("穴埋め問題8")
score=["A組"]
sum=0
max=0

for i in range(5):
    score.append(random.randint(30,100))
    if isinstance(score[i],int):
        sum +=score[i]
        print(str(i) + "人目の点数" + str(score[i]))
        if max <= score[i]:
            max=score[i]
print("合計点" + str(sum))
print("最大点" + str(max))
print("平均点" + str(sum/(len(score)-1)))

print("------------------------------")
print("穴埋め問題9")
data=["A組",45, 667, "B組","C組",56,89,"D組","E組"]
print(data)
num=0
i=0
for i in range(len(data)):
    if isinstance(data[i],str):
        num+=1
print("data内にある文字列のデータ数：" + str(num))

print("------------------------------")
print("穴埋め問題10")
data=[["A組",65, 67], ["B組","C組",55], [56,"D組",89]]
print(data)
sum=0
print("data内にある数字の合計点を算出します。")
i=0
j=0
for i in range(len(data)):
    for j in range(len(data[i])):
        if isinstance(data[i][j], int):
            sum =sum + data[i][j]
print("合計点:" + str(sum))





i=0
print("0，2，4，6と０から10まで２飛びで表示")

while i<=10:
    print("i=", i)
    i=i+2

# ---------------------------------------------

i=0
print("0，3，6，9と０から21まで3飛びで表示")

for i in range(0,21+1,3):
    print("i=", i)

# ---------------------------------------------
print("------------------------------")
print("穴埋め問題６")
print("30，28，26，24と30から0まで-2飛びで表示")
print("その中で２０〜25と５〜10の範囲内の数字を表示します")
for j in range(30, 0, -2):
    if ((j<=25 and j>=20 )or((j<=10 and j>=5 ))):
        print("j=", j)
"""