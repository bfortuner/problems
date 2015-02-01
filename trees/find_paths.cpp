#include <iostream>
#include <stdlib.h>
#include <queue>
#include <vector>

using namespace std;

struct Node
{
    int value;
    struct Node *left, *right;
};

// A utility function to create a new binary tree node
Node *newnode(int value)
{
    Node *temp = new Node;
    temp->value = value;
    temp->left = temp->right = NULL;
    return temp;
}
// function to find all the paths in a binary tree that sum to k starting from a node
void find_paths(Node *root,vector<int> &curr_path,vector<vector<int> > &paths, int k, int curr_sum){
	if (root == NULL){
		return;
	}
	// add current node value to path
	curr_sum+=root->value;
	curr_path.push_back(root->value);
	if (k == curr_sum)
	{
		paths.push_back(curr_path);
	}
	vector<int> left_path = curr_path;
	vector<int> right_path = curr_path;
	find_paths( root->left, left_path, paths, k, curr_sum);

	cout << "\n";
	find_paths( root->right, right_path, paths, k, curr_sum);	
}
// main function to find all paths that sum up to k in binary tree
void PathFinder(Node *root,int k){
	if (root == NULL)
	{
		cout << "Tree is empty\n";
	}

	// container to move through tree iteratively 
	queue<Node*> tmp;
	Node *tmp_node = root;
	tmp.push(tmp_node);
	vector<vector<int> > paths; // container to hold the paths

	// while there are nodes left in the tree to start at
	while(!tmp.empty())
	{
		// add child nodes
		if (tmp.front()->left != NULL){
			Node *tmp_nodeLeft = tmp.front()->left;
			tmp.push(tmp_nodeLeft);
		}
		if (tmp.front()->right != NULL){
			Node *tmp_nodeRight = tmp.front()->right;
			tmp.push(tmp_nodeRight);
		}
		
		vector<int> curr_path;
		find_paths(tmp.front(),curr_path,paths,k,0);
		tmp.pop(); // remove node
	}
	// if the vector<vector<int> > is empty
	if (paths.size() == 0)
		cout << "No paths found\n";
	else {
		// print paths
		for (int x=0; x<paths.size(); x++ ){
			cout << "Path " << x << ": ";
			for (int y=0; y<paths[x].size(); y++){
				cout << paths[x][y] << " ";
			}
			cout << "\n";
		}
	}
}


int main() {
	/* Let us construct the tree shown in above diagram */
    Node * root = newnode(5);
    root->left = newnode(3);
    root->right = newnode(2);
    root->right->left = newnode(1);
    root->right->left->right = newnode(7);
    root->right->right = newnode(-2);
    root->right->right->right = newnode(3);

    PathFinder(root,8);
	return 0;
}