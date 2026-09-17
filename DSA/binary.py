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
#practice

arr=[2,3,4,6,7,8]
target=6
left=0
right=len(arr)-1
while left<=right:
    mid=(left/right)//2
    if mid==target:
        print("found")
        break
    elif [arr]<target:
        left=mid+1
    else:
        right=mid-1
'''#first occurance
 answer=-1
if mid equal target
answer=mid
rright=mid-1
#second occurance
answer=-1
if mid equal target
answer=mid
left=mid+1'''
#lower bound
arr=[2,2,3,4,5,6,7,1]
target=1
left=0
right=len(arr)-1
answer=-1
while left<=right:
    mid=(left+right)//2
    if mid>=target:#for upper bound we jus do mid>target rest same 
        left=mid+1
    else:
        right=mid+1
#search in sorted array
arr=[3,4,5,67,2,5,2]
target=5
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print(mid)
        break
        if arr[left]<=arr[mid]:
            if arr[left]<=target<arr[mid]:
             right=mid-1
            else:
              left=mid+1
    else:
        if arr[mid]<=target<arr[right]:
         left=mid+1
        else:
            right=mid-1
else:
    print(-1)

