#  https: // cs50.harvard.edu/summer/2025/notes/3/

arr = [14, 44, 14, 56, 5, 77, 9, 10]
arr2= [1,2,3,4,5,6]


def merge_sort(arr):
    # for  i in range 
    if len(arr) <= 1 :
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    sorted_left= merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left,sorted_right)

def merge(left,right):
    result = []
    l=r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else: 
            result.append(right[r])
            r+=1
    result.extend(right[r:])
    result.extend(left[l:])
    return(result)

unsorted_arr =[2,8,15,88,4,3,4,7,9,1,5]
sorted_arr =merge_sort(unsorted_arr)
print(sorted_arr)
        

unsorted_arr.sort()
print(unsorted_arr)







def bubble_sort(arr):
    if not arr:
        return 'no array'

    arr_len = len(arr)
    for i in range(arr_len):
        swapped = False
        for j in range(arr_len - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            print('already sorted')
            break  # array already sorted
    return arr
print(bubble_sort(arr2))

def selection_sort(arr):
    arr_length = len(arr)
    if not arr:
        return
    for i in range(arr_length-1):
       
        min_index = i  # >>>  first element to be the smallest 
        for insider in range(i+1, arr_length): 
            if arr[insider] < arr[min_index]:
                min_index = insider
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(selection_sort(arr))


def rec(arr):
    ser=5
    if not arr :
        return 'no array'
    mid = len(arr)//2
    left=0
    right=len(arr)-1
    for i in range (len(arr)):
        mid = (left+right)//2
        if arr[mid]==ser:
            return arr[i],i
        if  arr [mid]<ser:
            rec(arr[mid+1])
        if arr[mid]>ser:
            rec(arr[:mid])
    return arr ,ser 
print(rec(arr))
      
      
      
def binary_search(arr):
    left =0 
    right = len(arr)
    ser = 15
    while left < right :
        mid = (left+right)//2
        if ser == arr[mid]:
            return arr[mid],mid 
        if ser < arr[mid]:
            right = mid
        if ser > arr[mid]:
            left = mid+1
print(binary_search([1,2,3,5,15,20]))
   
def pyrm(num):
   for i in range(num):
       print('#'*i)
        
print(pyrm(5))
         
    
# ! recursion


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        return fibonacci(n-1) , fibonacci(n-2)
print(fibonacci(5))

def factoriall(n):
    if n == 1:
        return 1
    else :
        return n * factoriall(n-1)
        
  
  
print(factoriall(5))