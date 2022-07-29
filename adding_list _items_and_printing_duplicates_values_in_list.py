#how to sum items in a list using for loop

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#first set total to zero
total = 0

for item in my_list:
    total += item

print(total)

#printing single item of duplicates

my_list2 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 10]
duplicate_value = []

for item in my_list2:
    if my_list2.count(item) > 1:
        if item not in duplicate_value: 
            duplicate_value.append(item)
        
print(duplicate_value)