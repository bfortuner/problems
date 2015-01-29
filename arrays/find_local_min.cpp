#include <iostream>
#include <stdlib.h>

using namespace std;

// function to find A local minimum in a array of distinct elements
// use binary search.

int find_local_min(int *array,int left,int right){
	if (left == right)
		return left;
	if (right-left ==1){
		if (array[left] < array[right])
			return left;
		else
			return right;
	}
	int mid = left + (right-left) / 2;
	int result = -1;
	if (array[mid-1] > array[mid] && array[mid+1] > array[mid])
		result = mid;
	else{
		if (array[mid-1] < array[mid])
			result = find_local_min(array,left,mid-1);
		else if (array[mid+1] < array[mid])
			result = find_local_min(array,mid+1,right);
	}
	return result;
}

int main() {
	int array[] = {11,5,12,7,4,0,6};
	cout << find_local_min(array,0,7);

	return 0;
}