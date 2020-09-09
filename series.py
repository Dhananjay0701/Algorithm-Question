# Question: Write a guessing game where the user has to guess a secret number.After every guess the
# code tells the user whether their number was too large or too small. At the end the number of tries
# needed should be printed. It counts only as one try if they input the same number multiple times
# consecutively.


# function takes input number, target number, already used element, no. of tries
def helper(trial, num, tried, count):

    # check if input no. is less than target
    if trial < num:
        return ('Less')

    # check if input no. is more than target
    if trial > num:
        return ('More')

    # input no. is equal to target
    if trial == num:
        return 'No. of tries: {}'.format(count+1)


def main():
    tried = []
    count = 0
    while True:
        trial = input()  # taking user input

        # input break to break the code
        if trial == 'break':
            break
        trial = int(trial)
        func = helper(trial, 10, tried, count)

        # check if input no. is already tried if not add no. of tries
        if trial not in tried:
            count += 1
            tried.append(trial)
        print(func)

main()
