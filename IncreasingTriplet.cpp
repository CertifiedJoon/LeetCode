#include <bits/stdc++.h>
using namespace std;
class Solution{
public:
  bool increasingTriplet(vector<int>& nums){
    int min = INT_MAX, second = INT_MAX;
    for (int a : nums){
      if (a <= min){
        min = a;
      }
      else if (a <= second){
        second = a;
      }
      else{
        return true;
      }
    }
    return false;
  }
};
