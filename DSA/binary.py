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

#lower bound
arr = [1, 2, 2, 2, 4, 5]
target = 2

left = 0
right = len(arr) - 1
answer = -1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] >=target:
        answer = mid
        left = mid + 1
    else:
        right=mid-1


#upper bound
arr = [1, 2, 2, 2, 4, 5]
target = 2

left = 0
right = len(arr) - 1
answer = -1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] >target:
        answer = mid
        left = mid + 1
    else:
        right=mid-1

#sorted array
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0

left = 0
right = len(arr) - 1

while left <= right:

    # find middle
    mid = (left + right) // 2

    # target found
    if arr[mid] == target:
        print(mid)
        break

    # left half is sorted
    if arr[left] <= arr[mid]:

        # target is in left half
        if arr[left] <= target < arr[mid]:
            right = mid - 1

        # target is in right half
        else:
            left = mid + 1

    # right half is sorted
    else:

        # target is in right half
        if arr[mid] < target <= arr[right]:
            left = mid + 1

        # target is in left half
        else:
            right = mid - 1

else:
    print(-1)
