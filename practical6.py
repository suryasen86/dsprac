import sys
n=int(input(' (1) for bubble sort (2) for insertion sort (3) for selection sort'))

arr = [64, 34, 25, 12, 22, 11, 90]

if n==1:
    
    def bubbleSort(arr):
        n = len(arr)

        
        for i in range(n-1):
        
            for j in range(0, n-i-1):
    
                if arr[j] > arr[j + 1] :
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] 


    bubbleSort(arr)

    print (" bubbleSort Sorted array is:")
    for i in range(len(arr)):
        print ("% d" % arr[i]), 
elif n==2:


    def insertionSort(arr): 
        for i in range(1, len(arr)):
    
            key = arr[i] 
            j = i-1
            while j >=0 and key < arr[j] :
                    arr[j+1] = arr[j]
                    j -= 1
            arr[j+1] = key
    
    
    print ("insertionSort Sorted array is:")
    for i in range(len(arr)):
        print ("%d" %arr[i])
  
 
 
elif n==3:
 
    for i in range(len(arr)):
    
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
            
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    
    print (" selected Sorted array")
    for i in range(len(arr)):
        print("%d" %arr[i]),
else:
    print ("wrong input")