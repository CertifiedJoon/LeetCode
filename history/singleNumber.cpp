#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        for(int i = 1; i < nums.size(); i++){
            nums[0] = nums[0] ^ nums[i];
        }
        return nums[0];
    }
};

int main(){
    Solution sl;
    vector<int> v = {4,1,2,1,2};
    cout << sl.singleNumber(v);
    return 0;
}
