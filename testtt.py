arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
k = [4,5]
left = arr[0:k[0]]
right = arr[k[1]+1:(len(arr))]
to_rev = arr[k[0]:k[1]+1]

sol = []

for i in to_rev:
    sol.insert(0, i)
        
arr1 = left + sol + right
print(arr1)