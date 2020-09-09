# Question: Write a function that returns the elements on odd positions in a list.

def sol(arr):
    flag = True
    for i in arr:

        # check flag if True then odd else even
        if flag == True:
            print(i, end=' ')
            flag = False
        else:
            flag = True


sol(arr=[1, 2, 4, 5, 6])
#output = 1, 4, 6
# ----------------------------
print('\n')
# Method2


arr1 = [1, 2, 4, 5, 0]
for i in range(len(arr1)):
    if i % 2 == 0:
        print(arr1[i], end=' ')
