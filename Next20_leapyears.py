# Question: Write a program that prints the next 20 leap years.

curr = 2020
count = 0
while count < 20:
    curr = curr+4

    # only hundred every 400 years are leap years
    if curr % 100 == 0 and curr % 400 != 0:
        continue

    print(curr)
    count += 1
