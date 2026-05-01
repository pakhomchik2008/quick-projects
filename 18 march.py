#1
from os.path import split
from turtledemo.sorting_animate import partition

from pandas import pivot

size = input('Enter size of array: ')
numbers = list(map(int,input('Enter numbers: ').split(' ')))
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
def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array)//2
    left = array[:middle]
    right = array[middle:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)
print('Merge sort implementation')
print(merge_sort(numbers))

def partition(array,first,last):
    pivot = array[first]
    pivot_index = first
    right_pointer = last
    left_pointer = first+1
    while True:
        while array[left_pointer] < pivot and left_pointer < last:
            left_pointer += 1
        while array[right_pointer] > pivot and right_pointer >= first:
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

def quick_sort(array,first,last):
    if last-first<=0:
        return
    else:
        partition_point = partition(array,first,last)
        quick_sort(array,first,partition_point-1)
        quick_sort(array,partition_point+1,last)
numbers2 = list(map(int, input('Enter numbers for quick sort: ').split()))
quick_sort(numbers2, 0, len(numbers2) - 1)
print('Quick sort:')
print(numbers2)
