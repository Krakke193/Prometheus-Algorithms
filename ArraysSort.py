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


array = [6, 4, 5, 2, 3, 1]
func = bubble_sort
print('{func_name}: {arr}'.format(func_name=func.__name__, arr=func(array)))
