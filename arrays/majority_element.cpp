#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <vector>

using namespace std;

// Moore's Voting algorithm
// 1. Get an element occuring most of the time in the array. 
//    This phase will make sure that if there is a majority element 
//	  then it will return that only.
// 2. Check if the element obtained from step 1 is the majority element

// Function to check if the candidate occurs more than n/2 times 
// where n is the size of the vector
bool isMajority(vector<int> &tmp,int candidate){
	int i, count =0;
	for(i = 0; i < tmp.size(); i++){
		if (tmp[i] == candidate)
			count++;
	}
	if (count > tmp.size()/2)
		return 1;
	else 
		return 0;
}
// function to find candidate for the majority
int findCandidate(vector<int> &tmp){
	int maj_index=0, count=1;
	int i;
	for (i=1; i<tmp.size(); i++)
	{ 
		if (tmp[maj_index] == tmp[i])
			count++;
		else
			count--;

		if(count == 0){
			maj_index = i;
			count = 1;
		}
	}
	return tmp[maj_index];
}


void printMajority(vector<int> &tmp){
	// find candidate for Majority
	int candidate = findCandidate(tmp);

	// Print candidate if it is majority
	if (isMajority(tmp,candidate))
		cout << candidate << " is Majority element" << endl;
	else
		cout << "No majority element." << endl;
}

int main() {
	int myints[] = {1,3,3,1,2};
	vector<int> tmp (myints,myints+3);
	printMajority(tmp);

	return 0; 
}