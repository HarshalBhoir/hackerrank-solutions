if __name__ == '__main__':
    n = int(input())
    i = 1
    numbers = []

    while i <= n:
        numbers.append(str(i))
        i+=1

    start = 0
    count = len(numbers)
    total = ""
    total =str(total)

    for number in numbers:
        total+=numbers[start]
        if start <= count:
            start+=1
    
    print(total)
