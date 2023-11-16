'''# def partition(pivot, arr): #work incorrect don't need
#     left, middle, right = [], [], []
#     for i in range(len(arr)):
#         if arr[i] < pivot:
#             left.append(arr[i])
#         elif arr[i] == pivot:
#             middle.append(arr[i])
#         else:
#             right.append(arr[i])
#     return left, middle, right
# def quick_sort(arr):
#     if len(arr) == 0:
#         return arr
#     else:
#         pivot = arr[0]
#         left, middle, right = partition(pivot, arr)
#     return quick_sort(left) + middle + quick_sort(right)'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [_ for _ in arr if _ < pivot]
    middle = [_ for _ in arr if _ == pivot]
    right = [_ for _ in arr if _ > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def quick_insertion_sort(arr):
    if len(arr) <= 1:
        return arr
    elif arr != sorted(arr):
        return quick_sort(arr)
    elif arr == sorted(arr):
        return insertion_sort(arr)

def insertion_sort(an_arr):
    for i in range(1, len(an_arr)):
        key = an_arr[i]
        j = i - 1
        while j >= 0 and key < an_arr[j]:
            an_arr[j + 1] = an_arr[j]
            j -= 1
        an_arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1