sumlist1=[]
finaleleone=0
elefour=0
CharList=[]
print("welcome to password Generator")
name = input("PLEASE ENTER YOUR NAME :-")
print("the name you entered is : ")
print(name)
CharList1 = list(name)
print(CharList1)
size = len(name)
print("size")
print(size)
for i in range(0,size,2):
    CharList.append(CharList1[i])
print("even list")

print(CharList)
CharList.sort()
print(" PLEASE ENTER YOUR AGE ")
DATE = int(input("ENTER THE DATE :"))
MONTH = int(input("ENTER THE MONTH :"))
YEAR = int(input("ENTER THE YEAR :"))
print(DATE)
print(YEAR)
print(MONTH)
tempdate=DATE
sumd=0
while(tempdate > 0):
    reminder = tempdate%10
    sumd=sumd+reminder
    tempdate = tempdate//10
print(sumd)
summ=0
tempmonth=MONTH
while(tempmonth > 0):
    reminder = tempmonth%10
    summ =summ+reminder
    tempmonth = tempmonth//10
print(summ)
sumy=0
tempyear=YEAR
while(tempyear > 0):
    reminder = tempyear%10
    sumy =sumy+reminder
    tempyear = tempyear//10
print(sumy)
CharList.sort()
print(CharList)
for i in range(size):
    if(CharList[i]==' '):
      print()
    else:
        eletwo=CharList[i]
        break

finalsum=sumd+summ+sumy
print("finalsum")
print(finalsum)
tempeleone=0
while( finalsum > 0):
    reminder = finalsum%10
    tempeleone =tempeleone+reminder
    finalsum = finalsum//10
print("---")
print(tempeleone)
eleone=0
if(tempeleone>9):
    while (tempeleone > 0):
     reminder = tempeleone % 10
     eleone = eleone + reminder
     tempeleone = tempeleone // 10
    finaleleone=eleone
else:
    finaleleone=tempeleone
print("elemnt 1")
print(finaleleone)
print("elemnt 2")
print(eletwo)
indexsum=0
for i in range (size):
    indexsum=indexsum+i
tempele3=0
print("indexsum")
print(indexsum)
while( indexsum > 0):
    reminder = indexsum%10
    tempele3=tempele3+reminder
    indexsum = indexsum//10
print("temp3")
print(tempele3)
print("tempele32")
temporary=tempele3
tempele32=0
while( temporary > 0):
    reminder = temporary%10
    tempele32=tempele32+reminder
    temporary = temporary//10
print(tempele32)
spllist=['~','!','@','#','$','%','^','&','*']
elethree=spllist[tempele32]
print("element 3")
print(elethree)
print("size")
print(size)
dummyval=0
if(size>9):
    while (size > 0):
        reminder = size % 10
        dummyval = dummyval + reminder
        size = size // 10
    elefour=dummyval
else:
    elefour=size

print("element 4")
print(elefour)
print("the secured 4 digit pin for you is :-")
print(finaleleone)
print(eletwo)
print(elethree)
print(elefour)
print("test build !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("sorry for the above mess")