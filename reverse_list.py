# Question: Write function that reverses a list, preferably in place.

def sol(arr):
    i = len(arr)-1
    while i > (len(arr)//2)-1:

        # swapping ith element from start with ith element from last
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
        i -= 1
    return arr


print(sol(arr=[3, 2, 1, 4, 5, 8]))

# ---------------------------------------------------------------------------------
# Method 2

arr1 = [3, 2, 1, 4, 5, 8]
print(arr1[::-1])
