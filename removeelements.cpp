#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int removeElement(vector<int>& nums, int val) {
    vector<int>::iterator it;
    do{
      it = find(nums.begin(), nums.end(), val);
      if (it != nums.end()) nums.erase(it);
    }while(it != nums.end());
  return nums.size();
  }
};
