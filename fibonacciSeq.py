def FibonacciOddSum(maxFib):
    # Special case
    if maxFib <= 0:
        print("Invalid input")
        return -1
    elif maxFib == 1:
        return 1
    # First 2 number of seq with their sum as start.
    firstNum = 1;
    secNum = 1;
    oddSum = 2
    while firstNum + secNum <= maxFib:
        currentNum = secNum + firstNum
        if currentNum % 2 == 1:
            oddSum += currentNum
        firstNum = secNum
        secNum = currentNum
    return oddSum


print(FibonacciOddSum(2))
