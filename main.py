def quick_select(items):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def select(arr, low, high, k):
        if low < high:
            pivot_index = partition(arr, low, high)

            if pivot_index == k:
                return arr[pivot_index]
            elif pivot_index > k:
                return select(arr, low, pivot_index - 1, k)
            else:
                return select(arr, pivot_index + 1, high, k)

        return arr[low]

    n = len(items)
    k = (n - 1) // 2  # Índice de la mediana

    return select(items, 0, n - 1, k)


print(quick_select((1, 3, 2, 4, 8, 5)))