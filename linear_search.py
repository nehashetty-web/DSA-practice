def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i 
        else:
            return-1
    print(linear_search([2,3,4,7,3]),4)