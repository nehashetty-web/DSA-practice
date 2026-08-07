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
    
window = arr[i-k]