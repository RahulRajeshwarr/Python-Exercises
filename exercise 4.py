# Exercise 4

list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
for i in list1:
    count = 0
    for j in list1:
        if i == j:
            count = count + 1
        else:
            continue
    print(i,count)