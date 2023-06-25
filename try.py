# this program helps to find the largest number in a list and also counts the number of items in the list
highest_num = 0
counter = 0
print("Lowest Number = ", highest_num)
for digits in [23, 15, 74, 9, 205, 11] :
    counter = counter + 1
    if digits > highest_num:
        highest_num = digits
    print(counter, highest_num, digits)
print("Higest Number = ", highest_num)
