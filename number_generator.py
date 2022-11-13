# A program that generates two random lists of unique numbers in order.

import random # Import necessary modules

# Create two empty lists
list_1 = []
list_2 = []
# Set these variables to zero. We increment them when adding values
list_1_len = 0
list_2_len = 0

# Loop until we have 25 values in this list
while list_1_len < 25:
    # Generate a randint
    num1 = random.randint(1,75)
    # If it is not in the list, append it and increase the length by 1
    if not num1 in list_1:
        list_1.append(num1)
        list_1_len += 1

# Same logic as the first loop
while list_2_len < 25:
    num2 = random.randint(1,50)
    if not num2 in list_2:
        list_2.append(num2)
        list_2_len += 1

# sort both lists
list_1.sort()
list_2.sort()


# Open the file in write mode
with open("numbers1.txt", "w") as num_list_1:
    # iterate through the list, writing each number to the file
    for num in list_1:
        num_list_1.write(f"{num}\n")

# Same again for the second file
with open("numbers2.txt", "w") as num_list_2:
    for num in list_2:
        num_list_2.write(f"{num}\n")