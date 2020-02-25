#12345
import re
from collections import Counter
from scipy.spatial import distance
def got(word, a):
    s=0
    for i in range(0, a.__len__()):
        if a[i]==word:
            s=s+1
    return s


f = open('sentences.txt','r')
f1 = open('sentences.txt','r')
w=f1.read().lower()
re.split('[^a-z]',w)
data = f.read().lower().split("\n")
#разделение на строки, перевод всех букв в маленькие

a=dict()
i=0
for d in data:
    a[i]=d.replace('.','').replace(',','').replace('(','').replace(')','').replace('/','').replace('-','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','').split()
    #разделение каждой строки на слова

    i=i+1


print(a.__len__())
del a[a.__len__()-1]
print(a.__len__())
max_str_len=0
for i in range(a.__len__()):
    if max_str_len<list(a[i]).__len__():
        max_str_len=list(a[i]).__len__()


wLen=0
wk=0
wWords=[]

#Определим число уникальных слов в каждой строке и суммируем эти числа
for i in range(0, a.__len__()):
    wLen=0
    for j in a[i]:
        if j not in wWords:
            wWords.append(j)
            wLen=wLen+1
    wk=wk+wLen

print("wlen=",wk, 'ww',a.__len__())

#инициализация матрицы 22 на 254
print(wk," ",a.__len__())
m=[[0 for j in range(0, wk)] for i in range(0, a.__len__())]

a1=[]
for i in range(a.__len__()):
    a1=[]
    a1=list(a[i])
    c = Counter(a[i])
    for j in range(0, wWords.__len__()):
        t=got(wWords[j], a1)
        m[i][j]=t


for i in range(0, m.__len__()):
    print(m[i])


result=[]
r1=r2=1
i1=i2=0
for i in range (0, a.__len__()):
    r=distance.cosine(m[0],m[i])
    result.append(r)
    if r<r1 and r != 0:
        r1=r
        i1=i

for i in range (0, result.__len__()):
    if result[i]<r2 and result[i]>r1:
        r2=result[i]
        i2=i

print("Res")
for i in range(0, a.__len__()):
    print(result[i])

print()
print(r1, " ", i1)
print(r2," ", i2)
f.close()
f = open('result.txt', 'w')
f.write(str(i1))
f.write(" ")
f.write(str(i2))
f.close()
f1.close()