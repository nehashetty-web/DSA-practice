arr=[10,11,12,13,14]
print(arr[1])
for num in arr:
    print(num)
arr=[20,30,40,50,60]
largest=arr[0]
for num in arr:
    if num>largest:
        largest=num
print(largest)
arr=[20,30,40,50,60]
smallest=arr[0]
for num in arr:
    if num<smallest:
        smallest=num
print(smallest)
#sum
arr = [10, 20, 30, 40, 50]
total=0
for num in arr:
    total+=num
print(total)
# Count even numbers

arr = [1, 2, 3, 4, 5, 6]
count=0
for num in arr:
    if num%2==0:
        count+=1
print(count)
#second largest
arr = [10, 20, 30, 40, 50]
largest=arr[0]
second_largest=-1
for num in arr:
    if num>largest:
        second_largest=largest
        largest=num
print(second_largest)
#reverse 
arr=[2,8,6,4]
for num in range (len(arr)-1,-1,-1):
    print(arr[num])
#sorted
arr=[9,8,6,3,6]
sorted=True
for num in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        sorted=False
        break
    print(sorted)
#frequencies
arr=[9,8,5,2,6,2,9,2,1,5,6,6,6]
freq={}
for num in arr:
    if num in freq:
         freq[num]+=1
    else:
        freq[num]=1
print(freq)
#removing zeroes
arr=[1,0,2,0,4,2,4,0,0,]
result=[]
for num in arr:
    if num!=0:
        result.append(num)
        print(result)
        duplicates
arr=[1,0,2,0,4,2,4,0,0,]
result=[]
for num in arr:
    if num not in result:
        result.append(num)
        print(result)

#missing
arr = [1, 2, 3, 5, 6, 7]

n = 7

for i in range(1, n+1):
    if i not in arr:
        print(i)
#zeroes to end
arr = [1, 0, 2, 0, 4, 2, 4, 0, 0]

result = []

for num in arr:
    if num != 0:
        result.append(num)

zeros = len(arr) - len(result)

for i in range(zeros):
    result.append(0)

print(result)  

#mock test
arr = [23, 45, 12, 67, 34]
largest=arr[0]
for num in arr:
    if num>largest:
        largest=num
print(largest)


arr = [5, 10, 15, 20] 
for num in range(len(arr),-1,-1,-1):
    print(arr[num])

arr =[2, 5, 8, 11, 15]
sorted=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        sorted=False
        break
print(sorted)

arr = [4, 0, 6, 0, 2, 8, 0]
result=[]
for num in arr:
   if num!=0:
       result.append(num)
zeroes=len(arr)-len(result)
for i in range(zeroes):
        result.append(0)
print(result)
    #two pointers

arr = [10, 20, 30, 40, 50]
left=0
right=len(arr)-1

while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
    print(arr)

    #reverse a string
    s=['s','b','a','w','r']
    left=0
    right=len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
        print(s)

# valid palindrome
s="racecar"
left=0
right=len(s)-1
while left<right:
    if s[left]!=s[right]:
        print("false")
        break
    left+=1
    right-=1
else:
    print("true")

#move zeroes

arr=[0,1,2,3,0,1,4,0]
slow=0
for fast in range(len(arr)):
 if arr[fast]!=0:
    arr[slow],arr[fast]=arr[fast],arr[slow]
    slow+=1
print(arr)

# Remove Duplicates (Sorted Array)

arr = [1, 1, 2, 2, 3, 3, 4]

# slow points to the last unique element
slow = 0

# fast checks every element from index 1
for fast in range(1, len(arr)):

    # If current element is different, it is a new unique element
    if arr[fast] != arr[slow]:

        # Move slow to the next position
        slow += 1

        # Copy the new unique element
        arr[slow] = arr[fast]

# Print only the unique elements
print(arr[:slow + 1])

#two sum
arr=[2,7,11,15]
target=9
left=0
right=(len(arr)-1)
while left<right:
    total=arr[left]+arr[right]
    if total==target:
        print(arr[left],arr[right])
        break
    elif (total<target):
        left+=1
    else:
        right-=1



    




