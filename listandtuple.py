#assigning the elements to lists

list1=[1,2,4,5,6]
print("before assigning",list1)
list1.append(8)
print("after assigning",list1)
list2=[8,5,6,7,8]
print("before assigning",list2)
list2.append(8)
print("after assigning",list2)



#accessing the elements from tuple

mytuple1=(1,3,5,6,8,9)
print(mytuple1)
print(mytuple1[3])
mytuple2=(9,9,6,7,8)
print(mytuple2)
print(mytuple2[1])


#deleteing elements from dictionary

dict1={"name":"archan","clas":"btech","ro":"i"}
print(dict1)
del dict1["name"]
print(dict1)
dict2={"1":"a","2":"b","3":"c"}
print(dict2)
del dict2["1"]
print(dict2)


