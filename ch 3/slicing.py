list = [1, 2, 3, 4, 5]
 # we can slice the list to get a new list with only the elements we want
secondlist = list[1:4]

print("The second list is:", secondlist, type(secondlist))

list.append(6)
list.insert(0, 0)

print("The updated list is:", list, type(list))