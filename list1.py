list=[]
("empty list.....\n\n")

list=[1,"python",20.5,True,"vaibhav","suchak"]
print(type(list))                   #print type 

print(len(list))                    #print length of list

print(list[1:3])                    #slicing
print(list[-2])                     #accessing list using neg. index


list2=["python","hello",20,30.4]
print(list + list2)                 #concate  using + operator


a=(input("Search here:"))

if a  in list:
        print(f"yes {a} is in  list")
else:
        print(f"sorry, {a} is not found in list")


list[4] = 2054402
print(list)