def betterCountingSort(listOfNumbers):
    n = len(listOfNumbers)
    temp = zeros(n)

    for i in listOfNumbers:
        temp[i] += 1


