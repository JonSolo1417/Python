def countdown(num):
    arr=[]
    for x in range(num,-1,-1):
        arr.append(x)
    return arr

print(countdown(5))

def printAndReturn(num1,num2):
    print (num1)
    return num2

x =printAndReturn(5,10)
print("This is x: " + str(x))

def firstPlusLength(arr):
    return arr[0] + len(arr)
sum = firstPlusLength([1,2,3,4,5])
print(sum)

def ValuesGreaterThanSecond(arr):
    newList=[]
    count=0
    if len(arr) < 2:
        return False
    for x in range (0,len(arr)):
        if arr[x] > arr[1]:
            count+=1
            newList.append(arr[x])
    print (count)
    return newList
newList=ValuesGreaterThanSecond([1,2,6,1,4,6,8])
print(newList)
smallList = []
print(ValuesGreaterThanSecond([]))

def lengthVal(num1,num2):
    newList=[]
    for x in range (0,num1):
        newList.append(num2)
    return newList

print(lengthVal(6,2))
print(lengthVal(4,7))