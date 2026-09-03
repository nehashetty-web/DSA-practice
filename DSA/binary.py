arr = [2, 4, 6, 8, 10, 12, 14]
target = 12
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print("found")
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
#first occ
arr = [2, 4, 6, 8, 10, 12, 14]
target = 12
left=0
right=len(arr)-1
answer=-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        answer=mid
        right=mid-1
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
#secondf occ

arr = [1, 2, 2, 2, 4, 5]
target = 2

left = 0
right = len(arr) - 1
answer = -1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        answer = mid
        left = mid + 1

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

print(answer)