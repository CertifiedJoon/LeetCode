#include <bits/stdc++.h>
using namespace std;
class Solution{
public:
    int hammingWeight(uint32_t n){
        n -= (n >> 1) & 0x55555555; // put count of each 2 bits into those 2 bits
        n = (n & 0x33333333) + (n >> 2 & 0x33333333); // put count of each 4 bits into those 4 bits
        n = (n + (n >> 4)) & 0x0F0F0F0F; // put count of each 8 bits into those 8 bits
        return n * 0x01010101 >> 24;
    }
};

int main(){
    Solution sl;
    cout << sl.hammingWeight(00000000000000000000000000001011);
    return 0;
}
