#include <iostream>
using namespace std;
   int main()
{
    int arr[20], n, i, num;
     //  n should be less than 100 
    cout << "Enter Number of Elements in Array\n";
    cin >> n;
    cout << "Enter " << n << " numbers to be stored in array \n";
      
    // Read array elements
    for(i = 0; i < n; i++)
   {
        cin >> i;
    }
      
    cout << "Enter a number to search in Array\n";
    cin >> num;
       
    for(i = 0; i < n; i++)
   {
        if(i == num)
       {
            cout << "Element found at index " << i;
            break;
        }
    }
      
    if(i == num)
    {
        cout  << "Element Not Present in Input Array\n";
    }
 
    return 0;
}
