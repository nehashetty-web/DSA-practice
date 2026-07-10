#prefix
arr=[1,2,3,4,5,6]
prefix=[]
total=0
for num in arr:
    total+=1
    prefix.append(total)
print(prefix)

#range sum query
arr=[1,2,3,4,5,6]
prefix=[]
total=0
for num in arr:
    total+=1
    prefix.append(total)
left=1
right=3
if left==0:
    answer=prefix[right]
else:
    answer=prefix[right]-prefix[left-1]

print(answer)

# Find Equilibrium Index

arr = [1, 3, 5, 2, 2]

# Find total sum of the array
total = sum(arr)

# Initially, left side has no elements
left_sum = 0

# Traverse the array
for i in range(len(arr)):

    # Right sum = Total - Left sum - Current element
    right_sum = total - left_sum - arr[i]

    # If left and right sums are equal,
    # current index is the equilibrium index
    if left_sum == right_sum:
        print(i)

    # Add current element to left sum
    # for the next iteration
    left_sum += arr[i]




r