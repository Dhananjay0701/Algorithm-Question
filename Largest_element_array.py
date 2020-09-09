# Write a function that returns the largest element in a list.

def sol(arr):
    arr = [3, 6, 4, 7, 7, 4]
    max_ele = arr[0]
    for i in arr:
        # check if current element is greater than max_ele
        if i > max_ele:
            max_ele = i
    return max_ele


print(sol(arr=[3, 6, 4, 7, 7, 4]))
# --------------------------------------------
# Method-2

arr1 = [3, 6, 4, 3, 7, 4]
print(max(arr1))
