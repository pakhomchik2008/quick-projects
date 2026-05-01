'''def partition(array, first_index, last_index):
    pivot = array[first_index]
    pivot_index = first_index
    right_pointer = last_index
    left_pointer = first_index + 1

    while True:

        while left_pointer <= last_index and array[left_pointer] < pivot:
            left_pointer += 1

        while right_pointer >= first_index and array[right_pointer] > pivot:
            right_pointer -= 1

        if left_pointer < right_pointer:
            temp = array[left_pointer]
            array[left_pointer] = array[right_pointer]
            array[right_pointer] = temp
        else:
            break

    array[pivot_index] = array[right_pointer]
    array[right_pointer] = pivot

    return right_pointer

arr = [43, 3, 20, 4, 89, 77]
partition(arr, 0, len(arr) -1)
print(arr)'''


def merge(left, right):
    i = j = 0
    merged = []

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            merged.append(left[i])
            i += 1

        else:
            merged.append(right[j])
            j += 1

    merged += left[i:]
    merged += right[j:]

    return merged

arr = [6, 5, 12, 10, 9, 1]

merge([6,5,12],[10,9,1])

print(arr)