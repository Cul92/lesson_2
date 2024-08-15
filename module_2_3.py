my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while len(my_list) > 0:
    deleted_element = my_list.pop(0)
    if deleted_element > 0:
        print(deleted_element)
    if deleted_element < 0:
        break