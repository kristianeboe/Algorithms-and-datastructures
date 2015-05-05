for i in range(1,n):
    j = i-1
    while j>= 0 && numbers[j] > numbers[j+1]:
        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        j-=1
