#first fun -cretae list # 2nd fun-printing list-inside 1st fun use loop and create list and append values in list. and in 2nd fun print list using while loop.
def add_items(list1):
    i=0
    elements=int(input("Enter no of elements to be added:"))
    while len(list1)<elements:
       i=int(input("Enter an element to append to list:"))
       list1.append(i)
       i+=1
    return list1
    
def print_items(list1):
    j=0
    while j<len(list1):
        print(list1[j])
        j+=1
list1=[]
list1=add_items(list1)
print_items(list1)
    



        




