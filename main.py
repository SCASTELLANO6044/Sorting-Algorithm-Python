import random

def quick_select (data, left, right, k):
    if left == right:
        return data[left]
    pivot_index = partition (data, left, right)

    if k == pivot_index:
        return data [k]
    elif k < pivot_index:
        return quick_select(data, left, pivot_index - 1, k)
    else:
        return quick_select(data, pivot_index - 1, right, k)

def partition (data, left, right):
    random_index = random.randint(0, len(data) - 1)
    return random_index

data = [7, 2, 1, 6, 8, 5, 3, 4]
k = 3

# data = [1, 2, 3, 4, 5, 6, 7, 8]
result = quick_select(data, 0, len(data) -1, k)

print(result)