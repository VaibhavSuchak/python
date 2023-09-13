#tuple is immutable
tuple1 =(25,20.4,120,10,'vaibhav','suchak',210102116,"python","tuple")

#display tuple
print(tuple1)

#display type
print(type(tuple1))

#dspaly particular index
print(tuple1[2])

#change particalr index value
#tuple1[4] = 2054402
# tuple is immutable so  index of tuple is not change and error generate 

print(tuple1[2:6])

#display tuple length
print(len(tuple1))

#check condition in tuple
if 210102116 in tuple1:
    print("Yes, this is present in this tuple")
else:
    print("sorry, this is not found in this tuple")

#use old tuple index in new tuple and display 

#it take  stop index by  difault it self last index
tup=tuple1[-5:]
print(tup)


#-------------tuple methods--------------

language = ("c","c++","java","python",".net","php")

temp = list(language)
temp.append ("html")
temp.remove("java")
