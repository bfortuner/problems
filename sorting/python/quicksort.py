def sort(arr, start, end):
    if start >= end:
        return
    pivot = (start+end)/2
    i = start
    j = end
    while i < j:
        if arr[i] >= arr[pivot] and arr[j] <= arr[pivot]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i+=1
            j-=1
        else:
            if arr[i] < arr[pivot]:
                i+=1
            if arr[j] > arr[pivot]:
                j-=1
    sort(arr,start,pivot)
    sort(arr,pivot+1,end)




a1 = [12,5,6,2,4,13]
sort(a1,0,len(a1)-1)
print a1

a2 = [12,5,4,13]
sort(a2,0,len(a2)-1)
print a2

a3 = [12,5]
sort(a3,0,len(a3)-1)
print a3

a4 = [5]
sort(a4,0,len(a4)-1)
print a4

a5 = [12,5,5,12]
sort(a5,0,len(a5)-1)
print a5


