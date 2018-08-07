#returns the list, backwards.

my_list = [1, 32, 69]

def reverse_list(list):
    position = -1
    new_list = []
    for i in list:
        new_list.append(list[position])
        position = position - 1
    return new_list

print(reverse_list(my_list))
