'''list = [1,2,3,5,8]
target = 6

def search_target(target):
    if target in list:
        print(list, 'true')
        return list
    else:
        print(list,'false')
        return []

search_target(target)'''

'''
list =  [11,23,58,31,56,77,43,12,65,19]

target = 31

sorted_list = sorted(list)

def search_index(target):
    if target in sorted_list:
        print(sorted_list.index(target), 'true')
    else:
        print( 'false')


search_index(target)'''



'''
def bubble_sort(array):
    for i in range(len(array)):
        for j  in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
list = [5,2,9,1,5]
print(bubble_sort(list))'''


def insertion_sort(array):
    for i in range(0, len(array)):
        for j in range(i+1,len(array)-i):
            if array[i] > array[j]:
                array[i], array[j+1] = array[j+1], array[i]
                continue
        return array

list = [5,2,9,1,5]
print(insertion_sort(list))

