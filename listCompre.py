if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    coordinates = [[i, j, k] for i in range(x + 1) 
                             for j in range(y + 1) 
                             for k in range(z + 1) 
                              if i + j + k != n ]

print(coordinates)



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_value= max(arr)
    arr = [i for i in arr if i!=max_value]
    print(max(arr))
