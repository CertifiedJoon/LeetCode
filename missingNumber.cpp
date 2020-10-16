#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int result = nums.size();
        int i = 0;

        for(int num : nums){
            result ^= num;
            result ^= i++;
        }

        return result;
    }
};

int main(){
    Solution sl;
    vector<int> v = {0,1,2,3,4,6};
    cout << sl.missingNumber(v);
    return 0;
}
