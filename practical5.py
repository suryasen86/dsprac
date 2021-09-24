 
#  leniear  search
def search(list,n):
  
    for i in range(len(list)):
        if list[i] == n:
            return True
    return False
  
 
list = [1, 2, 'baby', 4,'noob', 6]
  
 
n = 'noob'
print('using linera search')
if search(list, n):
    print("Found")
else:
    print("Not Found")


#   Binary Search Function
 
print('using Binary search')
def binary_search(list, x):
    low = 0
    high = len(list) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
     
        if list[mid] < x:
            low = mid + 1
 
    
        elif list[mid] > x:
            high = mid - 1
 
       
        else:
            return mid
 
   
    return -1
 
 
 
x = 'baby'
 
# Function call
result = binary_search(list, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")