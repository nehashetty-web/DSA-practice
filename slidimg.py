def sliding(arr,k):
    n=(len(arr))
    if n<k:
        return None
    window_sum=sum(arr[:k])
    max_sum=window_sum

    for i in range(n-k):
        window_sum= window_sum-arr[i]+arr[i+k]
        max_sum = max(window_sum,max_sum)
    return max_sum
print(sliding([2,3,4,6,7,8],3))