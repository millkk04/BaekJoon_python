n = int(input())

arr = list(map(int, input().split()))
arr2 = []
arr2.append(arr[0])
last = arr2[0]
for i in range(1,n):
    if arr[i] > last:
        
        arr2.append(arr[i])
        
    else:
        
        for j in range(len(arr2)):
            
            if arr2[j]>=arr[i]:
                arr2[j] = arr[i]
                break
    last = arr2[len(arr2) - 1]
                

print(len(arr2))
