arr = [4, 2, 7, 1, 9, 3]
largest=0
second_largest=-1
for num in arr:
    if num >largest:
        second_largest=largest
        largest=num
    elif num > second_largest:
      second_largest = num
print(second_largest)

arr = [1, 2, 3, 4, 5, 6]
target = 9
left=0
right=len(arr)-1
while left<right:
   total=arr[left]+arr[right]
   if total==target:
      print(arr[left],arr[right])
      break
   elif total<target:
      left+=1
   else:
      right-=1

arr = [2, 4, 1, 3, 5]    
prefix=[]
total=0
for num in arr:
    total+=num
    prefix.append(total)
left=1
right=3
if left==0:
    answer=prefix[right]
else:
    answer=prefix[right]-prefix[left-1]

#after mid recap
arr = [2, 4, 1, 7, 3, 7, 5]
largest=0
second_largest=-1
for num in arr:
   if num>largest:
    second_largest=largest
    largest=num
   elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)


arr = [2, 1, 5, 2, 3, 2]
target = 7
left=0
current=0
answer=len(arr)+1
for right in range(len(arr)):
   current+=arr[right]
   while current>=target:
      answer=min(answer,right-left+1)
      current+=arr[left]
   left+=1