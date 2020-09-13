#include <iostream>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long long int rev = 0;
        while (x){
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        return (rev > INT_MAX || rev < INT_MIN) ? 0 : rev;
    }
    bool isPalindrome(int x) {
        if (x < 0) {return false;}
        else{
            return (x == reverse(x)) ? true : false;
        }
    }
};
int main(){
  Solution sl;
  cout << sl.isPalindrome(1222) << endl;
}
