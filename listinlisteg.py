list1=[1,2,3]
list2=['a','b','c']
list3=[]
list3.append(list1)
list3.append(list2)
print(list3)
print(list3[1][1])

list4=[[1,2,3],['c','d','g']]
print(list4)
list5=[[11,2,3],['t','h','j'],["jhon","Sam"],[1,45,'g']]
print(list5)
list5[2][1]="jam"
print(list5)
tup1=tuple(list5)
print(tup1)
tup1[2][1]="sam"
print(tup1)
del tup1[2][1]
print(tup1)

print(type(tup1))


