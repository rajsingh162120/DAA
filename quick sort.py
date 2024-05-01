def partition(array,low,high):
    pivot=array[high]
    i=low-1
    
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            array[i],array[j]=array[j],array[i]
    
    array[i+1],array[high]=array[high],array[i+1]
    return i+1

def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)
        
if __name__ == '__main__':
    array=[15,13,11,5,2,7]
    N=len(array)
    quicksort(array,0,N-1)
    print("SORTED ARRAY:")
    for x in array:
        print(x,end='\t')                