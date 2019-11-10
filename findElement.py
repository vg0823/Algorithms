#find element in rotated array
#steps 1 find pivot element and then search in array

def findPivot(s,start,end):
	print(start,end)
	if(start > end): 
		return -1
	if(start == end):
		return start

	mid = start + int((end-start)/2)
	print(mid)
	if(s[mid]<s[end]):
		return findPivot(s,start,mid)
	else:
		return findPivot(s,mid+1,end)

def main():
	s = [3,4,5,6,7,1,2]
	res = findPivot(s,0,len(s)-1)
	print(res)

if __name__ == "__main__":
    main()


