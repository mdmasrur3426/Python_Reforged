n = int(input())
arr = map(int, input().split())
z = max(arr)
while max(arr) == z:
    arr.remove(max(arr))

print(max(arr))