w#take input as length of list
#create list for length
#create dictionaries inside list
#print the data using condition-for loop


list1=[]
n=int(input("Enter how many elements to be there in list:"))
for i in range(n):
    item=dict(Region=input("Enter Region name:"),Model=input("Enter Model name:"),Type=input("Enter Type name:"),Year=input("Enter Year:"))
    list1.append(item)
print(list1)
for e in list1:
    if e["Region"]=="India":
        print("The details For the mentioned region are as below:")
        print("Model:{}".format(e["Model"]),"Type:{}".format(e["Type"]),"Year:{}".format(e["Year"]))



            
        
    
        
    
    

