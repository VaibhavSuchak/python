#set is unordered
set={'jan','fab','mar','apr','may','aug','dec'}
#print(set)

#create dynamic set user get value 
set11=(input("Enter Set:"))
set1=set11()

#display set type
#print(type(set))

#create new set

#adding(append) (changes) is not posible in set
  #set.add('jun')

#to add the data first convert set into list and perform operation
templist=list(set)
print(templist)
