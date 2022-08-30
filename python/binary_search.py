def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1
    
    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

answer = binary_search(array, target, 0, n-1)

if answer == None:
    print("없음 ")
else:
    print(answer + 1) # index