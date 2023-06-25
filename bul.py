# this program helps to find the largest number in a list and also counts the number of items in the list

smallest = None
print("Start:")
for value in [23, 15, 74, 9, 205, 11] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print("End: ",smallest)