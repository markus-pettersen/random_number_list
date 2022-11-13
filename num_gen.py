import random

def num_generator(items, range, unique = True):
    new_list = []
    list_length = 0
    while list_length < items:
        random_int = random.randint(1, range)
        if unique:
            if not random_int in new_list:
                new_list.append(random_int)
                list_length += 1
                new_list.sort()
        else:
            new_list.append(random_int)
            list_length += 1

    return new_list


list_1 = num_generator(100, 6, False)
list_2 = num_generator(10, 100)
list_3 = num_generator(10, 100)
list_4 = num_generator(10, 100)

def write_list(a_list, file):
    with open(file, "w") as a_file:
        for num in a_list:
            print(num, file=a_file)

write_list(list_1, "new_numbers_1.txt")
