def clean(arr):
    new_arr = []
    for x in arr:
        if(new_arr.count(x) == 0):
            new_arr.append(x)
    # print(new_arr)
    return new_arr


def clean2(arr):
    return list(set(arr))


clean([1, 2, 3, 2, 3, 4, 6, 6, 6])
clean2([1, 2, 3, 2, 3, 4])
