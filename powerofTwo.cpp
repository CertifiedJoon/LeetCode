#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n <= 0? 0 : !(n & (n-1));
    }
};

int main(){
    Solution sl;
    cout << sl.isPowerOfTwo(-8);
    return 0;
}
