//#include <cconio>
#include <iostream>
#include <algorithm>
#include <time.h>
using std::cout;
using std::cin;
using std::endl;

#define KEY_UP 72
#define KEY_DOWN 80
#define KEY_LEFT 75
#define KEY_RIGHT 77

int side;
int data[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

int up, down, left, right, EMPTY, count;

void swap (int *a, int *b);
void randomize ();
bool check();
void display();

int main()
{
    int c;

	cout << "Enter size of puzzle(2/3/4): ";
	cin >> side;

	randomize();
	display();
	
	while(1)
    {
        c = 0;

        switch((c=getchar())) {
        case KEY_UP:
            //cout << endl << "Up" << endl;//key up
			if(up != -1) {
				swap(&data[up], &data[EMPTY]);

				EMPTY = up;
			}
            break;
        case KEY_DOWN:
            //cout << endl << "Down" << endl;   // key down
            if(down != -1) {
				swap(&data[down], &data[EMPTY]);
				
				EMPTY = down;
			}
            break;
        case KEY_LEFT:
            //cout << endl << "Left" << endl;  // key left
            if(left != -1) {
				swap(&data[left], &data[EMPTY]);
				
				EMPTY = left;
			}
            break;
        case KEY_RIGHT:
            //cout << endl << "Right" << endl;  // key right
            if(right != -1) {
				swap(&data[right], &data[EMPTY]);
				
				EMPTY = right;
			}
            break;
        default:
            //cout << endl << "null" << endl;  // not arrow
            break;
        }
	    count++;
		display();
		if(check()) {
			cout << "**********Congrats! You Finished in " << count << " Steps********" << endl;
			break;
		}
    }

    return 0;
}

void swap (int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

// A function to generate a random permutation of arr[]
void randomize ()
{
    // Use a different seed value so that we don't get same
    // result each time we run this program
    srand ( time(NULL) );
 
    // Start from the last element and swap one by one. We don't
    // need to run for the first element that's why i > 0
    for (int i = side*side-1; i > 0; i--)
    {
        // Pick a random index from 0 to i
        int j = rand() % (i+1);
 
        // Swap arr[i] with the element at random index
        swap(&data[i], &data[j]);
    }
}

bool check()
{
	if(EMPTY != side*side -1)
		return false;

	for(int i = 0; i < side-1; i++) {
		if(i+1 != data[i])
			return false;
	}
	return true;
}

void display()
{
	system("clear");
	cout << endl << endl << endl;
	cout << "Move the blank up/down/left/right till right bottom" << endl;
	for(int i = 0; i < side; i++) {
		for(int j = 0; j < side; j++) {
			if(data[i*side + j] == 0) {
				cout << "      ";
				EMPTY = i*side + j;
			}
			else { 
				printf ("%2d    ", data[i*side + j]);
				//cout << data[i*side + j] << "    ";
			}
		}
		cout << endl << endl << endl;
	
		up = -1;
		down = -1;
		left = -1;
		right = -1;
	    
		if(EMPTY > side-1)
			up = EMPTY-side;
		if(EMPTY < side*side-side)
			down = EMPTY+side;
		if(EMPTY % side != 0)
			left = EMPTY-1;
		if((EMPTY+1)%side != 0)
			right = EMPTY+1;
	}
}
