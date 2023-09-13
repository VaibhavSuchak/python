#-------------tuple methods--------------

language = ("c","c++","java","python",".net","php","python","python")

#convert tuple into list
temp = list(language)

#append method perform in list
temp.append ("html",)

#remove  metod perform in list
temp.remove("java")

#change perticular difing index value
temp[3]="js"

#perform counting total no. of defing value is display
total=temp.count("python")
print(total)

#display index of defing  value
ind = temp.index("c++")
print(ind)

#change list into new tuple
#----- not modify last tuple --- create new tuple------ because it is immutale-----
language=tuple(temp)
print(tuple(language))


