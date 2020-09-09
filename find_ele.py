# Question: Write a function that checks whether an element occurs in a list.

def sol(arr, target):
    for i in arr:
        # check if target is equal to current element

        if i == target:
            return True
    return False


print(sol(arr=[3, 4, 5, 7, 10], target=1))

# ---------------------------------------------------------------
# Method 2
arr1, tar = [3, 4, 5, 7, 10], 1
if tar in arr1:
    print(True)
else:
    print(False)
