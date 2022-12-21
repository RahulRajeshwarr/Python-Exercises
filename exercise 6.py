# Exercise 6

first_list = [23,42,65,57,78,83,29]
second_list = [57,83,29,67,73,43,48]
final_list = []
for i in first_list:
    if i in second_list:
        pass
    else:
        final_list.append(i)
print(final_list)