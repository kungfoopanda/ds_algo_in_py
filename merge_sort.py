def merge_sort(array1, array2):
    sorted_array = []
    i, j = 0, 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            sorted_array.append(array1[i])
            i += 1
        else:
            sorted_array.append(array2[j])
            j += 1
        print('Inside the while check ->', sorted_array)

    while i < len(array1):
        sorted_array.append(array1[i])
        i += 1

    while j < len(array2):
        sorted_array.append(array2[j])
        j += 1

    return sorted_array


def divide_array(my_array):
    if len(my_array) < 2:
        return my_array[:]
    else:
        middle = len(my_array) // 2
        l1 = divide_array(my_array[middle:])
        l2 = divide_array(my_array[:middle])
        print('divide ->', middle, l1, l2)
        return merge_sort(l1, l2)


sample_array = [50, 30, 29, 45, 5, 7, 9, 2, 3, 5, 9, 10, 12, 7]
print('Final ->', divide_array(sample_array))
