def insertion_sort(arr, simulation=False):
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor

    return arr

arr=[]
file = open('New Text Document.txt',"r")
file=file.readlines()
for i in file:
    i=i.split()
    arr.append(i)
print(arr)
print("############################################################################")    
sorter=insertion_sort(arr)
print(sorter)