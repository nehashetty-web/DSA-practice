#sliding window fixed K
arr=[1,2,1,5,3,1,4,2]
k=3
window_sum = sum(arr[:k])
max_sum=window_sum
for i in range(k,len(arr)):
    window_sum=window_sum-arr[i-k]+arr[i]
    if window_sum>max_sum:
        max_sum=window_sum

print(max_sum)

#average size K
arr=[1,2,1,5,3,1,4,2]
k=3
window_sum = sum(arr[:k])
result=[]
result.append(window_sum/k)
for i in range(k,len(arr)):
    window_sum=window_sum-arr[i-k]+arr[i]

result.append(window_sum/k)
print(result)
    

#smallest subarray:
arr = [2, 1, 5, 2, 3, 2]
target = 7
left=0
current=0
answer=len(arr)+1#as we want min we start with max by +1
for right in range(len(arr)):
    current+=arr[right]
    while current>=target:
        answer=min(answer,right-left+1)
        current-=arr[left]
        left+=1

print(answer)


#longest substring without repeating
s="abcbcabcda"
left=0
seen=set()
maximum=0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove (s[left])
        left+=1
    seen.add(s[right])
maximum=max(maximum, right-left+1)
print(maximum)


# Fruits Into Baskets

fruits = [1, 2, 1, 2, 3]

left = 0
maximum = 0
count = {}

for right in range(len(fruits)):

    if fruits[right] in count:
        count[fruits[right]] += 1
    else:
        count[fruits[right]] = 1

    while len(count) > 2:

        count[fruits[left]] -= 1

        if count[fruits[left]] == 0:
            del count[fruits[left]]

        left += 1

    maximum = max(maximum, right - left + 1)

print(maximum)



