#include <iostream>
#include <stdlib.h>
#include <cstdlib>

using namespace std;

// First Ancestor problem
// *** Assumes nodes each have unique integer values to identify them *** 

/* A tree node structure */
struct TreeNode {
	int data;
	TreeNode *left;
	TreeNode *right;
	TreeNode *parent;
};

// utility function to create a new binary tree node
struct TreeNode* newNode( int data)
{
	struct TreeNode *temp = new struct TreeNode;
	temp->data = data;
	temp->left = NULL;
	temp->right = NULL;
	temp->parent = NULL;

	return temp;
}

// Finds what level a node is on in a tree
int find_level(TreeNode *root, int num, int level){
	if (root == NULL)
		return 0;
	// if node is the one we are looking for
	if (root->data == num)
		return level;

	int down_left = find_level(root->left,num,level++);
	if (down_left != 0)
		return down_left;

	int down_right = find_level(root->right,num,level++);
	if (down_right != 0)
		return down_right;
}

// If both nodes are on the same level
// checks if parent of each node is ancestor
// if not...returns grandparent as ancestor
void same_level_ancestor(TreeNode* node1, TreeNode* node2){
	// One of the nodes is the root of the tree
	if (node1->parent == NULL || node2->parent == NULL){
		cout << "NO ANCESTOR EXISTS" << endl;
		exit(1);
	}

	// if both nodes share a parent then it is the ancestor
	if (node1->parent == node2->parent){
		cout << "ANCESTOR = " << (node1->parent)->data << endl;
		exit(1);
	}

	// if they do not share a parent but are on the same level
	// the ancestor is the grandparent
	cout << "ANCESTOR = " << ((node1->parent)->parent)->data << endl;
	exit(1);

}

// If nodes are on different levels:
// moves the younger node up to the same level as the older node 
// then calls *same_level_ancestor* function 

void different_levels(TreeNode* older, TreeNode* younger, int level_old, int level_young){
	// Nodes are now on the same level
	if (level_young = level_old){
		same_level_ancestor(older,younger);
	}
	// if not then move younger up the tree
	different_levels(older,younger->parent,level_old,level_young--);
}


void first_ancestor(TreeNode* root, TreeNode* node1, TreeNode* node2){
	if (node1 == NULL || node2 == NULL)
		cout << "Node not in tree" << endl;


	// Step 1: Find what level the nodes are on
	int level1 = find_level(root,node1->data,1);
	if (level1 == -1)
		cout << "Node1 not in tree" << endl;

	int level2 = find_level(root,node2->data,1);
	if (level2 == -1)
		cout << "Node2 not in tree" << endl;

	// Step 2: Decide which function to use;
	if (level1 == level2)
		same_level_ancestor(node1,node2);

	// if node1 is older than node2
	if (level1 < level2)
		different_levels(node1,node2,level1,level2);
	// if node 2 is older than node1
	if (level1 > level2)
		different_levels(node2,node1,level2,level1);

}

int main() {
	// create a treenode
	struct TreeNode *root = new struct TreeNode;
 
    /* Constructing tree given in the above figure */
    root = newNode(3);									// 	  Ancestor -->	3
    root->left = newNode(2);							//					^
    root->right = newNode(5);							//				  2   5  <-- node1
    root->left->left = newNode(1);						//               ^
    root->left->right = newNode(4);						//  node2 -->  1   4
  	// set parents
    root->left->parent = root;
    root->right->parent = root;
    root->left->left->parent = root->left;
    root->left->right->parent = root->left;
    // pick two nodes to use
    TreeNode *node1 = root->right;
    TreeNode *node2 = root->left->left;
 	
 	// call function to find first ancestor
    first_ancestor(root,node1,node2);

	return 0;
}