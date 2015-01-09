#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

// Program that takes in a 2D SORTED matrix of integers
// Goal: find the row with the most number of ones


int find_row(vector<vector<int> >&tmp){
	if (tmp.size() == 0){
		return -1;
	}
	else {
		int max = 0; 
		int count = 0;
		int index = -1;
		for (int x=0;x<tmp.size();x++){
			for (int y=0;y<tmp[x].size();y++){
				if (tmp[x][y] ==1)
					count++;
			}
			if (count > max){
				max = count;
				index = x;
			}
			count = 0;
		}
		return index;
	}	
	
}

int main() {
	//constructing a matrix
	int myints0[] = {0,2,6};
	int myints1[] = {1,1,2}; // index 1 is the answer
	int myints2[] = {1,3,5,12};
	vector<int> tmp0 (myints0,myints0+3);
	vector<int> tmp1 (myints1,myints1+3);
	vector<int> tmp2 (myints2,myints2+4);
	vector<vector<int> > matrix;
	matrix.push_back(tmp0);
	matrix.push_back(tmp1);
	matrix.push_back(tmp2);


	cout << "index with the most ones: " << find_row(matrix) << endl;
	

	return 0;
}