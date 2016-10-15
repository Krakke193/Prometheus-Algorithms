import math


def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key
    return a


def bubble_sort(a):
    for i in reversed(range(len(a))):
        for j in range(i):
            if a[j] > a[i]:
                a[j], a[i] = a[i], a[j]
    return a


def merge_sort(a):
    def perform(alist):
        if len(alist) > 1:
            mid = len(alist) // 2
            left_arr = alist[:mid]
            right_arr = alist[mid:]

            # Recursive call onto the array, until we reach elemental nodes that contains only two numbers
            merge_sort(left_arr)
            merge_sort(right_arr)

            # So when we reach this level (two numbers only) we begin to sort elemental nodes first
            # and after that the complex nodes at the higher recursive level. Until we sort the whole array.
            left_arr.append(math.inf)
            right_arr.append(math.inf)
            i, j, k = 0, 0, 0

            for k in range(0, len(alist)):
                if left_arr[i] < right_arr[j]:
                    alist[k] = left_arr[i]
                    i += 1
                else:
                    alist[k] = right_arr[j]
                    j += 1

    perform(a)
    return a


array = [6, 4, 5, 9, 3, 1, -4, 2]
func = merge_sort

print()
print('Unsorted array: {arr}'.format(arr=array))
print('Method is: {name}'.format(name=func.__name__))
print('Sorted array: {sorted_arr}'.format(sorted_arr=func(array)))
