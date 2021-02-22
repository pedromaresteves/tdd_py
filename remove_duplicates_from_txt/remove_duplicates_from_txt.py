# import re

# with open("lista_original.txt") as lista:
#     txt_lines = lista.readlines()
#     lists_with_duplicates = list(map(lambda item: item.split(","), txt_lines))
#     lists_of_digits_with_duplicates = []
#     for list_item in lists_with_duplicates:
#         lists_of_digits_with_duplicates.append(
#             list(map(lambda item: re.match("[0-9]+", item)[0], list_item)))
#     result_list = []
#     for item in lists_of_digits_with_duplicates:
#         result_line = ''
#         new_item = list(set(item))
#         new_item.sort()
#         result_line = ','.join(new_item) + '\n'
#         result_list.append(result_line)

# with open("dingus.txt", "w") as write_file:
#     write_file.writelines(result_list)

with open("lista_original.txt") as lista:
    items = lista.read().split()

with open("result_file.txt", "w") as result_file:
    print(items)
    for item in items:
        result_item = list(set(item.split(",")))
        result_item.sort()
        result_file.write(','.join(result_item) + '\n')
