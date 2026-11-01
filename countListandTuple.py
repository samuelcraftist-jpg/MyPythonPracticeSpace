my_list = [1, 2, 2, 3, 3, 3]
my_tuple = (4, 4, 5, 5, 5, 6)


def count_items(data):
    for item in set(data):
        print(item, "occurs", data.count(item), "times")


print("List:")
count_items(my_list)

print("Tuple:")
count_items(my_tuple)