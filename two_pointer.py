def pair_sum(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        s = arr[left] + arr[right]
        
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1
            
    return False

print(pair_sum([1, 2, 3, 4, 6], 6))

        