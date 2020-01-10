if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    new_list = sorted(set(arr))
    print(new_list[-2])
