'''
Написать скрипт, который выводит на экран «True», если элементы
программно задаваемого списка представляют собой возрастающую
последовательность, иначе – «False»
'''
trueList = [1,2,3,4,5,6]
falseList = [4,5,2,1,7,7]

orderedList = True
for i in range(0,len(trueList)-1):
    if trueList[i] > trueList[i+1]:
        orderedList = False
        break
print(orderedList)

'''
temp = trueList.copy()
temp2 = falseList.copy()

trueList.sort()
falseList.sort()

if trueList == temp:
    print("true")
else:
    print("false")

if falseList == temp2:
    print("true")
else:
    print("false")
'''
