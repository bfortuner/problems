#include <iostream>
#include <stdlib.h>

using namespace std;


// Given an array, find the maximum difference between two array // elements given the second element comes after the first

// ex. array= [1,2,3,4,5,6,7]
// answer = 7-1

int max_difference(int *array,int size){
	int min=100;
	int max=0;

	// find min and max of array
	for (int x=0;x<size;x++){
		if (array[x] < min)
			min = array[x];
		if (array[x] > max)
			max = array[x];
	}
	cout << max << "-" << min << endl;
	return max-min;
}


int main() {
	int array[] = {1,2,3,4,5,6,7};
	cout << max_difference(array,7);
	return 0;
}