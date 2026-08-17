#hashing
#dictionary


arr=[2,5,7,5,2,2]
count={}
for num in arr:
   if num in count:
      count+=1
   else:
      count=1
print(count)
#set
seen=set()
arr=[1,2,3,2]
for num in arr:
   if num in seen:
      print("duplicate")
   else:
      seen.add(num)
print(seen)
#freq map
for num in arr:
   if num in count:
      count+=1
   else:
      count=1
print(count)
#duplicate detection
arr = [1, 2, 3, 2]

seen = set()

for num in arr:
    if num in seen:
        print("Duplicate")
        break
    else:
        seen.add(num)
#two sum
arr=[2,7,11,15]
target=9
seen={}
for i in range (len(arr)):
   needed=target-arr[i]
   if target in seen:
      print(seen[needed],i)
      break
seen[arr[i]]=i
#count elements:
arr=[1,3,3,5,52,5]
count = {}

for num in arr:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
