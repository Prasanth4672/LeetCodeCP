def max_hep(arr,i,N):
	largest = i
	l=2*i+1
	r=2*i+2

	if l < N and arr[largest]<arr[l]:
		largest =l
	if r < N and arr[largest]< arr[r]:
		largest = r
	if largest!=i:
		arr[i],arr[largest] = arr[largest],arr[i]
		max_hep(arr,N,largest)



def heap_sort(arr):
	N=len(arr)
	for i in range(N//2 -1,-1,-1):
		  max_hep(arr,i,N)
		  
    


arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
    