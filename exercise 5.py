# Exercise 5

first_list = [2,3,4,5,6,7,8]
second_list = [4,9,16,25,36,49,64]
l1 = len(first_list)
l2 = len(second_list)
dictionary = {}
if l1 == l2:
    for i in range(0,l1):
        dic = {first_list[i]:second_list[i]}
        dictionary.update(dic)
print(dictionary)