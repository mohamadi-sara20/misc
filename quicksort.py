def swap(ar, i, j):
    temp = ar[i]
    ar[i] = ar[j]
    ar[j] = temp
    
    
def partition(ar, lo, hi):
    pivot = ar[hi]
    left_ind = lo
    right_ind = hi - 1
    while True:
        while ar[left_ind] < pivot:
            left_ind += 1
        while ar[right_ind] > pivot:
            right_ind -= 1
        if left_ind < right_ind:
            swap(ar, left_ind, right_ind)
            right_ind -= 1
            left_ind += 1
        else:
            break
    swap(ar, hi, left_ind)
    return left_ind


def quicksort(a, left, right):
    if right - left <= 0:
        return
    ind = partition(a, left, right)
    quicksort(a, left, ind - 1)
    quicksort(a, ind + 1, right)

