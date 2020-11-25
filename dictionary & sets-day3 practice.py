# exercise 1 - merge 2 dict


def merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


dict1 = {'Maharashtra': 'Mumbai',
         'Karnataka': 'Bangalore',
         'Telangana': 'Hyderabad'}
dict2 = {'Andhra pradesh': 'Amaravati', 'Tamilnadu': 'Chennai'}
dict3 = merge(dict1, dict2)

print(dict3)

# exercise2 - remove a key

dict1.__delitem__('Maharashtra')
print(dict1)

# exercise3 - map 2 lists into dict

list1 = [1, 2, 3]
list2 = [4, 5, 6]

dict = dict(zip(list1, list2))
print(str(dict))

# exercise 4-  to find the length of a set
myset = {'hello', 'how', 'are', 'you'}
print(len(myset))

# exercise 5 - remove intersection of 2nd set from 1st set

set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6, 7}
print(set1,set2)
set2 = set2.difference(set1)

print(set2)
