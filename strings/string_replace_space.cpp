#include <iostream>
#include <stdlib.h>

using namespace std;

// replaces each space in the string with '%20'
// Linear time solution
string replace_Space(string &word){
	if (word.size() == 0)
		return "nothing to return";
	string word2="";
	for (int x=0;x<word.size();x++){
		if (word[x]==' ')
			word2+= "%20";
		else
			word2+=word[x];
	}

	return word2;
}


int main(){

	string test1 = "";
	string test2 = "%20%20%20%20%20";
	string test3 = "______ ___weoiru";
	string test4 = "!!! !$$ $# &$(*";
	string test5 = "       ";
	string test6 = " hello my name Is Dog Boy";
	string test7 = "/ ";

	cout << replace_Space(test1) << endl;
	cout << replace_Space(test2) << endl;
	cout << replace_Space(test3) << endl;
	cout << replace_Space(test4) << endl;
	cout << replace_Space(test5) << endl;
	cout << replace_Space(test6) << endl;
	cout << replace_Space(test7) << endl;

	return 0;
}