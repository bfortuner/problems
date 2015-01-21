
// C++ program to Implement Binary Heap
// use "./start.exe" in the command_line to run
// 

#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

// Binary Heap Structure
class BH {

	public:
		// CONSTRUCTOR
		BH() {}

		// ACCESSORS
		int get_min();
		int get_size();

		// MODIFIERS
		void insert(int element);
		void delete_min();
		
		// OUTPUT
		void print_bh();

	private:
		
		//REPRESENATION
		std::vector<int> heap;
		
		void heapify_up(int start);
		void heapify_down(int start);
		int get_left_child(int element);
		int get_right_child(int element);
		int get_parent(int element);


};


int BH::get_size()
{
	return heap.size();
}

void BH::insert(int element){
	heap.push_back(element);
	heapify_up(heap.size()-1);
}

void BH::delete_min() 
{
	if (heap.size() == 0)
		return;

	heap[0] = heap.at(heap.size() -1);
	heap.pop_back();
	heapify_down(0);
	cout << "Element deleted" << endl;
}

int BH::get_min() 
{
	if (heap.size() == 0)
		return -1;
	else 
		return heap.front();
}

void BH::print_bh() 
{
	vector<int>::iterator pos = heap.begin();
	cout << "Heap --> ";
	while (pos != heap.end()){
		cout << *pos << " ";
		pos++;
	}
	cout << endl;
}

int BH::get_left_child(int parent)
{
	int l = 2*parent +1;
	if (l <heap.size())
		return l;
	else 
		return -1;
}

int BH::get_right_child(int parent)
{
	int r = 2*parent +2;
	if (r < heap.size())
		return r;
	else
		return -1;
}

int BH::get_parent(int child)
{
	int p = (child -1)/2;
	if (child == 0)
		return -1;
	else 
		return p;
}

void BH::heapify_up(int start)
{
	if (start >=0 && get_parent(start) >=0 && heap[get_parent(start)] > heap[start]){
		int tmp = heap[start];
		heap[start] = heap[get_parent(start)];
		heap[get_parent(start)] = tmp;
		heapify_up(get_parent(start));
	}
}

void BH::heapify_down(int start)
{
	int child = get_left_child(start);
	int child1 = get_right_child(start);
	if (child >= 0 && child1 >= 0 && heap[child] > heap[child1]){
		child = child1;
	}
	if (child >0){
		int tmp = heap[start];
		heap[start] = heap[child];
		heap[child]=tmp;
		heapify_down(child);
	}
}

int main() {

	BH h;
	while (1)
    {
        cout<<"------------------"<<endl;
        cout<<"Operations on Heap"<<endl;
        cout<<"------------------"<<endl;
        cout<<"1.Insert Element"<<endl;
        cout<<"2.Delete Minimum Element"<<endl;
        cout<<"3.Extract Minimum Element"<<endl;
        cout<<"4.Print Heap"<<endl;
        cout<<"5.Exit"<<endl;
        int choice, element;
        cout<<"Enter your choice: ";
        cin>>choice;
        switch(choice)
        {
        case 1:
            cout<<"Enter the element to be inserted: ";
            cin>>element;
            h.insert(element);
            break;
        case 2:
            h.delete_min();
            break;
        case 3:
            cout<<"Minimum Element: ";
            if (h.get_min() == -1)
            {
                cout<<"Heap is Empty"<<endl;
            }
            else
                cout<<"Minimum Element:  "<<h.get_min()<<endl;
            break;
        case 4:
            cout<<"Displaying elements of Hwap:  ";
            h.print_bh();
            break;
        case 5:
            exit(1);
        default:
            cout<<"Enter Correct Choice"<<endl;
        }
    }
	return 0;
}