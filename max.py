def largest(arr, n):
 
    max = arr[0]
 
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = input("enter values: ").split()
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)
