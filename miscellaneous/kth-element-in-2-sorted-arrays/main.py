# binary search
# Time  O(logk)
# Space O(1)


def kthlargest(arr1, arr2, k):
    if len(arr1) == 0:
        return arr2[k]
    elif len(arr2) == 0:
        return arr1[k]

    mida1 = len(arr1)/2
    mida2 = len(arr2)/2

    if mida1 + mida2 < k:
        if arr1[mida1] > arr2[mida2]:
            return kthlargest(arr1, arr2[mida2+1:], k-mida2-1)
        else:
            return kthlargest(arr1[mida1+1:], arr2, k-mida1-1)
    else:
        if arr1[mida1] > arr2[mida2]:
            return kthlargest(arr1[:mida1], arr2, k)
        else:
            return kthlargest(arr1, arr2[:mida2], k)


print(kthlargest([1, 2, 3], [4, 5, 6], 5))
print(kthlargest([1], [4, 5, 6], 1))
print(kthlargest([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9], 5))
print(kthlargest([4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6], 5))
