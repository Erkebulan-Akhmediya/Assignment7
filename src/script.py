n1, n2 = 0, 1
count = 0

while count < 10:
    print(n1, end=" ")
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1