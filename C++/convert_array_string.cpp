#include <string>
#include <iostream>
using namespace std;

int main()
{

   //uint8_t arr[] = {'h', 'i', 'h', 'e','l','l','o'};   
   uint8_t arr[] = {0x23, 0x34, 0x12, 0x55, 0x57, 0x8, 0x21};
   
   string s;
   cout << "Size of arr "<< sizeof(arr) << endl;
   cout << "Actual size of arr=sizeof(arr)/sizeof(arr[0])="<< sizeof(arr)/sizeof(arr[0]) << endl;
   s.assign(arr, arr + sizeof(arr));

   cout << "string s size="<< s.size() << "string "<< s << '\n';
   
   string first_4_from_1;
   first_4_from_1.assign(s, 1, 4); //expect get ihel
   
   cout << "first 4 from 1 (ihel)" << first_4_from_1 << " sizeof " << sizeof(first_4_from_1) << endl;
   cout << "min(4,8)=" << min(4,8) << endl;
}
