#exercise 1
num_list = [2,4,6,8,10]
list.append(num_list,12)
print(num_list)

# exercise 2 --	Delete (using function)
list.__delitem__(num_list,2)
print((num_list))

#exercise3-
a=(max(num_list))
print(a)
#exercise 4

b=min(num_list)
print(b)

#exercise 5 - Tuple
my_tuple = (1,4,9,10)
rev = my_tuple[::-1]
print(rev)

# exercise 6 - convert tuple to list

tuple1 = ('my','name',10,20)
list1 = list(tuple1)
print (list1)
print(type(list1))
