#take input as length of list
#create list for length
#create dictionaries inside list
#print the data using condition-while loop


list1=[]
n=int(input("Enter how many elements to be there in list:"))
while len(list1)<n:
    item=dict(Region=input("Enter Region name:"),Model=input("Enter Model name:"),Type=input("Enter Type name:"),Year=input("Enter Year:"))
    list1.append(item)
print(list1)
i=0
while i<len(list1):
    if list1[i]["Region"]=="India":
        print("The details For the mentioned region are as below:")
        print("Model:{}".format(list1[i]["Model"]),"Type:{}".format(list1[i]["Type"]),"Year:{}".format(list1[i]["Year"]))
    i+=1


