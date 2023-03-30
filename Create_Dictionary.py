#Dictionary-key-value pair
#ordered,changeable and no duplicates
#Create dictionary:Method1
cars={ "type":"Ford","Model":"Aspire","Year":1994}
cars["Region"]={"Country":"India","V-Type":["Passanger","Commercial","Truck"]}
print(cars)
print(cars["Region"]["Country"])
print(cars["Region"]["V-Type"])
print(cars["Region"]["V-Type"][0])

#Create dictionary:Method2 using dict() constructor
cars=dict(typ="Ford",Model="Aspire",Year=1994)
print(cars)

print(type(cars))

print(len(cars))

#print(cars["Model"])#Access value using key


#No duplicates allowed-overwrite existing value
cars={ "type":"Ford","Model":"Aspire","Year":1994,"Year":1997}
print(cars)

#values in dictionary can be of any data type
cars={ "type":"Ford","Model":"Aspire","Year":1994,
       "colours":["red","blue","white"]}
print(cars)

print(cars["colours"])

print(cars["colours"][1])







