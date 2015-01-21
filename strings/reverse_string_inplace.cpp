#include <iostream>
#include <stdlib.h>
#include <string>


//inplace reverse a sentence
using namespace std;

void inplace_reverse(string & arr, int size){
	int s = 0;
	while (size > s){
		char *start = &arr[s];
		char *tmp = &arr[size];
		char tmp2 = *tmp;
		
		*tmp = *start;
		*start = tmp2;
		s++;
		size--;
	}

}

int main() {
	string tmp = "this is my word";
	inplace_reverse(tmp,14);
	cout << tmp << endl;
	return 0;
}