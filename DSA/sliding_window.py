#sliding window
arr=[1,2,1,5,3,1,4,2]
k=3
max_sum=window_sum
for i in range(k,len(arr)):
    window_sum=window_sum-arr[i-k]+arr[i]
    if window_sum>max_sum:
        max_sum=window_sum

print(max_sum)
    