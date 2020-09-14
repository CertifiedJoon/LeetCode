#include <bits/stdc++.h>
using namespace std;
class Solution{
public:
  int removeDuplicates(vector<int> &nums){
    size_t l = nums.size();
    for(size_t i = 0; i < l; ++i){
      if(nums.front() == nums.back() && nums.size() > 1){
        nums.erase(nums.begin());
      } else {
        nums.push_back(nums.front());
        nums.erase(nums.begin());
      }
    }
    return nums.size();
  }
  int removeDuplicates2(vector<int>& nums){
	   nums.erase(unique(nums.begin() ,nums.end()),nums.end() );
	   return nums.size() ;
}
};
